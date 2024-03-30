Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 2, in <module>
    from dtu import Parameters, dtu, GPU
ModuleNotFoundError: No module named 'dtu'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 20985830: <test_0> in cluster <dcc> Exited

Job <test_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Sat Mar 30 10:15:45 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 30 10:16:32 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sat Mar 30 10:16:32 2024
Terminated at Sat Mar 30 10:16:34 2024
Results reported at Sat Mar 30 10:16:34 2024

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

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   76 sec.
    Turnaround time :                            49 sec.

The output (if any) is above this job summary.


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
| <c>name</c>       | <d>str</d>        | <j>"test-0"</j>   |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"sample_data/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"sample_data/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"sample_data/train/answer.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>batch_size</c> | <d>int</d>        | <f>64</f>         |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 62, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 30, in run
    wandb.init(project="ML_healthcare", name=name, config={"batch_size": batch_size, "isServer": isServer, "device": str(device)})
UnboundLocalError: local variable 'device' referenced before assignment

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 20985972: <test_0> in cluster <dcc> Exited

Job <test_0> was submitted from host <n-62-30-8> by user <s183914> in cluster <dcc> at Sat Mar 30 10:19:07 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 30 10:19:09 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sat Mar 30 10:19:09 2024
Terminated at Sat Mar 30 10:19:19 2024
Results reported at Sat Mar 30 10:19:19 2024

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

    CPU time :                                   2.92 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   27 sec.
    Turnaround time :                            12 sec.

The output (if any) is above this job summary.

