

def add_sale(argv):
    argv = argv[1:]
    argv.append('\n')
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(argv)

    return 0

if __name__ == '__main__':
    import sys

    exit(add_sale(sys.argv))