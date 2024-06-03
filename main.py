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
    prediction_name: str = "sample_data/valid/data.json"

    model_type: str = "t5"
    t5_model_name: str = "t5-base"

    batch_size: int = 1

    make_predictions_after: int = 2
    lr: float = 0.001
    max_length_source: int = 512
    max_length_target: int = 512
    append_scheme_info: bool = True
    give_extra_info: bool = True

    def run(self, name: str, append_scheme_info: bool, give_extra_info: bool, max_length_source: int, max_length_target: int, lr: float, t5_model_name: str, isServer: bool, make_predictions_after: int, time: int, batch_size: int, model_type:str, data_name:str, prediction_name: str) -> None:
        start = seconds()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tables_file = "mimic_iv/tables.json"
        if (isServer):
            wandb.init(project="ML_healthcare", name=name, config={"batch_size": batch_size, "isServer": isServer, "device": str(device)})
        
        model = Model(model_type, t5_model_name, max_length_source, max_length_target, lr)
        evaluator = Evaluator()

        raw_data = read_json(data_name)
        data = {d["id"]: d["question"] for d in raw_data}
        labels = {d["id"]: d["query"] for d in raw_data}

        raw_valid_data = read_json(prediction_name)

        valid_data = {d["id"]: d["question"] for d in raw_valid_data}


        dataset_train = T5Dataset(model.tokenizer, data, labels, is_test=False, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        train_loader = DataLoader(dataset_train, batch_size=batch_size, collate_fn=dataset_train.collate_fn, shuffle=True)

        dataset_valid = T5Dataset(model.tokenizer, valid_data, None, is_test=True, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        valid_loader = DataLoader(dataset_valid, batch_size=batch_size, collate_fn=dataset_valid.collate_fn, shuffle=False)

        for i in range(1000):
            for j, batch in enumerate(train_loader):
                train_loss = model.trainer(batch)
                if (isServer):
                    wandb.log({"train_loss": train_loss})
                else:
                    print(f"train_loss: {train_loss:.6f}")

            if i >= make_predictions_after:
                # eval on prediction data
                out_eval = model.model.generate(model.tokenizer, valid_loader)
                pred_dict = {out["id"]: out["pred"] for out in out_eval}
                evaluator.save_predictions(name, pred_dict)
                break

            if seconds() - start > time:
                print(f"Time limit reached: epoch {i}")
                break




Defaults.start()