# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

# é preciso inicializar as variáveis para poder usá-las depois
s = 0
count = 0
# como precisamos verificar cada número, criamos um laço e como sabemos o seu limite, o 'for' é bem apropriado
for c in range(1, 501, 2):
    # queremos somente os números múltiplos de 3, então criamos esta condição
    if c % 3 == 0:
        # a variável count vai dizer quantos valores passaram na ciclo
        count = count + 1 # esta variável 'c' é um contador, ou seja, ela conta os valores
        # e a variável 's', a soma entre eles
        s = s + c # esta variável 's' é um acumulador, ou seja, ela soma os valores
print('A soma de todos os {} múltiplos de 3 entre 1 e 500, \nÉ {}.'.format(count, s))
