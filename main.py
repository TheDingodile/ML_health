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

    model_type: str = "t5"

    batch_size: int = 1

    def run(self, name: str, isServer: bool, time: int, batch_size: int, model_type:str, data_name:str, labels_name: str, answer_name: str) -> None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if (isServer):
            wandb.init(project="ML_healthcare", name=name, config={"batch_size": batch_size, "isServer": isServer, "device": str(device)})
        
        model = Model(model_type)
        evaluator = Evaluator()
        data = read_json(data_name)["data"]
        labels = read_json(labels_name)
        data_train, label_train, data_test, label_test = split_data(data, labels, every=5)
        # answer = read_json(answer_name)
        dataset_train = T5Dataset(model.tokenizer, data_train, label_train, is_test=False, append_schema_info=True, tables_file="mimic_iv/tables.json")
        train_loader = DataLoader(dataset_train, batch_size=batch_size, collate_fn=dataset_train.collate_fn, shuffle=True)
        dataset_test = T5Dataset(model.tokenizer, data_test, label_test, is_test=False, append_schema_info=True)
        test_loader = DataLoader(dataset_test, batch_size=batch_size, collate_fn=dataset_test.collate_fn, shuffle=False, tables_file="mimic_iv/tables.json")

        for i in range(1000):

            # eval on test data
            out_eval = model.model.generate(model.tokenizer, test_loader)
            real_dict = {out["id"]: out["real"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] for out in out_eval}
            scores = evaluator.evaluate(real_dict, pred_dict, name)
            if (isServer):
                scores = {f"eval_{k}": v for k, v in scores.items()}
                wandb.log(scores)
            else:
                print("eval", scores)

            # eval on train data
            out_eval = model.model.generate(model.tokenizer, train_loader)
            real_dict = {out["id"]: out["real"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] for out in out_eval}
            scores = evaluator.evaluate(real_dict, pred_dict, name)
            if (isServer):
                scores = {f"train_{k}": v for k, v in scores.items()}
                wandb.log(scores)
            else:
                print("train", scores)

            for j, batch in enumerate(train_loader):
                train_loss = model.trainer(batch)

            if (isServer):
                wandb.log({"epochs": i, "train_loss": train_loss})
            else:
                print(f"epochs: {i}, train_loss: {train_loss:.6f}")




Defaults.start()