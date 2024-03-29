from __future__ import annotations
from dtu import Parameters, dtu, GPU
import torch
import wandb
from time import time as seconds
from src.models.Model import Model
from src.utils import read_json, save_predictions, save_model
from src.evaluator import Evaluator


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 82800

    data_name: str = "mimic_iv/train/data.json"
    labels_name: str = "mimic_iv/train/label.json"
    answer_name: str = "mimic_iv/train/answer.json"



    def run(self, isServer: bool, time: int, name:str, data_name:str, labels_name: str, answer_name: str) -> None:
        model = Model()
        evaluator = Evaluator()
        data = read_json(data_name)["data"]
        labels = read_json(labels_name)
        answer = read_json(answer_name)
        predictions = model(data)
        evaluator.evaluate(labels, predictions, name)
        save_predictions(name, predictions)
        save_model(name, model)


Defaults.start()