wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240330_144149-dcgrgjsb
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run tester16-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/dcgrgjsb/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"tester16-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"mimic_iv/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"mimic_iv/train/answer.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>batch_size</c> | <d>int</d>        | <f>16</f>         |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 80, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 43, in run
    test_loader = DataLoader(dataset_test, batch_size=batch_size, collate_fn=dataset_test.collate_fn, shuffle=False, tables_file="mimic_iv/tables.json")
TypeError: DataLoader.__init__() got an unexpected keyword argument 'tables_file'
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)

Aborted!
Exception ignored in atexit callback: <function _Manager._atexit_setup.<locals>.<lambda> at 0x7f94415704c0>
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_manager.py", line 156, in <lambda>
    self._atexit_lambda = lambda: self._atexit_teardown()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_manager.py", line 165, in _atexit_teardown
    self._teardown(exit_code)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_manager.py", line 176, in _teardown
    result = self._service.join()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/service/service.py", line 263, in join
    ret = self._internal_proc.wait()
  File "/appl/python/3.10.7/lib/python3.10/subprocess.py", line 1207, in wait
    return self._wait(timeout=timeout)
  File "/appl/python/3.10.7/lib/python3.10/subprocess.py", line 1941, in _wait
    (pid, sts) = self._try_wait(0)
  File "/appl/python/3.10.7/lib/python3.10/subprocess.py", line 1899, in _try_wait
    (pid, sts) = os.waitpid(self.pid, wait_flags)
KeyboardInterrupt: 

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 20997331: <tester16_0> in cluster <dcc> Exited

Job <tester16_0> was submitted from host <n-62-27-23> by user <s183914> in cluster <dcc> at Sat Mar 30 14:41:37 2024
Job was executed on host(s) <4*n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 30 14:41:38 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sat Mar 30 14:41:38 2024
Terminated at Sat Mar 30 15:13:41 2024
Results reported at Sat Mar 30 15:13:41 2024

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
Exited with exit code 1.

Resource usage summary:

    CPU time :                                   18.00 sec.
    Max Memory :                                 1178 MB
    Average Memory :                             974.60 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64358.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                34
    Run time :                                   1951 sec.
    Turnaround time :                            1924 sec.

The output (if any) is above this job summary.

