#!/bin/sh
mkdir -p outputs/Ensemble_fix6/Markdown
bsub -o "outputs/Ensemble_fix6/Markdown/Ensemble_fix6_0.md" -J "Ensemble_fix6_0" -env MYARGS="-name Ensemble_fix6-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 5 -lr 0.001 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_a40.sh
mkdir -p outputs/Ensemble_fix7/Markdown
bsub -o "outputs/Ensemble_fix7/Markdown/Ensemble_fix7_0.md" -J "Ensemble_fix7_0" -env MYARGS="-name Ensemble_fix7-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 5 -lr 0.001 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_a40.sh
mkdir -p outputs/Ensemble_fix8/Markdown
bsub -o "outputs/Ensemble_fix8/Markdown/Ensemble_fix8_0.md" -J "Ensemble_fix8_0" -env MYARGS="-name Ensemble_fix8-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 5 -lr 0.001 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_a80.sh
mkdir -p outputs/Ensemble_fix9/Markdown
bsub -o "outputs/Ensemble_fix9/Markdown/Ensemble_fix9_0.md" -J "Ensemble_fix9_0" -env MYARGS="-name Ensemble_fix9-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 5 -lr 0.001 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_a80.sh
