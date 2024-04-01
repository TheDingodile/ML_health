#!/bin/sh
mkdir -p outputs/Add_information/Markdown
bsub -o "outputs/Add_information/Markdown/Add_information_0.md" -J "Add_information_0" -env MYARGS="-name Add_information-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -model_type t5 -t5_model_name t5-base -batch_size 16 -eval_fraction 25 -null_chance_boundary 1.0 -make_predictions_after 3 -lr 0.001 -max_length_source 1024 -max_length_target 512 -ID 0" < submit_gpu_a80.sh
