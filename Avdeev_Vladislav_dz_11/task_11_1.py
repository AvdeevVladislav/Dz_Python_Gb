# Задание № 1


class Date:

    @classmethod
    def int_date(cls, dd_mm_yyyy):
        try:
            day = int(dd_mm_yyyy[:2])
            month = int(dd_mm_yyyy[3:5])
        except TypeError:
            day = int(dd_mm_yyyy[1])
            month = int(dd_mm_yyyy[4])
        year = int(dd_mm_yyyy[6:10])
        return Date.check_date(day, month, year)

    @staticmethod
    def check_date(day, month, year):
        if year % 400 == 0 or year % 4 == 0:
            if month == 2 and day > 29:
                raise ValueError
        elif month == 2 and day > 28:
            raise ValueError
        elif (month != 2 and month % 2 == 0) and day > 30:
            raise ValueError
        elif month % 2 != 0 and day > 31:
            raise ValueError
        elif month > 12:
            raise ValueError
        return f'{day:02d}-{month:02d}-{year}'


print(Date.int_date('29-02-2024'))
print(Date.int_date('01-05-1983'))