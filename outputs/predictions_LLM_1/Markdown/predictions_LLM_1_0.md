wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240603_185155-xp2xd1aa
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run predictions_LLM_1-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/xp2xd1aa
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
| <c>name</c>       | <d>str</d>        | <j>"predictions_LLM_1-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"dataset/mimic_iv_cxr/train/train_data.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"dataset/mimic_iv_cxr/valid/valid_data.json"</j> |
| <c>test_name</c>  | <d>str</d>        | <j>"dataset/mimic_iv_cxr/test/test_data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>12</f>         |
| <c>make_predictions_after</c>| <d>int</d>        | <f>1</f>          |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |
| <c>append_scheme_info</c>| <d>bool</d>       | <e>False</e>      |
| <c>give_extra_info</c>| <d>bool</d>       | <e>False</e>      |

# Output

```
```
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.007 MB uploadedwandb: | 0.007 MB of 0.007 MB uploadedwandb: 
wandb: Run history:
wandb: train_loss █▄▃▃▃▂▂▁▁▁▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: train_loss 0.00135
wandb: 
wandb: 🚀 View run predictions_LLM_1-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/xp2xd1aa
wandb: ⭐️ View project at: https://wandb.ai/kobomao/ML_healthcare
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240603_185155-xp2xd1aa/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21906039: <predictions_LLM_1_0> in cluster <dcc> Done

Job <predictions_LLM_1_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Mon Jun  3 16:45:05 2024
Job was executed on host(s) <4*n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Jun  3 18:51:44 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Jun  3 18:51:44 2024
Terminated at Tue Jun  4 00:35:58 2024
Results reported at Tue Jun  4 00:35:58 2024

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

    CPU time :                                   20739.78 sec.
    Max Memory :                                 1720 MB
    Average Memory :                             1634.76 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63816.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                35
    Run time :                                   20653 sec.
    Turnaround time :                            28253 sec.

The output (if any) is above this job summary.

