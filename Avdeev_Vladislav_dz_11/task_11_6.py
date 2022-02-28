# Задание № 6


class Store:
    def __init__(self, name='', stock=0):
        self.store_dict = {name: stock}
        self.type = name

    def goods_receipt(self, name, count):

        try:
            count = int(count)
        except ValueError:
            print('Проблема. Кол-во продукции должно быть числом')
        else:
            if self.store_dict.get(name):
                self.store_dict[name] += count
                print(f'Продукция {name} добавлена на склад в кол-во {count}, остаток: {self.store_dict[name]}')
            else:
                if self.store_dict.get(name):
                    self.store_dict[name] += count
                    print(f'Новая продукция {name} добавлена на склад в кол-во {count}')


    def goods_send(self, name, count, office):

        if self.store_dict.get(name):
            if self.store_dict[name] >= count:
                self.store_dict[name] -= count
                print(f'Проудкция {name} доставлена в {office}. Остаток на складе: {self.store_dict[name]}')
            else:
                print(f'{name} кол-во недостаточно на складе')
        else:
            print(f'{name} отсуствует на скаде')

    def show_stocks(self):
        return self.store_dict


class OfficeEquipment(Store):
    def __init__(self, id, name, type):
        super().__init__(id, name)
        self.type = type

class Printer(OfficeEquipment):
    def __init__(self, id, name, type, printer_type):
        super().__init__(id, name, type)
        self.printer_type = printer_type

class Scaner(OfficeEquipment):
    def __init__(self, id, name, type, scanner_speed):
        super().__init__(id, name, type)
        self.scanner_speed = scanner_speed

class Xerox(OfficeEquipment):
    def __init__(self, id, name, type, resolution):
        super().__init__(id, name, type)
        self.resolution = resolution


d = Store()
d.goods_receipt('Printer', 4)
d.goods_receipt('Xerox', 2)
d.goods_receipt('Xerox', 8)
d.goods_receipt('Scaner', 2)

d.goods_send('Printer', 1, 'Office 1')
d.goods_send('Xerox', 10, 'Office 2')

d.goods_receipt('Scaner', 'таак')


