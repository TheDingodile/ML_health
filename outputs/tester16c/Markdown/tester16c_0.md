wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240330_152917-fqkrwejf
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run tester16c-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/fqkrwejf/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"tester16c-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"mimic_iv/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"mimic_iv/train/answer.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>batch_size</c> | <d>int</d>        | <f>16</f>         |
| <c>eval_fraction</c>| <d>int</d>        | <f>10</f>         |

# Output

```
Aborted!
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 82, in <module>
    scores = evaluator.evaluate(real_dict, pred_dict, name)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 69, in run
    ave_entropy_non_null_first_token = torch.mean(torch.tensor([v["entropy"][0] for v in out_eval if v["real"] != "null"]))
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/T5_model.py", line 38, in generate
    generation_output = self.network.generate(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/generation/utils.py", line 1527, in generate
    result = self._greedy_search(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/generation/utils.py", line 2411, in _greedy_search
    outputs = self(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 1748, in forward
    decoder_outputs = self.decoder(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 1115, in forward
    layer_outputs = layer_module(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 695, in forward
    self_attention_outputs = self.layer[0](
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 602, in forward
    attention_output = self.SelfAttention(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 527, in forward
    value_states = project(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/transformers/models/t5/modeling_t5.py", line 498, in project
    hidden_states = shape(proj_layer(hidden_states))
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/nn/modules/linear.py", line 116, in forward
    return F.linear(input, self.weight, self.bias)
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 20999336: <tester16c_0> in cluster <dcc> Exited

Job <tester16c_0> was submitted from host <n-62-27-23> by user <s183914> in cluster <dcc> at Sat Mar 30 15:29:06 2024
Job was executed on host(s) <4*n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 30 15:29:07 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Sat Mar 30 15:29:07 2024
Terminated at Sat Mar 30 17:02:22 2024
Results reported at Sat Mar 30 17:02:22 2024

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

    CPU time :                                   5343.00 sec.
    Max Memory :                                 1243 MB
    Average Memory :                             1140.71 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64293.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   5677 sec.
    Turnaround time :                            5596 sec.

The output (if any) is above this job summary.

