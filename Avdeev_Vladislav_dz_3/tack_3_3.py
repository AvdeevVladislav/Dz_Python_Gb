# Задание № 3


def thesaurus(*args) -> dict:
    dict_out = {}
    for name in args:
        dict_out.setdefault(name[0], [])
        dict_out[name[0]].append(name)
    dict_out = dict(sorted(dict_out.items()))
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))



