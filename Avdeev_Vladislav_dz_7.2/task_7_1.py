# Задание № 1


import os

patent = {'my_project': ['setting', 'mainapp', 'adminapp', 'authapp']}
for root, folders in patent.items():
    if os.path.exists(root):
        print(root, 'присутствует')
    else:
        for folder in folders:
            dir = os.path.join(root, folder)
            os.makedirs(dir)
