# Задание №2

import requests
from decimal import *

getcontext().prec = 4

def currency_rates(money):
    money = money.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if money not in response:
        return None

    rub = response[response.find('<Value>', response.find(money)) + 7:response.find('</Value', response.find(money))]
    return f"{Decimal(rub.replace(',', '.'))}"


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates("GBP"))