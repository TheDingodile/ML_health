#!/bin/sh
mkdir -p outputs/test_real_data_16/Markdown
bsub -o "outputs/test_real_data_16/Markdown/test_real_data_16_0.md" -J "test_real_data_16_0" -env MYARGS="-name test_real_data_16-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 16 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/test_real_data_32/Markdown
bsub -o "outputs/test_real_data_32/Markdown/test_real_data_32_0.md" -J "test_real_data_32_0" -env MYARGS="-name test_real_data_32-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 32 -ID 0" < submit_gpu_v32.sh
