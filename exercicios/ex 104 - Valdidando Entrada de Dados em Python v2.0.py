# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# contudo fazendo a validação para aceitar apenas um valor numérico.


def leiaint(num):
    ok = False
    while ok is False:
        ler = input(num)
        try:
            n = int(ler)
            print(f'\033[1;32mVocê digitou o número {n}.\033[m')
            ok = True
        except Exception as erro:
            print(f'\033[1;31mEste não é um valor válido!\033[m')
            print()


leiaint('Digite um número (inteiro): ')

def leiafloat(num):
    ok = False
    while ok is False:
        while True:
            ler = input(num).replace(',', '.')
            if '.' in ler:
                break
            else:
                print(f'\033[1;31mEste não é um valor válido!\033[m')
                print()
        try:
            n = float(ler)
            print(f'\033[1;32mVocê digitou o número {n}.\033[m')
            ok = True
        except Exception as erro:
            print(f'\033[1;31mEste não é um valor válido!\033[m')
            print()


leiafloat('Digite um número (com vírgula): ')
