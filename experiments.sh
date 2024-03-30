#!/bin/sh
mkdir -p outputs/tester16b/Markdown
bsub -o "outputs/tester16b/Markdown/tester16b_0.md" -J "tester16b_0" -env MYARGS="-name tester16b-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 16 -ID 0" < submit_gpu_v32.sh
mkdir -p outputs/tester32b/Markdown
bsub -o "outputs/tester32b/Markdown/tester32b_0.md" -J "tester32b_0" -env MYARGS="-name tester32b-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 32 -ID 0" < submit_gpu_a80.sh
