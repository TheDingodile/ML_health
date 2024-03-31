#!/bin/sh
mkdir -p outputs/null_safety000001/Markdown
bsub -o "outputs/null_safety000001/Markdown/null_safety000001_0.md" -J "null_safety000001_0" -env MYARGS="-name null_safety000001-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -null_chance_boundary 1e-05 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/null_safety00001/Markdown
bsub -o "outputs/null_safety00001/Markdown/null_safety00001_0.md" -J "null_safety00001_0" -env MYARGS="-name null_safety00001-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -null_chance_boundary 0.0001 -ID 0" < submit_gpu_a80.sh
