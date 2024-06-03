#!/bin/sh
mkdir -p outputs/project2LLM/Markdown
bsub -o "outputs/project2LLM/Markdown/project2LLM_0.md" -J "project2LLM_0" -env MYARGS="-name project2LLM-0 -time 82800 -data_name dataset/mimic_iv_cxr/train/train_data.json -prediction_name dataset/mimic_iv_cxr/valid/valid_data.json -model_type t5 -t5_model_name t5-base -batch_size 12 -make_predictions_after 2 -lr 0.001 -max_length_source 512 -max_length_target 512 -append_scheme_info True -give_extra_info True -ID 0" < submit_gpu_v32.sh
