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

    batch_size: int = 16




    def run(self, isServer: bool, time: int, batch_size: int, model_type:str, name:str, data_name:str, labels_name: str, answer_name: str) -> None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = Model(model_type)
        evaluator = Evaluator()
        data = read_json(data_name)["data"]
        labels = read_json(labels_name)
        # answer = read_json(answer_name)
        dataset_train = T5Dataset(model.tokenizer, data, labels, is_test=False, append_schema_info=True)
        train_loader = DataLoader(dataset_train, batch_size=batch_size, collate_fn=dataset_train.collate_fn, shuffle=False)

        for batch in train_loader:
            model.trainer(batch)

        # split data into train and test
        predictions = model(data)
        evaluator.evaluate(labels, predictions, name)
        save_predictions(name, predictions)
        save_model(name, model)


Defaults.start()