from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, T5Tokenizer, T5ForConditionalGeneration, get_linear_schedule_with_warmup
import torch.nn as nn
import torch

class T5Model(nn.Module):
    def __init__(self, device, model_name):
        super().__init__()
        self.device = device
        self.model_name = model_name
        self.network = T5ForConditionalGeneration.from_pretrained(self.model_name).to(device)

    def trainer(self, input_ids, attention_mask, labels, tokenizer, optimizer):
        self.network.train()
        labels[labels[:,:]==tokenizer.pad_token_id] = -100
        labels = labels.to(self.device)
        loss = self.network(input_ids=input_ids, attention_mask=attention_mask, labels=labels)[0]
        loss.backward()
        optimizer.step()
        self.network.eval()
        return loss.detach().cpu().numpy()

    def generate(self, tokenizer, eval_loader):
        max_length = 512
        num_beams = 1
        num_samples = 1
        # Disable gradient calculations for efficiency, as they are not needed in evaluation.
        with torch.no_grad():
            out_eval = []

            # Iterate over batches of data in the evaluation dataset.
            for batch in eval_loader:
                # Extract relevant data from the batch.
                ids = batch["id"]
                source_ids = batch["source_ids"].to(self.device)
                attention_mask = batch["source_mask"].to(self.device)

                # Generate predictions using the model.
                generation_output = self.network.generate(
                    input_ids=source_ids,
                    max_length=max_length,
                    num_beams=num_beams,
                    return_dict_in_generate=True,
                    output_scores=True,
                )

                # Move the generated sequences to the CPU if using CUDA.
                preds = generation_output["sequences"].cpu() if self.device == "cuda" else generation_output["sequences"]

                # Process logits and calculate probabilities and entropies.
                logits = torch.stack(generation_output["scores"], dim=1)[:: int(num_beams / num_samples)]
                logits = logits.cpu() if self.device == "cuda" else logits
                probs = torch.softmax(logits, dim=2).float()
                log_probs = torch.log_softmax(logits, dim=2).float()
                entropies = (torch.sum(probs * log_probs, axis=2) * (-1)).cpu().numpy()
                null_voca_idx = 206
                prob_null = probs[:, 0, null_voca_idx]

                # Determine if the current batch is for testing or training.
                is_test = True
                if "target_ids" in batch:
                    is_test = False
                    reals = batch["target_ids"]

                # Initialize lists to store predictions, probabilities, and entropies.
                pred_list = []
                entropy_list = []

                # Process each prediction in the batch.
                for idx in range(len(preds)):
                    pred = preds[idx]
                    pred_tensor = preds[idx][1:]
                    entropy_truncated = entropies[idx].tolist()

                    # Truncate the prediction at the end-of-sequence token, if present.
                    if tokenizer.eos_token_id in pred_tensor:
                        pred_eos_idx = torch.nonzero(pred_tensor == tokenizer.eos_token_id)[0].item()
                        entropy_truncated = entropy_truncated[: pred_eos_idx + 1]

                    pred_list.append(pred)
                    entropy_list.append(entropy_truncated)

                # Construct the output results for each prediction.
                for idx in range(len(preds)):
                    result = {
                        "id": ids[idx],
                        "question": tokenizer.decode(source_ids[idx], skip_special_tokens=True),
                        "pred": tokenizer.decode(pred_list[idx], skip_special_tokens=True),
                        "entropy": entropy_list[idx],
                        "source_ids": source_ids[idx].cpu().numpy().tolist(),
                        "pred_ids": pred_list[idx].cpu().numpy().tolist(),
                        "prob_null": prob_null[idx].cpu().numpy().tolist(),
                    }

                    # Include the real target output if it's training data.
                    if not is_test:
                        result["real"] = tokenizer.decode(reals[idx], skip_special_tokens=True)

                    out_eval.append(result)

            return out_eval