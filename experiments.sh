#!/bin/sh
mkdir -p outputs/tester16c/Markdown
bsub -o "outputs/tester16c/Markdown/tester16c_0.md" -J "tester16c_0" -env MYARGS="-name tester16c-0 -time 82800 -data_name mimic_iv/train/data.json -labels_name mimic_iv/train/label.json -answer_name mimic_iv/train/answer.json -model_type t5 -batch_size 16 -eval_fraction 10 -ID 0" < submit_gpu_v32.sh
