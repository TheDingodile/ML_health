wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240401_210747-frxp7b4q
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run added_scheduler4-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/frxp7b4q/workspace
You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
/bin/rm: write error: No space left on device

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21087719: <added_scheduler4_0> in cluster <dcc> Exited

Job <added_scheduler4_0> was submitted from host <n-62-30-1> by user <s183914> in cluster <dcc> at Mon Apr  1 17:11:55 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  1 21:07:33 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Apr  1 21:07:33 2024
Terminated at Mon Apr  1 21:54:54 2024
Results reported at Mon Apr  1 21:54:54 2024

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

Exited with exit code 120.

Resource usage summary:

    CPU time :                                   2793.00 sec.
    Max Memory :                                 1384 MB
    Average Memory :                             1255.82 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64152.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   2840 sec.
    Turnaround time :                            16979 sec.

The output (if any) is above this job summary.

wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240402_045939-l8d3t64c
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run added_scheduler4-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/l8d3t64c/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"added_scheduler4-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"mimic_iv/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"mimic_iv/train/answer.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"mimic_iv/valid/data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>12</f>         |
| <c>eval_fraction</c>| <d>int</d>        | <f>50</f>         |
| <c>null_chance_boundary</c>| <d>float</d>      | <f>1.0</f>        |
| <c>make_predictions_after</c>| <d>int</d>        | <f>25</f>         |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |
| <c>append_scheme_info</c>| <d>bool</d>       | <e>True</e>       |
| <c>give_extra_info</c>| <d>bool</d>       | <e>True</e>       |

# Output

```
```
wandb: - 0.005 MB of 0.005 MB uploaded
wandb: Run history:
wandb:   eval_accuracy0 ▁▇▆▇█▇▇███████████████████
wandb:  eval_accuracy10 ▁▇▆▇██████████████████████
wandb:   eval_accuracy5 ▁▇▆▇██████████████████████
wandb:   eval_accuracyN ▁▇▆▇██████████████████████
wandb:  train_accuracy0 ▁▅▇█▆█████████████████████
wandb: train_accuracy10 ▁▅▇█▇█████████████████████
wandb:  train_accuracy5 ▁▅▇█▇█████████████████████
wandb:  train_accuracyN ▁▅▇█▇█████████████████████
wandb:       train_loss █▂▂▁▂▂▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb:   eval_accuracy0 76.69903
wandb:  eval_accuracy10 76.69903
wandb:   eval_accuracy5 76.69903
wandb:   eval_accuracyN 76.69903
wandb:  train_accuracy0 76.69903
wandb: train_accuracy10 76.69903
wandb:  train_accuracy5 76.69903
wandb:  train_accuracyN 76.69903
wandb:       train_loss 8e-05
wandb: 
wandb: 🚀 View run added_scheduler4-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/l8d3t64c/workspace
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240402_045939-l8d3t64c/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21113585: <added_scheduler4_0> in cluster <dcc> Done

Job <added_scheduler4_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Tue Apr  2 04:13:07 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr  2 04:59:29 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Tue Apr  2 04:59:29 2024
Terminated at Tue Apr  2 08:53:06 2024
Results reported at Tue Apr  2 08:53:06 2024

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

Successfully completed.

Resource usage summary:

    CPU time :                                   13879.76 sec.
    Max Memory :                                 1315 MB
    Average Memory :                             1274.60 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64221.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   14017 sec.
    Turnaround time :                            16799 sec.

The output (if any) is above this job summary.
