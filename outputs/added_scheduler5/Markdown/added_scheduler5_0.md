wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240401_212400-xx3mjheq
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run added_scheduler5-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/xx3mjheq/workspace
You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
/bin/rm: write error: No space left on device

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21087720: <added_scheduler5_0> in cluster <dcc> Exited

Job <added_scheduler5_0> was submitted from host <n-62-30-1> by user <s183914> in cluster <dcc> at Mon Apr  1 17:11:56 2024
Job was executed on host(s) <4*n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  1 21:23:53 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Apr  1 21:23:53 2024
Terminated at Mon Apr  1 21:54:53 2024
Results reported at Mon Apr  1 21:54:53 2024

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

    CPU time :                                   1863.00 sec.
    Max Memory :                                 1259 MB
    Average Memory :                             1242.92 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64277.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   1859 sec.
    Turnaround time :                            16977 sec.

The output (if any) is above this job summary.

