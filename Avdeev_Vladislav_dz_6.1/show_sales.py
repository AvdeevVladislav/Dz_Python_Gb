

def show_sales(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        sale_list = f.readlines()
        for i, el in enumerate(sale_list):
            sale_list[i] = el.replace('\n', '')
            if not args:
                print(sale_list[i])

        return 0


if __name__ == '__main__':
    import sys

    exit(show_sales(sys.argv))