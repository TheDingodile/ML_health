wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.17.0
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240603_101245-pmj18p0q
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run final_LLM_0-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/pmj18p0q
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
| <c>name</c>       | <d>str</d>        | <j>"final_LLM_0-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"dataset/mimic_iv_cxr/train/train_data.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"dataset/mimic_iv_cxr/valid/valid_data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>12</f>         |
| <c>make_predictions_after</c>| <d>int</d>        | <f>1</f>          |
| <c>lr</c>         | <d>float</d>      | <f>0.0005</f>     |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |
| <c>append_scheme_info</c>| <d>bool</d>       | <e>True</e>       |
| <c>give_extra_info</c>| <d>bool</d>       | <e>True</e>       |

# Output

```
Aborted!
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 90, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 76, in run
    out_eval = model.model.generate(model.tokenizer, valid_loader)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/T5_model.py", line 41, in generate
    generation_output = self.network.generate(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/generation/utils.py", line 1758, in generate
    result = self._sample(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/generation/utils.py", line 2397, in _sample
    outputs = self(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 1740, in forward
    decoder_outputs = self.decoder(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 1107, in forward
    layer_outputs = layer_module(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 687, in forward
    self_attention_outputs = self.layer[0](
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 594, in forward
    attention_output = self.SelfAttention(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 525, in forward
    query_states, key_states.transpose(3, 2)
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21903222: <final_LLM_0_0> in cluster <dcc> Exited

Job <final_LLM_0_0> was submitted from host <n-62-27-23> by user <s183914> in cluster <dcc> at Mon Jun  3 10:03:53 2024
Job was executed on host(s) <4*n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Jun  3 10:12:34 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Jun  3 10:12:34 2024
Terminated at Mon Jun  3 16:43:10 2024
Results reported at Mon Jun  3 16:43:10 2024

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

    CPU time :                                   23559.00 sec.
    Max Memory :                                 2131 MB
    Average Memory :                             1929.17 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63405.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                35
    Run time :                                   23437 sec.
    Turnaround time :                            23957 sec.

The output (if any) is above this job summary.

