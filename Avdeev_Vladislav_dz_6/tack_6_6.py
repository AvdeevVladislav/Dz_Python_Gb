# Задание № 6


import sys
import os

STRING_LENGTH = 7

if len(sys.argv) < 2:
    print('Указать значение')
    sys.exit(1)
else:
    with open(os.path.join('day', 'bakery.csv'), 'a', encoding='utf-8') as f:
        script, number = sys.argv
        try:
            number_int = float(number.replace(',', '.'))
            f.write(f'{number.zfill(STRING_LENGTH - 1)}\n')
        except ValueError:
            print('Укажите значение в формате "сумма, сумма"')
