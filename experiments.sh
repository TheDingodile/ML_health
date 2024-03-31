#!/bin/sh
mkdir -p outputs/more_buffer/Markdown
bsub -o "outputs/more_buffer/Markdown/more_buffer_0.md" -J "more_buffer_0" -env MYARGS="-name more_buffer-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 8 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 2 -lr 0.001 -max_length_source 1024 -max_length_target 1024 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/more_buffer_a80/Markdown
bsub -o "outputs/more_buffer_a80/Markdown/more_buffer_a80_0.md" -J "more_buffer_a80_0" -env MYARGS="-name more_buffer_a80-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 16 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 2 -lr 0.001 -max_length_source 1024 -max_length_target 1024 -ID 0" < submit_gpu_a80.sh
