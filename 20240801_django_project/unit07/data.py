users = [1, 3, 5]

classes = [{'id': 1, 'name': '语文'}, {'id': 2, 'name': '数学'}, {'id': 3, 'name': '英语'}]

scores = [
    {
        "student_id": 1,
        "class_id": 1,
        "score": 10,
    },
    {
        "student_id": 1,
        "class_id": 2,
        "score": 20,
    },
    {
        "student_id": 1,
        "class_id": 3,
        "score": 30,
    },
    {
        "student_id": 3,
        "class_id": 1,
        "score": 40,
    },
    {
        "student_id": 3,
        "class_id": 2,
        "score": 50,
    },
    {
        "student_id": 3,
        "class_id": 3,
        "score": 60,
    },
    {
        "student_id": 5,
        "class_id": 1,
        "score": 70,
    },
    {
        "student_id": 5,
        "class_id": 2,
        "score": 80,
    },
    {
        "student_id": 5,
        "class_id": 3,
        "score": 90,
    },
]

# [
# 	{ 1: {"语文":B,"数学":B,"英语":B}},
# 	{ 3: {"语文":B,"数学":B,"英语":B}},
# 	{ 5: {"语文":B,"数学":B,"英语":B}},
# ]

result = [
    {
        user_id:
            {
                class_item.get('name'): score_item.get('score')
                for score_item in scores for class_item in classes
                if score_item.get('student_id') == user_id
                   and score_item.get('class_id') == class_item.get('id')
            }
    } for user_id in users
]
print(result)
