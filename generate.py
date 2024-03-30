from main import Defaults, GPU

# Defaults(name="test_real_data_16", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json")


# Defaults(name="tester16b", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json")

# Defaults(name="tester32b", 
#          GPU=GPU.a80, 
#          batch_size=32, 
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json")

# Defaults(name="tester16c", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json")

# Defaults(name="log_entropy_nulls", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

Defaults(name="prediction_test16", 
         GPU=GPU.v32, 
         batch_size=16, 
         eval_fraction=50,
         model_type="t5",
         data_name="mimic_iv/train/data.json",  
         labels_name="mimic_iv/train/label.json",
         answer_name="mimic_iv/train/answer.json",
         prediction_name="mimic_iv/valid/data.json")

Defaults(name="prediction_test32", 
         GPU=GPU.a80, 
         batch_size=32, 
         eval_fraction=50,
         model_type="t5",
         data_name="mimic_iv/train/data.json",  
         labels_name="mimic_iv/train/label.json",
         answer_name="mimic_iv/train/answer.json",
         prediction_name="mimic_iv/valid/data.json")
