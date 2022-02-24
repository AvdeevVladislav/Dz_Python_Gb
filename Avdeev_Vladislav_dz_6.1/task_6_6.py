# Задание № 6


import os
import sys


mode = len(sys.argv)
with open(os.path.join('data', 'bakery.csv'), encoding='utf-8') as f:
    if mode == 1:
        for line in f.readlines():
            print(line.strip())

    elif mode == 2:
        script, min_number = sys.argv
        for line in f.readlines()[int(min_number) - 1:]:
            print(line.strip())

    elif mode == 3:
        script, min_number, max_number = sys.argv
        for line in f.readlines()[int(min_number) - 1:int(max_number)]:
            print(line.strip())