from src.models.dummy_model import Dummymodel
from src.models.T5_model import T5Model
import torch.nn as nn
import torch
from transformers import T5Tokenizer
from torch import Tensor

class Model(nn.Module):
    def __init__(self, model_type: str, t5_model_name: str, max_length_source: int, max_length_target: int, lr: float):
        super(Model, self).__init__()
        self.max_length_source = max_length_source
        self.max_length_target = max_length_target
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = t5_model_name
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        if model_type == "dummy":
            self.model = Dummymodel()
            self.optimizer = None
        elif model_type == "t5":
            self.model = T5Model(self.device, self.model_name, max_length_target)
            self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)

    def trainer(self, batch: dict[str: Tensor]):
        """
        Trains the model using the given batch.
        """
        self.optimizer.zero_grad()
        input_ids = batch["source_ids"].to(self.device)
        attention_mask = batch["source_mask"].to(self.device)
        labels = batch["target_ids"].to(self.device)
        loss = self.model.trainer(input_ids, attention_mask, labels, self.tokenizer, self.optimizer)
        return loss
    

    def forward(self, input_data):
        return self.model.generate(input_data)
    
    def save(self, path: str):
        pass

    def encode_file(self, tokenizer, text):
        """
        Tokenizes the text and returns tensors.
        """
        return tokenizer(
            text,
            max_length=self.max_length_source,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )

    def add_extra_tokens(self):
        add_tokens = ["<", "<=", "<>"]
        self.tokenizer.add_tokens(add_tokens)
        self.model.network.resize_token_embeddings(len(self.tokenizer))

