from __future__ import annotations
from dtu import Parameters, dtu, GPU
import torch
import wandb
from time import time as seconds
from src.models.Model import Model
from src.utils import read_json, save_predictions, save_model
from src.evaluator import Evaluator
from src.data.T5dataset import T5Dataset
from torch.utils.data import DataLoader
from src.utils import split_data


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 82800

    data_name: str = "sample_data/train/data.json"
    labels_name: str = "sample_data/train/label.json"
    answer_name: str = "sample_data/train/answer.json"

    prediction_name: str = "sample_data/valid/data.json"
    prediction_name2: str = "sample_data/test/data.json"

    model_type: str = "t5"
    t5_model_name: str = "t5-base"

    batch_size: int = 1
    eval_fraction: int = 4

    null_chance_boundary: float = 0.5
    make_predictions_after: int = 5
    lr: float = 0.001
    max_length_source: int = 512
    max_length_target: int = 512
    append_scheme_info: bool = True
    give_extra_info: bool = True

    def run(self, name: str, eval_fraction: int, append_scheme_info: bool, give_extra_info: bool, max_length_source: int, max_length_target: int, lr: float, t5_model_name: str, isServer: bool, make_predictions_after: int, time: int, batch_size: int, model_type:str, data_name:str, labels_name: str, answer_name: str, prediction_name: str, prediction_name2: str, null_chance_boundary: float) -> None:
        start = seconds()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tables_file = "mimic_iv/tables.json"
        if (isServer):
            wandb.init(project="ML_healthcare", name=name, config={"batch_size": batch_size, "isServer": isServer, "device": str(device)})
        
        model = Model(model_type, t5_model_name, max_length_source, max_length_target, lr)
        evaluator = Evaluator()
        data = read_json(data_name)["data"]
        labels = read_json(labels_name)
        data_train, label_train, data_test, label_test, data_train_small, label_train_small = split_data(data, labels, every=eval_fraction)
        # answer = read_json(answer_name)
        prediction_data = read_json(prediction_name)["data"]
        prediction_data2 = read_json(prediction_name2)["data"]

        dataset_train = T5Dataset(model.tokenizer, data_train, label_train, is_test=False, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        train_loader = DataLoader(dataset_train, batch_size=batch_size, collate_fn=dataset_train.collate_fn, shuffle=True)
        dataset_test = T5Dataset(model.tokenizer, data_test, label_test, is_test=False, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        test_loader = DataLoader(dataset_test, batch_size=batch_size, collate_fn=dataset_test.collate_fn, shuffle=False)
        dataset_train_small = T5Dataset(model.tokenizer, data_train_small, label_train_small, is_test=False, append_schema_info=True, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        train_loader_small = DataLoader(dataset_train_small, batch_size=batch_size, collate_fn=dataset_train_small.collate_fn, shuffle=False)

        dataset_val = T5Dataset(model.tokenizer, prediction_data, None, is_test=True, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        val_loader = DataLoader(dataset_val, batch_size=batch_size, collate_fn=dataset_val.collate_fn, shuffle=False)
        dataset_final = T5Dataset(model.tokenizer, prediction_data2, None, is_test=True, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        final_loader = DataLoader(dataset_final, batch_size=batch_size, collate_fn=dataset_test.collate_fn, shuffle=False)

        for i in range(1000):
            
            for j, batch in enumerate(train_loader):
                train_loss = model.trainer(batch)
                if (isServer):
                    wandb.log({"train_loss": train_loss})
                else:
                    print(f"train_loss: {train_loss:.6f}")

            # eval on test data
            out_eval = model.model.generate(model.tokenizer, test_loader)
            real_dict = {out["id"]: out["real"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] if out["prob_null"] < null_chance_boundary else 'null' for out in out_eval}
            scores = evaluator.evaluate(real_dict, pred_dict, name)
            if (isServer):
                scores = {f"eval_{k}": v for k, v in scores.items()}
                wandb.log(scores)
            else:
                print("eval", scores)

            # eval on train data
            out_eval = model.model.generate(model.tokenizer, train_loader_small)
            real_dict = {out["id"]: out["real"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] if out["prob_null"] < null_chance_boundary else 'null' for out in out_eval}
            scores = evaluator.evaluate(real_dict, pred_dict, name)
            if (isServer):
                scores = {f"train_{k}": v for k, v in scores.items()}
                wandb.log(scores)
            else:
                print("train", scores)

            if i >= make_predictions_after:
                # eval on prediction data
                out_eval = model.model.generate(model.tokenizer, val_loader)
                pred_dict = {out["id"]: out["pred"] if out["prob_null"] < null_chance_boundary else 'null' for out in out_eval}
                evaluator.save_predictions(name, pred_dict, out_eval)

                out_eval = model.model.generate(model.tokenizer, final_loader)
                pred_dict = {out["id"]: out["pred"] if out["prob_null"] < null_chance_boundary else 'null' for out in out_eval}
                evaluator.save_predictions(name + "test", pred_dict, out_eval)
                break

            if seconds() - start > time:
                print(f"Time limit reached: epoch {i}")
                break




Defaults.start()