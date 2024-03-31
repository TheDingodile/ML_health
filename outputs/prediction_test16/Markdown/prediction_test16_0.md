wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240330_175504-ogu5nf9h
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run prediction_test16-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/ogu5nf9h/workspace
You are using the default legacy behaviour of the <class 'transformers.models.t5.tokenization_t5.T5Tokenizer'>. This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thoroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.

Aborted!
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21005206: <prediction_test16_0> in cluster <dcc> Exited

Job <prediction_test16_0> was submitted from host <n-62-30-4> by user <s183914> in cluster <dcc> at Sat Mar 30 17:44:35 2024
Job was executed on host(s) <4*n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 30 17:54:57 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sat Mar 30 17:54:57 2024
Terminated at Sun Mar 31 08:57:13 2024
Results reported at Sun Mar 31 08:57:13 2024

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

    CPU time :                                   49998.00 sec.
    Max Memory :                                 1228 MB
    Average Memory :                             1204.83 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64308.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   50536 sec.
    Turnaround time :                            51158 sec.

The output (if any) is above this job summary.

