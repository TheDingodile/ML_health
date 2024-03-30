#!/bin/sh
mkdir -p outputs/log_entropy_nulls/Markdown
bsub -o "outputs/log_entropy_nulls/Markdown/log_entropy_nulls_0.md" -J "log_entropy_nulls_0" -env MYARGS="-name log_entropy_nulls-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 16 -eval_fraction 50 -ID 0" < submit_gpu_v32.sh
