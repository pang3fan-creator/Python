users = [1, 2, 3]
class_name = [{'id': 1, 'name': '语文'}, {'id': 2, 'name': '数学'}, {'id': 3, 'name': '英语'}]
scores = [
    {"student_id": 1, "class_id": 1, "score": 80, }, {"student_id": 1, "class_id": 2, "score": 89, },
    {"student_id": 1, "class_id": 3, "score": 85, }, {"student_id": 2, "class_id": 1, "score": 92, },
    {"student_id": 2, "class_id": 2, "score": 75, }, {"student_id": 2, "class_id": 3, "score": 36, },
    {"student_id": 3, "class_id": 1, "score": 60, }, {"student_id": 3, "class_id": 2, "score": 77, },
    {"student_id": 3, "class_id": 3, "score": 92, }, ]
# [
# 	{ 1: {"语文":B,"数学":B,"英语":B}},
# 	{ 3: {"语文":B,"数学":B,"英语":B}},
# 	{ 5: {"语文":B,"数学":B,"英语":B}},
# ]
result_list = []
for u in users:
    dict_2 = {}
    dict_1 = {}
    for c in class_name:
        for s in scores:
            if s["student_id"] == u and s['class_id'] == c['id']: dict_1[c['name']] = s['score']
    dict_2[u] = dict_1
    result_list.append(dict_2)
print(result_list)

result_1 = [
    {i:
         {c['name']: s['score']
          for s in scores for c in class_name
          if s['student_id'] == i and s['class_id'] == c['id']}
     }
    for i in users]
print(result_1)
#
