from main import Defaults, GPU

Defaults(name="test_real_data_16", 
         GPU=GPU.v32, 
         batch_size=16, 
         model_type="t5",
         data_name="mimic_iv/train/data.json",
         labels_name="mimic_iv/train/label.json",
         answer_name="mimic_iv/train/answer.json")
Defaults(name="test_real_data_32", 
         GPU=GPU.v32, 
         batch_size=32, 
         model_type="t5",
         data_name="mimic_iv/train/data.json",
         labels_name="mimic_iv/train/label.json",
         answer_name="mimic_iv/train/answer.json")
