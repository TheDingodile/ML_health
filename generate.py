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

# Defaults(name="prediction_test16", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="prediction_test32", 
#          GPU=GPU.a80, 
#          batch_size=32, 
#          eval_fraction=50,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="null_safety01", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.1,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="null_safety001", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.01,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="null_safety0001", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.001,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")



# Defaults(name="null_safety025", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.25,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="null_safety000001", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.00001,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="null_safety00001", 
#          GPU=GPU.a80, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.0001,
#          model_type="t5",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="null_safety01Large", 
#          GPU=GPU.a80, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.1,
#          model_type="t5",
#          t5_model_name="t5-large",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="log_entropy", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=0.1,
#          model_type="t5",
#          t5_model_name="t5-base",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="LargeTest_fix", 
#          GPU=GPU.v32, 
#          batch_size=4, 
#          eval_fraction=50,
#          null_chance_boundary=0.1,
#          model_type="t5",
#          t5_model_name="t5-large",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="LargeTesta40", 
#          GPU=GPU.a40, 
#          batch_size=8, 
#          eval_fraction=50,
#          null_chance_boundary=0.1,
#          model_type="t5",
#          t5_model_name="t5-large",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="save_predictions", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=1,
#          model_type="t5",
#          t5_model_name="t5-base",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="save_predictions2", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=1,
#          model_type="t5",
#          t5_model_name="t5-base",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="save_predictions3", 
#          GPU=GPU.v32, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=1,
#          model_type="t5",
#          t5_model_name="t5-base",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="more_buffer", 
#          GPU=GPU.v32, 
#          batch_size=8, 
#          eval_fraction=50,
#          null_chance_boundary=1,
#          model_type="t5",
#          t5_model_name="t5-base",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# Defaults(name="more_buffer_a80", 
#          GPU=GPU.a80, 
#          batch_size=16, 
#          eval_fraction=50,
#          null_chance_boundary=1,
#          model_type="t5",
#          t5_model_name="t5-base",
#          data_name="mimic_iv/train/data.json",  
#          labels_name="mimic_iv/train/label.json",
#          answer_name="mimic_iv/train/answer.json",
#          prediction_name="mimic_iv/valid/data.json")

# for i in range(6):
#     Defaults(name=f"Ensemble{i}", 
#             GPU=GPU.v32, 
#             batch_size=16, 
#             eval_fraction=25,
#             null_chance_boundary=1,
#             model_type="t5",
#             t5_model_name="t5-base",
#             data_name="mimic_iv/train/data.json",  
#             labels_name="mimic_iv/train/label.json",
#             answer_name="mimic_iv/train/answer.json",
#             prediction_name="mimic_iv/valid/data.json")
    
# Defaults(name="Ensemble6", 
#         GPU=GPU.a80, 
#         batch_size=16, 
#         eval_fraction=25,
#         null_chance_boundary=1,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")

# Defaults(name="Ensemble7", 
#         GPU=GPU.a40, 
#         batch_size=16, 
#         eval_fraction=25,
#         null_chance_boundary=1,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")

# Defaults(name="Add_information", 
#         GPU=GPU.a80, 
#         batch_size=16, 
#         eval_fraction=25,
#         max_length_source=1024,
#         null_chance_boundary=1,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")
    

# Defaults(name="Ensemble_fix", 
#         GPU=GPU.v32, 
#         batch_size=12, 
#         eval_fraction=50,
#         null_chance_boundary=1,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")

# for i in range(1, 6):
#     Defaults(name=f"Ensemble_fix{i}", 
#             GPU=GPU.v32, 
#             batch_size=12, 
#             eval_fraction=50,
#             null_chance_boundary=1,
#             model_type="t5",
#             t5_model_name="t5-base",
#             data_name="mimic_iv/train/data.json",  
#             labels_name="mimic_iv/train/label.json",
#             answer_name="mimic_iv/train/answer.json",
#             prediction_name="mimic_iv/valid/data.json")

# for i in range(6, 8):
#     Defaults(name=f"Ensemble_fix{i}", 
#             GPU=GPU.a40, 
#             batch_size=12, 
#             eval_fraction=50,
#             null_chance_boundary=1,
#             model_type="t5",
#             t5_model_name="t5-base",
#             data_name="mimic_iv/train/data.json",  
#             labels_name="mimic_iv/train/label.json",
#             answer_name="mimic_iv/train/answer.json",
#             prediction_name="mimic_iv/valid/data.json")
    
# for i in range(8, 10):
#     Defaults(name=f"Ensemble_fix{i}", 
#             GPU=GPU.a80, 
#             batch_size=12, 
#             eval_fraction=50,
#             null_chance_boundary=1,
#             model_type="t5",
#             t5_model_name="t5-base",
#             data_name="mimic_iv/train/data.json",  
#             labels_name="mimic_iv/train/label.json",
#             answer_name="mimic_iv/train/answer.json",
#             prediction_name="mimic_iv/valid/data.json")


# Defaults(name=f"low_lr", 
#         GPU=GPU.v32, 
#         batch_size=12, 
#         eval_fraction=50,
#         null_chance_boundary=1,
#         make_predictions_after=25,
#         lr=0.0001,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")

# Defaults(name=f"very_low_lr", 
#         GPU=GPU.v32, 
#         batch_size=12, 
#         eval_fraction=50,
#         null_chance_boundary=1,
#         make_predictions_after=25,
#         lr=0.00001,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")


# Defaults(name=f"added_scheduler", 
#         GPU=GPU.v32, 
#         batch_size=12, 
#         eval_fraction=50,
#         null_chance_boundary=1,
#         make_predictions_after=25,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")

# Defaults(name=f"added_scheduler_large", 
#         GPU=GPU.a80, 
#         batch_size=12, 
#         eval_fraction=25,
#         null_chance_boundary=1,
#         make_predictions_after=5,
#         model_type="t5",
#         t5_model_name="t5-large",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json")

# for i in range(3, 6):
#         Defaults(name=f"added_scheduler{i}", 
#                 GPU=GPU.v32, 
#                 batch_size=12, 
#                 eval_fraction=50,
#                 null_chance_boundary=1,
#                 make_predictions_after=25,
#                 model_type="t5",
#                 t5_model_name="t5-base",
#                 data_name="mimic_iv/train/data.json",  
#                 labels_name="mimic_iv/train/label.json",
#                 answer_name="mimic_iv/train/answer.json",
#                 prediction_name="mimic_iv/valid/data.json")
        
# for i in range(2):
#         Defaults(name=f"added_scheduler_no_extra{i}", 
#                 GPU=GPU.a80, 
#                 batch_size=12, 
#                 eval_fraction=50,
#                 null_chance_boundary=1,
#                 make_predictions_after=25,
#                 model_type="t5",
#                 t5_model_name="t5-base",
#                 data_name="mimic_iv/train/data.json",  
#                 labels_name="mimic_iv/train/label.json",
#                 answer_name="mimic_iv/train/answer.json",
#                 prediction_name="mimic_iv/valid/data.json",
#                 append_scheme_info=False,
#                 give_extra_info=False)

# for i in range(6):
#         Defaults(name=f"final_fix{i}", 
#                 GPU=GPU.v32, 
#                 batch_size=12, 
#                 eval_fraction=100,
#                 null_chance_boundary=1,
#                 make_predictions_after=25,
#                 model_type="t5",
#                 t5_model_name="t5-base",
#                 data_name="mimic_iv/train/data.json",  
#                 labels_name="mimic_iv/train/label.json",
#                 answer_name="mimic_iv/train/answer.json",
#                 prediction_name="mimic_iv/valid/data.json",
#                 prediction_name2 = "mimic_iv/test/data.json")

# Defaults(name=f"final6", 
#         GPU=GPU.a80, 
#         batch_size=12, 
#         eval_fraction=100,
#         null_chance_boundary=1,
#         make_predictions_after=25,
#         model_type="t5",
#         t5_model_name="t5-base",
#         data_name="mimic_iv/train/data.json",  
#         labels_name="mimic_iv/train/label.json",
#         answer_name="mimic_iv/train/answer.json",
#         prediction_name="mimic_iv/valid/data.json",
#         prediction_name2 = "mimic_iv/test/data.json")

# for i in range(6):
#         Defaults(name=f"final_fix_fix{i}", 
#                 GPU=GPU.v32, 
#                 batch_size=12, 
#                 eval_fraction=50,
#                 null_chance_boundary=1,
#                 make_predictions_after=25,
#                 model_type="t5",
#                 t5_model_name="t5-base",
#                 data_name="mimic_iv/train/data.json",  
#                 labels_name="mimic_iv/train/label.json",
#                 answer_name="mimic_iv/train/answer.json",
#                 prediction_name="mimic_iv/valid/data.json",
#                 prediction_name2 = "mimic_iv/test/data.json")

data_name = "dataset/mimic_iv_cxr/train/train_data.json"
prediction_name = "dataset/mimic_iv_cxr/valid/valid_data.json"
test_name = "dataset/mimic_iv_cxr/test/test_data.json"


for i in range(6):
        Defaults(name=f"predictions_LLM_{i}", 
                GPU=GPU.v32, 
                batch_size=12, 
                make_predictions_after=1,
                model_type="t5",
                t5_model_name="t5-base",
                data_name=data_name,  
                prediction_name=prediction_name,
                test_name=test_name,
                lr=0.001)