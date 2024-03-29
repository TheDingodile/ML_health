from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, T5Tokenizer, T5ForConditionalGeneration, get_linear_schedule_with_warmup
import torch.nn as nn

class T5Model(nn.Module):
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.model_name = "t5-base"
        self.network = T5ForConditionalGeneration.from_pretrained(self.model_name).to(device)

    def trainer(self, input_ids, attention_mask, labels, tokenizer, optimizer):
        self.network.train()
        labels[labels[:,:]==tokenizer.pad_token_id] = -100
        labels = labels.to(self.device)
        loss = self.network(input_ids=input_ids, attention_mask=attention_mask, labels=labels)[0]
        loss.backward()
        optimizer.step()
        self.network.eval()
        print(f"Loss: {loss.item()}")
        return loss.detach().cpu().numpy()

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
    

