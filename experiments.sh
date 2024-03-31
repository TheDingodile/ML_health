#!/bin/sh
mkdir -p outputs/LargeTest/Markdown
bsub -o "outputs/LargeTest/Markdown/LargeTest_0.md" -J "LargeTest_0" -env MYARGS="-name LargeTest-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-large -batch_size 8 -eval_fraction 50 -null_chance_boundary 0.1 -make_predictions_after 2 -ID 0" < submit_gpu_v32.sh
