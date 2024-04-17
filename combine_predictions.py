import json

# Define a list of JSON file paths
file_paths = ['best_predictions/predictions.json', 'best_predictions/TalkFile_test_prediction_gemini.json']
datas = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        data = json.load(file)
        datas.append(data)
pred_dict = {out: [] for out in datas[0]}
# print(pred_dict)
for data in datas:
    for out in data:
        pred_dict[out].append(data[out])


counts = 0
for pred in pred_dict:
    if len(set(pred_dict[pred])) == 1:
        pred_dict[pred] = pred_dict[pred][0]
    else:
        counts += 1
        pred_dict[pred] = "null"
print(counts/pred_dict.__len__() * 100)

# save as json file

with open('best_predictions/combined_predictions.json', 'w') as file:
    json.dump(pred_dict, file)

# print(pred_dict)