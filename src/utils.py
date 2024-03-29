import json
import os
from src.models.Model import Model


def read_json(path):
    with open(path) as f:
        file = json.load(f)
    return file

def save_predictions(name: str, predictions: dict[str, list[str]]):
    path = os.path.join('predictions', name)
    # check that the directory exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, 'prediction.json', ), 'w') as f:
        json.dump(predictions, f)

def save_model(name: str, model: Model):
    path = os.path.join('trained_models', name)
    # check that the directory exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)
    model.save(os.path.join(path))