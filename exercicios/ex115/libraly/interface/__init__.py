def leiaint(num):
    ok = False
    n = 0
    while ok is False:
        ler = input(num)
        try:
            n = int(ler)
            ok = True
        except Exception as erro:
            print(f'\033[1;31mEste não é um valor válido!\033[m')
            print()
    return n


def linha(com=42):
    return print('-' * com)


def cabeçalho(txt=' '):
    linha()
    print(f'{txt:^42}')
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = leiaint('Sua opção: ')
    return opc




