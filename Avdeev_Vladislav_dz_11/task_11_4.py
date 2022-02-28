# Задание № 4


class Store:
    def __init__(self, id, name, date_receipt, date_dispatch, warehouse_id):
        self.product_id = id
        self.product_name = name
        self.date_receipt = date_receipt
        self.date_dispatch = date_dispatch
        self.warehouse_id = warehouse_id

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

        