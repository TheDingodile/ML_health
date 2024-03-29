import torch.nn as nn


class Dummymodel(nn.Module):
    def __init__(self):
        super().__init__()

    def trainer(self, input_ids, attention_mask, labels, tokenizer):
        return 0

    
    def generate(self, input_data):
        """
        Arguments:
            input_data: list of python dictionaries containing 'id' and 'input'
        Returns:
            labels: python dictionary containing sql prediction or 'null' values associated with ids
        """
        labels = {}

        for sample in input_data:
            labels[sample["id"]] = "null"

        return labels