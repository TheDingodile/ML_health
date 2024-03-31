#!/bin/sh
mkdir -p outputs/null_safety01/Markdown
bsub -o "outputs/null_safety01/Markdown/null_safety01_0.md" -J "null_safety01_0" -env MYARGS="-name null_safety01-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -null_chance_boundary 0.1 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/null_safety001/Markdown
bsub -o "outputs/null_safety001/Markdown/null_safety001_0.md" -J "null_safety001_0" -env MYARGS="-name null_safety001-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -null_chance_boundary 0.01 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/null_safety0001/Markdown
bsub -o "outputs/null_safety0001/Markdown/null_safety0001_0.md" -J "null_safety0001_0" -env MYARGS="-name null_safety0001-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -null_chance_boundary 0.001 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/null_safety025/Markdown
bsub -o "outputs/null_safety025/Markdown/null_safety025_0.md" -J "null_safety025_0" -env MYARGS="-name null_safety025-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -batch_size 16 -eval_fraction 50 -null_chance_boundary 0.25 -ID 0" < submit_gpu_v32.sh
