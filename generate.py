from main import Defaults, GPU

Defaults(name="test_real_data", 
         GPU=GPU.v32, 
         batch_size=128, 
         model_type="t5",
         data_name="mimic_iv/train/data.json",
         labels_name="mimic_iv/train/label.json",
         answer_name="mimic_iv/train/answer.json")
