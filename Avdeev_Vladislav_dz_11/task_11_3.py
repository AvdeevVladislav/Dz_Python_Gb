# Задание № 3


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
inp_num = 0

while inp_num != 'stop':
    inp_num = input("Вводите элемент списка(число):")

    try:
        if not inp_num.isnumeric():
            raise OwnError("Ошибка. введен текст!")
    except OwnError as err:
        print(err)
    else:
        my_list.append(inp_num)

print(my_list)
