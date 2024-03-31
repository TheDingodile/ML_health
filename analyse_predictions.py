from src.evaluator import Evaluator
import json
import time


def assemble_model():
    evaluator = Evaluator()
    out_evals = ["save_predictions", "save_predictions2", "save_predictions3"]


    datas = [json.load(open(f"predictions/{out_eval}-0/out_eval.json")) for out_eval in out_evals]
    pred_dict = {out["id"]: [] for out in datas[0]}
    for data in datas:
        for out in data:
            pred_dict[out["id"]].append(out["pred"])

    agrees = 0
    disagrees = 0
    for pred in pred_dict:
        if len(set(pred_dict[pred])) == 1:
            pred_dict[pred] = pred_dict[pred][0]
            agrees += 1
        else:
            pred_dict[pred] = "null"
            disagrees += 1
    print(agrees, disagrees)

    evaluator.save_predictions("assemble_model", pred_dict)

def entropy_model():
    evaluator = Evaluator()
    out_eval = "save_predictions"
    data = json.load(open(f"predictions/{out_eval}-0/out_eval.json"))
    # pred_dict = {out["id"]: (out["pred"], out["entropy"]) for out in data}
    pred_dict = {out["id"]: out["question"] for out in data}
    counts = 0
    for pred in pred_dict:
        print(pred_dict[pred])
        time.sleep(10)
        if pred_dict[pred][-1] == 0:
            # pred_dict[pred] = pred_dict[pred][:-1]
            counts += 1
    print(counts)


entropy_model()
