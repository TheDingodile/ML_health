wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240331_125733-gc8w7et5
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run save_predictions3-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/gc8w7et5/workspace
You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.

Aborted!
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21037358: <save_predictions3_0> in cluster <dcc> Exited

Job <save_predictions3_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Sun Mar 31 12:57:23 2024
Job was executed on host(s) <4*n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 31 12:57:24 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sun Mar 31 12:57:24 2024
Terminated at Mon Apr  1 06:31:53 2024
Results reported at Mon Apr  1 06:31:53 2024

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

TERM_OWNER: job killed by owner.
Exited with exit code 143.

Resource usage summary:

    CPU time :                                   61802.00 sec.
    Max Memory :                                 1272 MB
    Average Memory :                             1252.03 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64264.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   63364 sec.
    Turnaround time :                            63270 sec.

The output (if any) is above this job summary.

