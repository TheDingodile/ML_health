#!/bin/sh
mkdir -p outputs/added_scheduler/Markdown
bsub -o "outputs/added_scheduler/Markdown/added_scheduler_0.md" -J "added_scheduler_0" -env MYARGS="-name added_scheduler-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 25 -lr 0.001 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_v32.sh
