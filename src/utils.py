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

def split_data(data, labels, every: int):
    data_train = []
    label_train = dict()
    data_test = []
    label_test = dict()
    for i, d in enumerate(data):
        if i % every == 0:
            data_test.append(d)
            label_test[d["id"]] = labels[d["id"]]
        else:
            data_train.append(d)
            label_train[d["id"]] = labels[d["id"]]
    return data_train, label_train, data_test, label_test