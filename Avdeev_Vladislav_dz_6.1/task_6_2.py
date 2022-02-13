# Задание № 2


ip_numbers = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    file_lines = f.readline()
    f.seek(0)

    for line in f:
        new_line = f.readline()
        ip = new_line.split()[0]
        if ip not in ip_numbers:
            log_filter = list(filter(lambda el: el.split()[0] == ip, file_lines))
            ip_numbers[ip] = len(log_filter)
        else:
            continue

key_val = ip_numbers.items()
key_val_list = list(key_val)
max_ip_numbers = max(key_val_list, key=lambda x: x[1])
print(f'Спамер - {max_ip_numbers[0]} c числом запросов - {max_ip_numbers[1]}')





