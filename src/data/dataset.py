from src.models.Model import Model
import torch


class dataset():
    def __init__(self, data: dict[str, str], labels: dict[str, str], split_percentage: float, model: Model) -> None:
        self.train_data, self.train_labels, self.test_data, self.test_labels = {}, {}, {}, {}


        for i, key in enumerate(data):
            if i < split_percentage * len(data):
                self.train_data[key] = data[key]
                self.train_labels[key] = labels[key]
            else:
                self.test_data[key] = data[key]
                self.test_labels[key] = labels[key]

        question_encoded = model.encode_file(questions)


    def preprocess_sample(self, sample, append_schema_info=False):
        """
        Processes a single data sample, adding schema description to the question.
        """
        question = sample["question"]

        if append_schema_info:
            if self.db_json:
                tables_json = [db for db in self.db_json if db["db_id"] == self.db_id][0]
                schema_description = self.get_schema_description(tables_json)
                question += f" {schema_description}"
            return question
        else:
            return question
        

    def get_schema_description(self, tables_json, shuffle_schema=False):
        """
        Generates a textual description of the database schema.
        """
        table_names = tables_json["table_names_original"]
        if shuffle_schema:
            self.random.shuffle(table_names)

        columns = [
            (column_name[0], column_name[1].lower(), column_type.lower())
            for column_name, column_type in zip(tables_json["column_names_original"], tables_json["column_types"])
        ]

        schema_description = [""]
        for table_index, table_name in enumerate(table_names):
            table_columns = [column[1] for column in columns if column[0] == table_index]
            if shuffle_schema:
                self.random.shuffle(table_columns)
            column_desc = " , ".join(table_columns)
            schema_description.append(f"{table_name.lower()} : {column_desc}")

        return " | ".join(schema_description)
    


    def collate_fn(self, batch, return_tensors='pt', padding=True, truncation=True):
        """
        Collate function for the DataLoader.
        """
        ids = [x["id"] for x in batch]
        input_ids = torch.stack([x["source_ids"] for x in batch]) # BS x SL
        masks = torch.stack([x["source_mask"] for x in batch]) # BS x SL
        pad_token_id = self.tokenizer.pad_token_id
        source_ids, source_mask = trim_batch(input_ids, pad_token_id, attention_mask=masks)

        if self.is_test:
            return {
                "source_ids": source_ids,
                "source_mask": source_mask,
                "id": ids,
            }
        else:
            target_ids = torch.stack([x["target_ids"] for x in batch]) # BS x SL
            target_ids = trim_batch(target_ids, pad_token_id)
            return {
                "source_ids": source_ids,
                "source_mask": source_mask,
                "target_ids": target_ids,
                "id": ids,
            }

def trim_batch(input_ids, pad_token_id, attention_mask=None):
    """
    Trims padding from batches of tokenized text.
    """
    keep_column_mask = input_ids.ne(pad_token_id).any(dim=0)
    if attention_mask is None:
        return input_ids[:, keep_column_mask]
    else:
        return (input_ids[:, keep_column_mask], attention_mask[:, keep_column_mask])
