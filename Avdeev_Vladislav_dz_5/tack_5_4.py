# Задание № 4

import typing

def get_numbers(src: list) -> typing.Generator:
    for n in range(len(src) - 1):
        if src[n] < src[n + 1]:
         yield src[n + 1]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
