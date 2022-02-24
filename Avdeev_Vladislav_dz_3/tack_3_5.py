# Задание № 5
import random


def get_jokes(count=2, repeat=True) -> list:

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_out = []

    if not repeat:
        min_gen = min(len(nouns), len(adverbs), len(adjectives))
        if count > min_gen:
            count = min_gen

        for i in range(count):
            if repeat:
                keyword_list = list(map(random.choice, [nouns, adverbs, adjectives]))
            else:
                keyword_list = list(map(lambda x: x.pop(random.randrange(len(x))), [nouns, adverbs, adjectives]))
            list_out.append(' '.join(keyword_list))

        return list_out

print(get_jokes(count=3,repeat=True))
print(get_jokes(count=10,repeat=False))
print(get_jokes(count=5,repeat=True))

