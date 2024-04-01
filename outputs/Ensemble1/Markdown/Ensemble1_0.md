wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240401_072751-42ourlr0
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Ensemble1-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/42ourlr0/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"Ensemble1-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>82800</f>      |
| <c>data_name</c>  | <d>str</d>        | <j>"mimic_iv/train/data.json"</j> |
| <c>labels_name</c>| <d>str</d>        | <j>"mimic_iv/train/label.json"</j> |
| <c>answer_name</c>| <d>str</d>        | <j>"mimic_iv/train/answer.json"</j> |
| <c>prediction_name</c>| <d>str</d>        | <j>"mimic_iv/valid/data.json"</j> |
| <c>model_type</c> | <d>str</d>        | <j>"t5"</j>       |
| <c>t5_model_name</c>| <d>str</d>        | <j>"t5-base"</j>  |
| <c>batch_size</c> | <d>int</d>        | <f>16</f>         |
| <c>eval_fraction</c>| <d>int</d>        | <f>25</f>         |
| <c>null_chance_boundary</c>| <d>float</d>      | <f>1.0</f>        |
| <c>make_predictions_after</c>| <d>int</d>        | <f>3</f>          |
| <c>lr</c>         | <d>float</d>      | <f>0.001</f>      |
| <c>max_length_source</c>| <d>int</d>        | <f>512</f>        |
| <c>max_length_target</c>| <d>int</d>        | <f>512</f>        |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 110, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/main.py", line 66, in run
    train_loss = model.trainer(batch)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/Model.py", line 31, in trainer
    loss = self.model.trainer(input_ids, attention_mask, labels, self.tokenizer, self.optimizer)
  File "/zhome/ea/9/137501/Desktop/ML_health/ML_health/src/models/T5_model.py", line 18, in trainer
    loss.backward()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/_tensor.py", line 522, in backward
    torch.autograd.backward(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/torch/autograd/__init__.py", line 266, in backward
    Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 816.00 MiB. GPU 0 has a total capacity of 31.73 GiB of which 192.19 MiB is free. Including non-PyTorch memory, this process has 31.54 GiB memory in use. Of the allocated memory 28.49 GiB is allocated by PyTorch, and 2.68 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.010 MB uploadedwandb: | 0.010 MB of 0.010 MB uploadedwandb: 
wandb: Run history:
wandb: train_loss ▁
wandb: 
wandb: Run summary:
wandb: train_loss 11.85122
wandb: 
wandb: 🚀 View run Ensemble1-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/42ourlr0/workspace
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240401_072751-42ourlr0/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21070543: <Ensemble1_0> in cluster <dcc> Exited

Job <Ensemble1_0> was submitted from host <n-62-30-1> by user <s183914> in cluster <dcc> at Mon Apr  1 06:42:35 2024
Job was executed on host(s) <4*n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  1 07:27:47 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Apr  1 07:27:47 2024
Terminated at Mon Apr  1 07:28:18 2024
Results reported at Mon Apr  1 07:28:18 2024

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

    CPU time :                                   21.83 sec.
    Max Memory :                                 1163 MB
    Average Memory :                             1163.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64373.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                35
    Run time :                                   31 sec.
    Turnaround time :                            2743 sec.

The output (if any) is above this job summary.

