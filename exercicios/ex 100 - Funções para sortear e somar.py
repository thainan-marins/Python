# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = list()


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os números sorteados foram ', end='')
    for c in lista:
        print(c, end=' ')


def somapar(lista):
    soma = 0
    for d in lista:
        if d % 2 == 0:
            soma += d
    print(f'\nA soma entre os números pares é igual a {soma}')


sorteia(numeros)
somapar(numeros)
