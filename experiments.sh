#!/bin/sh
mkdir -p outputs/tester16/Markdown
bsub -o "outputs/tester16/Markdown/tester16_0.md" -J "tester16_0" -env MYARGS="-name tester16-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 16 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/tester32/Markdown
bsub -o "outputs/tester32/Markdown/tester32_0.md" -J "tester32_0" -env MYARGS="-name tester32-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 32 -ID 0" < submit_gpu_a80.sh
