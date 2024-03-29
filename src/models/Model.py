from src.models.dummy_model import Dummymodel
import torch.nn as nn

class Model(nn.Module):
    def __init__(self, model_type: str = "dummy"):
        super(Model, self).__init__()
        if model_type == "dummy":
            self.model = Dummymodel()

    def forward(self, input_data):
        return self.model.generate(input_data)
    
    def save(self, path: str):
        pass
