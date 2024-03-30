import re
import sqlite3
import json
import os
import time
import numpy as np

class Evaluator():
    def __init__(self):
        self.scores = {}
        self.table_path = 'mimic_iv/mimic_iv.sqlite'

    def save_predictions(self, name, pred_dict):
        pred_dict = {id_: self.post_process_sql(pred_dict[id_]) for id_ in pred_dict}
        pred_result = self.execute_all(pred_dict, tag='pred')

        if not os.path.exists(os.path.join("predictions", name)):
            os.makedirs(os.path.join("predictions", name))
        with open(os.path.join("predictions", name, 'predictions.json'), 'w') as score_file:
            score_file.write(json.dumps(pred_result))

    def evaluate(self, real_dict, pred_dict, name):
        real_dict = {id_: self.post_process_sql(real_dict[id_]) for id_ in real_dict}
        pred_dict = {id_: self.post_process_sql(pred_dict[id_]) for id_ in pred_dict}
        real_result = self.execute_all(real_dict, tag='real')
        pred_result = self.execute_all(pred_dict, tag='pred')
        scores = self.calculate_scores(real_result, pred_result, name)
        return scores

    def calculate_scores(self, real_dict, pred_dict, name):
        scores = self.reliability_score(real_dict, pred_dict)
        accuracy0 = self.penalize(scores, penalty=0)
        accuracy5 = self.penalize(scores, penalty=5)
        accuracy10 = self.penalize(scores, penalty=10)
        accuracyN = self.penalize(scores, penalty=len(scores))

        scores_dict = {
            'accuracy0': accuracy0*100,
            'accuracy5': accuracy5*100,
            'accuracy10': accuracy10*100,
            'accuracyN': accuracyN*100
        }

        self.scores = scores_dict

        return scores_dict


                


    def post_process_sql(self, query):
        __current_time = "2100-12-31 23:59:00"
        __precomputed_dict = {
                            'temperature': (35.5, 38.1),
                            'sao2': (95.0, 100.0),
                            'heart rate': (60.0, 100.0),
                            'respiration': (12.0, 18.0),
                            'systolic bp': (90.0, 120.0),
                            'diastolic bp':(60.0, 90.0),
                            'mean bp': (60.0, 110.0)
                                        }
        query = re.sub('[ ]+', ' ', query.replace('\n', ' ')).strip()
        query = query.replace('> =', '>=').replace('< =', '<=').replace('! =', '!=')

        if "current_time" in query:
            query = query.replace("current_time", f"'{__current_time}'")
        if re.search('[ \n]+([a-zA-Z0-9_]+_lower)', query) and re.search('[ \n]+([a-zA-Z0-9_]+_upper)', query):
            vital_lower_expr = re.findall('[ \n]+([a-zA-Z0-9_]+_lower)', query)[0]
            vital_upper_expr = re.findall('[ \n]+([a-zA-Z0-9_]+_upper)', query)[0]
            vital_name_list = list(set(re.findall('([a-zA-Z0-9_]+)_lower', vital_lower_expr) + re.findall('([a-zA-Z0-9_]+)_upper', vital_upper_expr)))
            if len(vital_name_list)==1:
                processed_vital_name = vital_name_list[0].replace('_', ' ')
                if processed_vital_name in __precomputed_dict:
                    vital_range = __precomputed_dict[processed_vital_name]
                    query = query.replace(vital_lower_expr, f"{vital_range[0]}").replace(vital_upper_expr, f"{vital_range[1]}")

        query = query.replace("%y", "%Y").replace('%j', '%J')

        return query
    
    def execute_sql(self, sql, db_path):
        con = sqlite3.connect(db_path)
        con.text_factory = lambda b: b.decode(errors="ignore")
        cur = con.cursor()
        result = cur.execute(sql).fetchall()
        con.close()
        return result

    def execute_sql_wrapper(self, key, sql, db_path, tag, skip_indicator='null'):
        assert tag in ['real', 'pred']
        if sql != skip_indicator:
            try:
                result = self.execute_sql(sql, db_path)
            except:
                if tag == 'pred':
                    return (key, skip_indicator)
                result = 'error_'+tag
            result = self.process_answer(result)
            return (key, result)
        else:
            return (key, skip_indicator)

    def execute_all(self, dict, tag):
        exec_result = {}
        for key in dict:
            sql = dict[key]
            exec_result[key] = self.execute_sql_wrapper(key, sql, self.table_path, tag)[-1]
        return exec_result
    
    def process_item(self, item):
        try:
            item = round(float(item),3)
        except:
            pass
        return str(item)

    def process_answer(self, ans):
        if type(ans)==str:
            return ans
        else:
            return str(sorted([[self.process_item(c) for c in row] for row in ans])[:100]) # check only up to 100th record

    def reliability_score(self, real_result, pred_result, return_dict=False):

        reliablity_score = []
        reliablity_score_dict = {}
        for key in real_result:
            ans_real = real_result[key]
            ans_pred = pred_result[key]
            exec_acc = (ans_real == ans_pred)

            # x in ANS; g(x)=1; Acc(x)=1
            if ans_real != 'null' and exec_acc == True:
                score = 1
            # x in ANS; g(x)=0; Acc(x)={0,1}
            elif ans_real != 'null' and ans_pred == 'null':
                score = 0
            # x in ANS; g(x)=1; Acc(x)=0
            elif ans_real != 'null' and exec_acc == False:
                score = -1
            # x in UnANS; g(x)=1
            elif ans_real == 'null' and ans_pred != 'null':
                score = -1
            # x in UnANS; g(x)=0
            elif ans_real == 'null' and ans_pred == 'null':
                score = 1
            else:
                NotImplementedError
            reliablity_score.append(score)
            reliablity_score_dict[key] = score

        if return_dict:
            return reliablity_score, reliablity_score_dict
        else:
            return reliablity_score

    def penalize(self, scores, penalty=1):
        return np.mean([score*penalty if score == -1 else score for score in scores])
