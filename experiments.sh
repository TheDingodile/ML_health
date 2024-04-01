#!/bin/sh
mkdir -p outputs/low_lr/Markdown
bsub -o "outputs/low_lr/Markdown/low_lr_0.md" -J "low_lr_0" -env MYARGS="-name low_lr-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 25 -lr 0.0001 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/very_low_lr/Markdown
bsub -o "outputs/very_low_lr/Markdown/very_low_lr_0.md" -J "very_low_lr_0" -env MYARGS="-name very_low_lr-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 50 -null_chance_boundary 1.0 -make_predictions_after 25 -lr 1e-05 -max_length_source 512 -max_length_target 512 -ID 0" < submit_gpu_v32.sh
