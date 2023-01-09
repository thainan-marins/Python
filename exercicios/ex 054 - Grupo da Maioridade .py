# Crie um programa que leia o ano
# de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

# como vamos trabalhar com datas importamos o método 'date'
from datetime import date
# pegamos o ano atual da máquina
ano = date.today().year
# inicializamos as variáveis
count = 0
count2 = 0
# criamos o laço para ler o ano de nascimento de sete pessoas
for c in range(1, 8):
    n = int(input('{}° > Ano de nascimento: '.format(c)))
    # criamos uma condição: se 'n' mais 21 for menor ou igual a 'ano' a pessoa será maior de idade
    if n + 21 <= ano:
        # então contamos quantos são
        count += 1
    # se for menor, significa que ainda é de menor
    elif n + 21 > ano:
        # também contamos quantos
        count2 += 1
# então mostramos os valores na tela
print('''\nDas 7 pessos registradas obtem-se os seguintes dados:
{} NÃO são maior de idade e;
{} JÁ SÃO maior de idade.'''.format(count2, count))
