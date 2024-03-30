#!/bin/sh
mkdir -p outputs/test_real_data/Markdown
bsub -o "outputs/test_real_data/Markdown/test_real_data_0.md" -J "test_real_data_0" -env MYARGS="-name test_real_data-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 128 -ID 0" < submit_gpu_v32.sh
