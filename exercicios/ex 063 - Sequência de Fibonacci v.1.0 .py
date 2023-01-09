# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

# pedimos os valores interiros ao usuário
n = int(input('Digite um número: '))
e = int(input('Quantos termos deseja mostrar? '))

# inicializamos as variáveis
contador = 0 # irá contar quando vezes o laço ocorreu
# será o primeiro termos da sequência
t1 = n
# será o segundo termos da sequência
t2 = n + 1

# aqui mostraremos os 2 primeiros termos
print('{} → {} '.format(t1, t2), end='→ ')

# enquanto 'contador' for menor ou igual a 'e', ou seja, enquanto não chagar ao números de termos digitado pelo usuário
while contador <= e:
    # e o terceiro termo, via de regra, será a soma dos dois termos anteriores
    t3 = t1 + t2 # como precisamos de um quarto termo ele será a soma dos dois primeiros, que receberam novos valores
    print(t3, end=' → ')
    # como a sequêcia precisa continuar, usaremos uma forma de reset
    t1 = t2 # o primeiro termo agora será o segundo
    t2 = t3 # o segundo termo será o terceiro
    contador += 1
# finalizamos o programa.
print('Fim.')
