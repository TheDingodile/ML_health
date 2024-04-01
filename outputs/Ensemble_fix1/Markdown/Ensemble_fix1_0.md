wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240401_082522-rkz984iy
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Ensemble_fix1-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/rkz984iy/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"Ensemble_fix1-0"</j> |
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
| <c>make_predictions_after</c>| <d>int</d>        | <f>5</f>          |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |

# Output

```
```
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.004 MB uploadedwandb: | 0.004 MB of 0.004 MB uploadedwandb: / 0.004 MB of 0.007 MB uploadedwandb: - 0.008 MB of 0.008 MB uploadedwandb: 
wandb: Run history:
wandb:   eval_accuracy0 ▁█▇▂▆▆
wandb:  eval_accuracy10 ▅█▃▇▁▁
wandb:   eval_accuracy5 ▃█▃▆▁▁
wandb:   eval_accuracyN ▆█▃█▁▁
wandb:  train_accuracy0 ▁▇▆▄▂█
wandb: train_accuracy10 ▁▇▄▃▂█
wandb:  train_accuracy5 ▁▇▄▃▂█
wandb:  train_accuracyN ▁▇▄▂▂█
wandb:       train_loss █▅▃▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb:   eval_accuracy0 73.78641
wandb:  eval_accuracy10 44.66019
wandb:   eval_accuracy5 59.2233
wandb:   eval_accuracyN -226.21359
wandb:  train_accuracy0 75.72816
wandb: train_accuracy10 66.01942
wandb:  train_accuracy5 70.87379
wandb:  train_accuracyN -24.27184
wandb:       train_loss 0.00057
wandb: 
wandb: 🚀 View run Ensemble_fix1-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/rkz984iy/workspace
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240401_082522-rkz984iy/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21070572: <Ensemble_fix1_0> in cluster <dcc> Done

Job <Ensemble_fix1_0> was submitted from host <n-62-30-1> by user <s183914> in cluster <dcc> at Mon Apr  1 07:49:37 2024
Job was executed on host(s) <4*n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  1 08:25:15 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Apr  1 08:25:15 2024
Terminated at Mon Apr  1 09:29:39 2024
Results reported at Mon Apr  1 09:29:39 2024

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

    CPU time :                                   3836.20 sec.
    Max Memory :                                 1258 MB
    Average Memory :                             1218.47 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64278.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   3863 sec.
    Turnaround time :                            6002 sec.

The output (if any) is above this job summary.

