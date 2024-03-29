from src.models.dummy_model import Dummymodel
from src.models.T5_model import T5Model
import torch.nn as nn
import torch
from transformers import T5Tokenizer
from torch import Tensor

class Model(nn.Module):
    def __init__(self, model_type: str = "dummy", tokenizer=None):
        super(Model, self).__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = "t5-base"
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        if model_type == "dummy":
            self.model = Dummymodel()
            self.optimizer = None
        elif model_type == "t5":
            self.model = T5Model(self.device)
            self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)

    def trainer(self, batch: dict[str: Tensor]):
        """
        Trains the model using the given batch.
        """
        self.optimizer.zero_grad()
        input_ids = batch["source_ids"].to(self.device)
        attention_mask = batch["source_mask"].to(self.device)
        labels = batch["target_ids"].to(self.device)
        self.model.trainer(input_ids, attention_mask, labels, self.tokenizer, self.optimizer)


    def forward(self, input_data):
        return self.model.generate(input_data)
    
    def save(self, path: str):
        pass

    def encode_file(tokenizer, text):
        """
        Tokenizes the text and returns tensors.
        """
        return tokenizer(
            text,
            max_length=512,
            truncation=True,
            padding=True,
            return_tensors="pt",
        )

    def add_extra_tokens(self):
        add_tokens = ["<", "<=", "<>"]
        self.tokenizer.add_tokens(add_tokens)
        self.model.network.resize_token_embeddings(len(self.tokenizer))

