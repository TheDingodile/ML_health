from src.evaluator import Evaluator
import json
import time


def assemble_model():
    evaluator = Evaluator()
    out_evals = ["added_scheduler", "added_scheduler0", "added_scheduler1", "added_scheduler2"]


    datas = [json.load(open(f"predictions/{out_eval}-0/out_eval.json")) for out_eval in out_evals]
    pred_dict = {out["id"]: [] for out in datas[0]}
    for data in datas:
        for out in data:
            pred_dict[out["id"]].append(out["pred"])

    counts = 0
    for pred in pred_dict:
        if len(set(pred_dict[pred])) == 1:
            pred_dict[pred] = pred_dict[pred][0]
        else:
            counts += 1
            pred_dict[pred] = "null"
    print(counts/pred_dict.__len__() * 100)

    evaluator.save_predictions("assemble_model", pred_dict)

def entropy_model():
    evaluator = Evaluator()
    out_eval = "save_predictions"
    data = json.load(open(f"predictions/{out_eval}-0/out_eval.json"))
    # pred_dict = {out["id"]: (out["pred"], out["entropy"]) for out in data}
    pred_dict = {out["id"]: (out["question"], max(out["entropy"]), out["pred"]) for out in data}
    counts = 0
    for pred in pred_dict:
        if pred_dict[pred][1] > 0.001:
            pred_dict[pred] = "null"
            counts += 1
        else:
            pred_dict[pred] = pred_dict[pred][2]
    print(counts/pred_dict.__len__() * 100)



    evaluator.save_predictions("entropy_model", pred_dict)


assemble_model()
