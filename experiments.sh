#!/bin/sh
mkdir -p outputs/save_predictions/Markdown
bsub -o "outputs/save_predictions/Markdown/save_predictions_0.md" -J "save_predictions_0" -env MYARGS="-name save_predictions-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 16 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 2 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/save_predictions2/Markdown
bsub -o "outputs/save_predictions2/Markdown/save_predictions2_0.md" -J "save_predictions2_0" -env MYARGS="-name save_predictions2-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 16 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 2 -ID 0" < submit_gpu_v32.sh
