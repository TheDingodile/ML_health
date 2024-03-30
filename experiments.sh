#!/bin/sh
mkdir -p outputs/prediction_test16_a40/Markdown
bsub -o "outputs/prediction_test16_a40/Markdown/prediction_test16_a40_0.md" -J "prediction_test16_a40_0" -env MYARGS="-name prediction_test16_a40-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -ID 0" < submit_gpu_a40.sh
