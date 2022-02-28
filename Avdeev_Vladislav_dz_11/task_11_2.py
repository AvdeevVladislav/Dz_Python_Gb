# Задание № 2


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_del = input('Введите делимое: ')
inp_to_del = input('Введите делитель: ')

try:
    inp_to_del = int(inp_to_del)
    inp_del = int(inp_to_del)
    if inp_to_del == 0:
        raise OwnError('Деление на ноль!')
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)
else:
    print(f'Результат деление: {inp_del / inp_to_del}')
