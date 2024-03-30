#!/bin/sh
mkdir -p outputs/test_real_data_64/Markdown
bsub -o "outputs/test_real_data_64/Markdown/test_real_data_64_0.md" -J "test_real_data_64_0" -env MYARGS="-name test_real_data_64-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 64 -ID 0" < submit_gpu_v32.sh
