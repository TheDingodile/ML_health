#!/bin/sh
mkdir -p outputs/final6/Markdown
bsub -o "outputs/final6/Markdown/final6_0.md" -J "final6_0" -env MYARGS="-name final6-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -prediction_name mimic_iv/valid/data.json -prediction_name2 sample_data/test/data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -eval_fraction 100 -null_chance_boundary 1.0 -make_predictions_after 25 -lr 0.001 -max_length_source 512 -max_length_target 512 -append_scheme_info True -give_extra_info True -ID 0" < submit_gpu_a80.sh
