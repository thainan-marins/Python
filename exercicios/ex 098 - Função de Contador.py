# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'\nFazendo a contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
            sleep(0.5)
        print()
    else:
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo
            sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 1, 2)

print('\nAgora é sua vez de fazer uma contagem...')
contador(inicio=int(input('Inicio: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))


