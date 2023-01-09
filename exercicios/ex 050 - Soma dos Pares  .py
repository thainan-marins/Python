# Desenvolva um programa que
# leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

# inicializamos as variáveis
soma = 0
count = 0
# fazemos um laço para perguntar 6 vezes ao usuário
for c in range(0, 6):
    valor = int(input('Digite um número: '))
    # nesta condição dizemos, se o resto da divisão por 2 for igual a 0, ou seja, se o 'valor' for divisível por 2
    if valor % 2 == 0:
        # esta variável irá somar os valores
        soma += valor
        # e esta, quantos valores passaram pelo laço
        count += 1
# por fim, mostramos tudo na tela
print('A soma do(s) {} número(s) PARES é {}.'.format(count, soma))


