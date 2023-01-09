# ENUNCIADO: Escreva um programa que leia dois números inteiros e
# compare-os, mostrando na tela, qual deles é o maior ou se são iguais.

# Para isto pedimos dois números inteiros ao usuário
n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
# como o intuito é comparação, criamos condições
# 'se o primeiro valor for maior que o sugundo, o primeiro valor é maior'
if n > n1:
    print('O primeiro valor é maior.')
# 'se não, se o segundo valor for maior que o primeiro valor, o segundo é maior'
elif n1 > n:
    print('O segundo valor é maior.')
# 'se não, os dois valores são iguais'
else:
    print('Não existe valor maior, os dois são iguais.')

