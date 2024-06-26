from __future__ import annotations
from dtu import Parameters, dtu, GPU
import torch
import wandb
from time import time as seconds
from src.models.Model import Model
from src.utils import read_json, save_model
from src.evaluator import Evaluator
from src.data.T5dataset import T5Dataset
from torch.utils.data import DataLoader
from src.utils import split_data
import json
import os


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 82800

    data_name: str = "sample_data/train/data.json"
    prediction_name: str = "sample_data/valid/data.json"
    test_name: str = "sample_data/valid/data.json"

    model_type: str = "t5"
    t5_model_name: str = "t5-base"

    batch_size: int = 1

    make_predictions_after: int = 2
    lr: float = 0.001
    max_length_source: int = 512
    max_length_target: int = 512
    append_scheme_info: bool = False
    give_extra_info: bool = False

    def run(self, name: str, append_scheme_info: bool, give_extra_info: bool, max_length_source: int, max_length_target: int, lr: float, t5_model_name: str, isServer: bool, make_predictions_after: int, time: int, batch_size: int, model_type:str, data_name:str, prediction_name: str, test_name: str) -> None:
        start = seconds()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tables_file = "mimic_iv/tables.json"
        if (isServer):
            wandb.init(project="ML_healthcare", name=name, config={"batch_size": batch_size, "isServer": isServer, "device": str(device)})
        
        model = Model(model_type, t5_model_name, max_length_source, max_length_target, lr)

        raw_data = read_json(data_name)
        data = []
        [data.append({"id": d["id"], "question": d["question"]}) for d in raw_data]
        labels = {d["id"]: d["query"] for d in raw_data}

        raw_valid_data = read_json(prediction_name)
        valid_data = []
        [valid_data.append({"id": d["id"], "question": d["question"]}) for d in raw_valid_data]
        
        raw_test_data = read_json(test_name)
        test_data = []
        [test_data.append({"id": d["id"], "question": d["question"]}) for d in raw_test_data]


        dataset_train = T5Dataset(model.tokenizer, data, labels, is_test=False, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        train_loader = DataLoader(dataset_train, batch_size=batch_size, collate_fn=dataset_train.collate_fn, shuffle=True)

        dataset_valid = T5Dataset(model.tokenizer, valid_data, None, is_test=True, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        valid_loader = DataLoader(dataset_valid, batch_size=batch_size, collate_fn=dataset_valid.collate_fn, shuffle=False)

        dataset_test = T5Dataset(model.tokenizer, test_data, None, is_test=True, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
        test_loader = DataLoader(dataset_test, batch_size=batch_size, collate_fn=dataset_test.collate_fn, shuffle=False)

        for i in range(1000):
            for j, batch in enumerate(train_loader):
                train_loss = model.trainer(batch)
                if (isServer):
                    wandb.log({"train_loss": train_loss})
                else:
                    print(f"train_loss: {train_loss:.6f}")

            # eval on prediction data
            out_eval = model.model.generate(model.tokenizer, valid_loader)
            pred_dict = {out["id"]: out["pred"] for out in out_eval}

            # save pred_dict as json
            with open(f"predictions/{name}.json", "w") as f:
                json.dump(pred_dict, f)

            # eval on test data
            out_eval = model.model.generate(model.tokenizer, test_loader)
            pred_dict = {out["id"]: out["pred"] for out in out_eval}

            # save pred_dict as json
            with open(f"predictions/{name}_test.json", "w") as f:
                json.dump(pred_dict, f)

            if seconds() - start > time:
                print(f"Time limit reached: epoch {i}")
                break
            
            if i > 1:
                break




Defaults.start()