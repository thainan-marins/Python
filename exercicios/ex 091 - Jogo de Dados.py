# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
maior = menor = 0
input()
sorteio = dict({'1º jogador': randint(1, 6),
                '2º jogador': randint(1, 6),
                '3º jogador': randint(1, 6),
                '4º jogador': randint(1, 6)})
raking = {}
print(f'Valores sorteados: ')
# sortteio.item() pega as chaves e os valores, então k fica com as chaves e v com os valores
for k, v in sorteio.items():
    print(f'O {k} sorteou o número {v} ')
    sleep(1.5)
print('=' * 32)
# Itemgetter: Retorna um objeto chamável que busca item de seu operando usando o operando do método __getitem__(). Se múltiplo
# itens são especificados, retorna uma tupla de valores da pesquisa.
# o método sorted() serve para organizar listas, o operador 'itemgetter' extrai uma chave para comparação. Neste comando
# usamos como key de comparação o número, ou seja, os valores do dicionário. A lista ranking será organizado do maior
# para o menor (reverse=True)
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
# como ranking é uma lista não é possivel usar o método items(), então usamos o enumerate()
for key, value in enumerate(ranking):
    if key == 0:
        print(f'O {value[0]} tirou o número {value[1]} e venceu!')
    else:
        print(f'O {value[0]} tirou o número {value[1]}.')

