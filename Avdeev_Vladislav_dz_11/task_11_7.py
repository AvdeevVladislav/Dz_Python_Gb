# Задание № 7


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + i * ({self.b})'

    def __add__(self, other):
        return f'({self.__str__()}) + ({other.__str__()}) = {self.a + self.b} + i * ({self.b + other.b})'

    def __sub__(self, other):
        return f'({self.__str__()}) - ({other.__str__()}) = {self.a - other.a} + i * ({self.b - other.b})'

    def __mul__(self, other):
        return f'({self.__str__()}) * ({other.__str__()}) = {self.a * other.a - self.b * other.b} + i *({self.b * other.a + other.a * self.a})'

    def __truediv__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return f'({self.__str__()}) / ({other.__str__()}) = {(a * c + b * d)/(c ** 2 + d ** 2)} + i * ({(b * c - a * d)/(c ** 2 + d ** 2)})'

c1 = ComplexNumber(5, 6)
c2 = ComplexNumber(1, 2)

print(c1)
print(c1 * c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)



















































































