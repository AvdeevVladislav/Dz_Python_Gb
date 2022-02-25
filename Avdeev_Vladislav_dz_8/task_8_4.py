# Задание № 4

from functools import  wraps


def val_checker(check_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if args:
                for arg in args:
                    if not check_func(arg):
                        raise ValueError(f'irregular val')
            return func(*args)

        return wrapper

    return _val_checker


def telegraph(x):
    if isinstance(x, int) and x >= 0:
        return True
    return False


@val_checker(telegraph)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(f'Имя декоратора скрыто: {calc_cube.__name__}')
    print(calc_cube(5))
    print(calc_cube('ss'))