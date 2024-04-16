wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: wandb version 0.16.6 is available!  To upgrade, please run:
wandb:  $ pip install wandb --upgrade
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240415_193928-n3vs8qw6
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run final_fix2-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/n3vs8qw6/workspace
You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.

<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"final_fix2-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"mimic_iv/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"mimic_iv/train/answer.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"mimic_iv/valid/data.json"</j> |
| <c>prediction_name2</c>| <d>str</d>        | <j>"mimic_iv/test/data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>12</f>         |
| <c>eval_fraction</c>| <d>int</d>        | <f>100</f>        |
| <c>null_chance_boundary</c>| <d>float</d>      | <f>1.0</f>        |
| <c>make_predictions_after</c>| <d>int</d>        | <f>25</f>         |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |
| <c>append_scheme_info</c>| <d>bool</d>       | <e>True</e>       |
| <c>give_extra_info</c>| <d>bool</d>       | <e>True</e>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 121, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 109, in run
    out_eval = model.model.generate(model.tokenizer, final_loader)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/T5_model.py", line 34, in generate
    for batch in eval_loader:
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 631, in __next__
    data = self._next_data()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 675, in _next_data
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/utils/data/_utils/fetch.py", line 54, in fetch
    return self.collate_fn(data)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/data/T5dataset.py", line 155, in collate_fn
    target_ids = torch.stack([x["target_ids"] for x in batch]) # BS x SL
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/data/T5dataset.py", line 155, in <listcomp>
    target_ids = torch.stack([x["target_ids"] for x in batch]) # BS x SL
KeyError: 'target_ids'
wandb: - 0.005 MB of 0.010 MB uploadedwandb: \ 0.005 MB of 0.010 MB uploadedwandb: | 0.010 MB of 0.010 MB uploadedwandb: 
wandb: Run history:
wandb:   eval_accuracy0 ▁▇▆▆▇▆▇▅▇█████████████████
wandb:  eval_accuracy10 ▁▆▆▄▆▆▆▆▆█████████████████
wandb:   eval_accuracy5 ▁▆▆▄▆▆▆▆▆█████████████████
wandb:   eval_accuracyN ▁▆▆▃▆▆▆▆▆█████████████████
wandb:  train_accuracy0 ▁▆█▅▇█▇███████████████████
wandb: train_accuracy10 ▁▅█▃▆█▆███████████████████
wandb:  train_accuracy5 ▁▅█▃▆█▆███████████████████
wandb:  train_accuracyN ▁▅█▃▆█▆███████████████████
wandb:       train_loss █▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb:   eval_accuracy0 75.0
wandb:  eval_accuracy10 75.0
wandb:   eval_accuracy5 75.0
wandb:   eval_accuracyN 75.0
wandb:  train_accuracy0 78.84615
wandb: train_accuracy10 78.84615
wandb:  train_accuracy5 78.84615
wandb:  train_accuracyN 78.84615
wandb:       train_loss 0.0001
wandb: 
wandb: 🚀 View run final_fix2-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/n3vs8qw6/workspace
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240415_193928-n3vs8qw6/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21414860: <final_fix2_0> in cluster <dcc> Exited

Job <final_fix2_0> was submitted from host <n-62-27-19> by user <s183914> in cluster <dcc> at Mon Apr 15 15:42:05 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 15 19:38:58 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Apr 15 19:38:58 2024
Terminated at Mon Apr 15 23:10:11 2024
Results reported at Mon Apr 15 23:10:11 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu32gb]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   12503.74 sec.
    Max Memory :                                 1446 MB
    Average Memory :                             1364.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64090.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   12673 sec.
    Turnaround time :                            26886 sec.

The output (if any) is above this job summary.

