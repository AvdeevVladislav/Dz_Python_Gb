# Заднание № 1


import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
    found_email = RE_MAIL.findall(email)
    if found_email:
        name, addr = found_email[0]
    else:
        raise ValueError(f'wrong email:{email}')
    print(name, addr)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    #email_parse('someone@geekbrainsru')
    email_parse('venom544@yandex.ru')
    