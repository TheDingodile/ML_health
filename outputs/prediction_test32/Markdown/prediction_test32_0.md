wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240330_182425-we0h9z4o
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run prediction_test32-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/we0h9z4o/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"prediction_test32-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"mimic_iv/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"mimic_iv/train/answer.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"mimic_iv/valid/data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>batch_size</c> | <d>int</d>        | <f>32</f>         |
| <c>eval_fraction</c>| <d>int</d>        | <f>50</f>         |

# Output

```

Aborted!
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/T5_model.py", line 91, in generate
    "prob_null": prob_null[idx].cpu().numpy().tolist(),
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 3825, in decode
    return self._decode(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/tokenization_utils.py", line 1024, in _decode
    sub_texts.append(self.convert_tokens_to_string(current_sub_text))
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/tokenization_t5.py", line 441, in convert_tokens_to_string
    if token in self.all_special_tokens:
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 1352, in all_special_tokens
    all_toks = [str(s) for s in self.all_special_tokens_extended]
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 1336, in all_special_tokens_extended
    for value in self.special_tokens_map_extended.values():
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 1319, in special_tokens_map_extended
    attr_value = getattr(self, "_" + attr)
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 93, in <module>
    evaluator.save_predictions(name, pred_dict)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 75, in run
    else:
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/T5_model.py", line 91, in generate
    "prob_null": prob_null[idx].cpu().numpy().tolist(),
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21005209: <prediction_test32_0> in cluster <dcc> Exited

Job <prediction_test32_0> was submitted from host <n-62-30-4> by user <s183914> in cluster <dcc> at Sat Mar 30 17:44:35 2024
Job was executed on host(s) <4*n-62-18-10>, in queue <gpua100>, as user <s183914> in cluster <dcc> at Sat Mar 30 18:24:12 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sat Mar 30 18:24:12 2024
Terminated at Sun Mar 31 10:29:09 2024
Results reported at Sun Mar 31 10:29:09 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu80gb]"
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

    CPU time :                                   51991.00 sec.
    Max Memory :                                 1234 MB
    Average Memory :                             1197.34 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64302.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   54297 sec.
    Turnaround time :                            56674 sec.

The output (if any) is above this job summary.

