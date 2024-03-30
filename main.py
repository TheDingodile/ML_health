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
        # answer = read_json(answer_name)
        dataset_train = T5Dataset(model.tokenizer, data, labels, is_test=False, append_schema_info=True)
        train_loader = DataLoader(dataset_train, batch_size=batch_size, collate_fn=dataset_train.collate_fn, shuffle=True)
        dataset_test = T5Dataset(model.tokenizer, data, labels, is_test=False, append_schema_info=True)
        test_loader = DataLoader(dataset_test, batch_size=batch_size, collate_fn=dataset_test.collate_fn, shuffle=False)

        for i in range(1000):
            for j, batch in enumerate(train_loader):
                train_loss = model.trainer(batch)
                if (isServer):
                    wandb.log({"trains": j, "train_loss": train_loss})
                else:
                    print(f"trains: {j}, train_loss: {train_loss:.6f}")

            out_eval = model.model.generate(model.tokenizer, test_loader)
            # make dict with id of questions as keys and sql as values for both real and pred
            real_dict = {out["id"]: out["real"] for out in out_eval}
            pred_dict = {out["id"]: out["pred"] for out in out_eval}
            scores = evaluator.evaluate(real_dict, pred_dict, name)
            if (isServer):
                wandb.log(scores)
            else:
                print(scores)


Defaults.start()