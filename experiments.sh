#!/bin/sh
mkdir -p outputs/test/Markdown
bsub -o "outputs/test/Markdown/test_0.md" -J "test_0" -env MYARGS="-name test-0 -time 82800 -data_name sample_data/train/data.json -labels_name sample_data/train/label.json -answer_name sample_data/train/answer.json -model_type t5 -batch_size 64 -ID 0" < submit_gpu_v32.sh
