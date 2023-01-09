# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

from math import factorial


def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número.
    :param num: é o valor a ser calculado.
    :param show: parâmetro opicional. Ele mostra ou não a conta.
    :return: o valor fatorial do número.
    """
    valor = num
    if show is True:
        while num > 0:
            print(num, end=' ')
            print('X' if num > 1 else '=', end=' ')
            num -= 1
        print(factorial(valor))
    else:
        print(f'O fatorial de {valor} é igual a {factorial(valor)}')


fatorial(5, show=False)
