wandb: Currently logged in as: kobomao. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.5
wandb: Run data is saved locally in /zhome/ea/9/137501/Desktop/ML_health/ML_health/wandb/run-20240401_094107-rkfkz8j8
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Ensemble_fix5-0
wandb: ⭐️ View project at https://wandb.ai/kobomao/ML_healthcare
wandb: 🚀 View run at https://wandb.ai/kobomao/ML_healthcare/runs/rkfkz8j8/workspace
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
| <c>name</c>       | <d>str</d>        | <j>"Ensemble_fix5-0"</j> |
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
wandb: - 0.004 MB of 0.004 MB uploadedwandb: \ 0.004 MB of 0.008 MB uploadedwandb: | 0.004 MB of 0.008 MB uploadedwandb: / 0.008 MB of 0.008 MB uploadedwandb: 
wandb: Run history:
wandb:   eval_accuracy0 ▁▅▇▅█▆
wandb:  eval_accuracy10 ▁▄▅▅█▅
wandb:   eval_accuracy5 ▁▄▆▅█▅
wandb:   eval_accuracyN ▁▄▅▅█▅
wandb:  train_accuracy0 ▁▅█▇█▇
wandb: train_accuracy10 ▁██▆█▅
wandb:  train_accuracy5 ▁▇█▆█▅
wandb:  train_accuracyN ▁██▆█▅
wandb:       train_loss █▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb:   eval_accuracy0 73.78641
wandb:  eval_accuracy10 54.36893
wandb:   eval_accuracy5 64.07767
wandb:   eval_accuracyN -126.21359
wandb:  train_accuracy0 72.81553
wandb: train_accuracy10 33.98058
wandb:  train_accuracy5 53.39806
wandb:  train_accuracyN -327.18447
wandb:       train_loss 0.00078
wandb: 
wandb: 🚀 View run Ensemble_fix5-0 at: https://wandb.ai/kobomao/ML_healthcare/runs/rkfkz8j8/workspace
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20240401_094107-rkfkz8j8/logs
Exception in thread IntMsgThr:
Traceback (most recent call last):
  File "/appl/python/3.10.7/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/appl/python/3.10.7/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_run.py", line 300, in check_internal_messages
    self._loop_check_status(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_run.py", line 224, in _loop_check_status
    local_handle = request()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface.py", line 844, in deliver_internal_messages
Exception in thread NetStatThr:
Traceback (most recent call last):
  File "/appl/python/3.10.7/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    return self._deliver_internal_messages(internal_message)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface_shared.py", line 516, in _deliver_internal_messages
    self.run()
  File "/appl/python/3.10.7/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_run.py", line 268, in check_network_status
    return self._deliver_record(record)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface_shared.py", line 459, in _deliver_record
    self._loop_check_status(
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/wandb_run.py", line 224, in _loop_check_status
    handle = mailbox._deliver_record(record, interface=self)
    local_handle = request()
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/mailbox.py", line 455, in _deliver_record
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface.py", line 836, in deliver_network_status
    return self._deliver_network_status(status)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface_shared.py", line 510, in _deliver_network_status
    interface._publish(record)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface_sock.py", line 51, in _publish
    return self._deliver_record(record)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface_shared.py", line 459, in _deliver_record
    handle = mailbox._deliver_record(record, interface=self)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/mailbox.py", line 455, in _deliver_record
    self._sock_client.send_record_publish(record)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 221, in send_record_publish
    interface._publish(record)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/interface/interface_sock.py", line 51, in _publish
    self.send_server_request(server_req)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 155, in send_server_request
    self._sock_client.send_record_publish(record)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 221, in send_record_publish
    self._send_message(msg)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 152, in _send_message
    self.send_server_request(server_req)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 155, in send_server_request
    self._sendall_with_error_handle(header + data)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 130, in _sendall_with_error_handle
    self._send_message(msg)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 152, in _send_message
    sent = self._sock.send(data)
BrokenPipeError: [Errno 32] Broken pipe
    self._sendall_with_error_handle(header + data)
  File "/zhome/ea/9/137501/Desktop/ML_health/project-env/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 130, in _sendall_with_error_handle
    sent = self._sock.send(data)
BrokenPipeError: [Errno 32] Broken pipe

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21070576: <Ensemble_fix5_0> in cluster <dcc> Done

Job <Ensemble_fix5_0> was submitted from host <n-62-30-1> by user <s183914> in cluster <dcc> at Mon Apr  1 07:49:38 2024
Job was executed on host(s) <4*n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  1 09:41:02 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_health/ML_health> was used as the working directory.
Started at Mon Apr  1 09:41:02 2024
Terminated at Mon Apr  1 10:44:40 2024
Results reported at Mon Apr  1 10:44:40 2024

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

    CPU time :                                   3797.11 sec.
    Max Memory :                                 1398 MB
    Average Memory :                             1313.32 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               64138.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                36
    Run time :                                   3817 sec.
    Turnaround time :                            10502 sec.

The output (if any) is above this job summary.

