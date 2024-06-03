wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240603_091950-ul8z2yw2
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run project2LLM-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/ul8z2yw2
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
| <c>name</c>       | <d>str</d>        | <j>"project2LLM-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"mimic_iv/valid/data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>12</f>         |
| <c>make_predictions_after</c>| <d>int</d>        | <f>2</f>          |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |
| <c>append_scheme_info</c>| <d>bool</d>       | <e>True</e>       |
| <c>give_extra_info</c>| <d>bool</d>       | <e>True</e>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 83, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 47, in run
    data = {d["id"]: d["question"] for d in raw_data}
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 47, in <dictcomp>
    data = {d["id"]: d["question"] for d in raw_data}
TypeError: string indices must be integers
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.007 MB of 0.010 MB uploadedwandb: - 0.010 MB of 0.010 MB uploadedwandb: 🚀 View run project2LLM-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/ul8z2yw2
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240603_091950-ul8z2yw2/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21903136: <project2LLM_0> in cluster <dcc> Exited

Job <project2LLM_0> was submitted from host <n-62-27-23> by user <s183914> in cluster <dcc> at Mon Jun  3 09:19:41 2024
Job was executed on host(s) <4*n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Jun  3 09:19:41 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Jun  3 09:19:41 2024
Terminated at Mon Jun  3 09:20:18 2024
Results reported at Mon Jun  3 09:20:18 2024

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

    CPU time :                                   6.84 sec.
    Max Memory :                                 379 MB
    Average Memory :                             379.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65157.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                33
    Run time :                                   37 sec.
    Turnaround time :                            37 sec.

The output (if any) is above this job summary.

wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240603_092349-fp9q61sh
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run project2LLM-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/fp9q61sh
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
| <c>name</c>       | <d>str</d>        | <j>"project2LLM-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"dataset/mimic_iv_cxr/train/train_data.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"dataset/mimic_iv_cxr/valid/valid_data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>12</f>         |
| <c>make_predictions_after</c>| <d>int</d>        | <f>2</f>          |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |
| <c>append_scheme_info</c>| <d>bool</d>       | <e>True</e>       |
| <c>give_extra_info</c>| <d>bool</d>       | <e>True</e>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 83, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 55, in run
    dataset_train = T5Dataset(model.tokenizer, data, labels, is_test=False, append_schema_info=append_scheme_info, tables_file=tables_file, max_source_length=max_length_source, max_target_length=max_length_target, give_extra_info=give_extra_info)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/data/T5dataset.py", line 63, in __init__
    ids.append(sample['id'])
TypeError: 'int' object is not subscriptable
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.007 MB of 0.010 MB uploaded (0.002 MB deduped)wandb: - 0.010 MB of 0.010 MB uploaded (0.002 MB deduped)wandb: 🚀 View run project2LLM-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/fp9q61sh
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240603_092349-fp9q61sh/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21903149: <project2LLM_0> in cluster <dcc> Exited

Job <project2LLM_0> was submitted from host <n-62-27-23> by user <s183914> in cluster <dcc> at Mon Jun  3 09:23:41 2024
Job was executed on host(s) <4*n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Jun  3 09:23:42 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Jun  3 09:23:42 2024
Terminated at Mon Jun  3 09:24:02 2024
Results reported at Mon Jun  3 09:24:02 2024

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

    CPU time :                                   6.56 sec.
    Max Memory :                                 1186 MB
    Average Memory :                             1186.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64350.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                27
    Run time :                                   19 sec.
    Turnaround time :                            21 sec.

The output (if any) is above this job summary.

