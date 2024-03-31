#!/bin/sh
mkdir -p outputs/LargeTest_fix/Markdown
bsub -o "outputs/LargeTest_fix/Markdown/LargeTest_fix_0.md" -J "LargeTest_fix_0" -env MYARGS="-name LargeTest_fix-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-large -batch_size 4 -eval_fraction 50 -null_chance_boundary 0.1 -make_predictions_after 2 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/LargeTesta40/Markdown
bsub -o "outputs/LargeTesta40/Markdown/LargeTesta40_0.md" -J "LargeTesta40_0" -env MYARGS="-name LargeTesta40-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-large -batch_size 8 -eval_fraction 50 -null_chance_boundary 0.1 -make_predictions_after 2 -ID 0" < submit_gpu_a40.sh
