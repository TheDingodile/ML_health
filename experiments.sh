#!/bin/sh
mkdir -p outputs/null_safety01Large/Markdown
bsub -o "outputs/null_safety01Large/Markdown/null_safety01Large_0.md" -J "null_safety01Large_0" -env MYARGS="-name null_safety01Large-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-large -batch_size 16 -eval_fraction 50 -null_chance_boundary 0.1 -make_predictions_after 2 -ID 0" < submit_gpu_a80.sh
