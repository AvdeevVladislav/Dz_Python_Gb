# Задание № 3


from itertools import zip_longest
import json
voc = {}
with open('users.csv', 'r', encoding='utf-8') as user, open('hobby.csv', 'r', encoding='utf-8') as hobby:
    num_line_user = sum(1 for line in user)
    num_line_hobby = sum(1 for line in hobby)

    if num_line_user < num_line_hobby:
        exit(1)

    user.seek(0)
    hobby.seek(0)
    for line_user, line_user_hobby in zip_longest(user, hobby):
        voc[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('task_6_3_result.json', 'w', encoding='utf-8') as f:
    json.dump(voc, f, ensure_ascii=False)

print(voc)
