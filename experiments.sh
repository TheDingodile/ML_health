#!/bin/sh
mkdir -p outputs/prediction_test16/Markdown
bsub -o "outputs/prediction_test16/Markdown/prediction_test16_0.md" -J "prediction_test16_0" -env MYARGS="-name prediction_test16-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/prediction_test32/Markdown
bsub -o "outputs/prediction_test32/Markdown/prediction_test32_0.md" -J "prediction_test32_0" -env MYARGS="-name prediction_test32-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 32 -eval_fraction 50 -ID 0" < submit_gpu_a80.sh
