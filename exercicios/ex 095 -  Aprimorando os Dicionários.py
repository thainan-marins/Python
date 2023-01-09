# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

dicio = dict()
geral = []
from operator import itemgetter
while True:
    dicio.clear()
    dicio['Nome'] = str(input('Nome: '))
    dicio['Partidas'] = int(input('Partidas jogadas: '))
    gol = []
    for n in range(dicio['Partidas']):
        gol.append(int(input(f'Gols feitos na {n + 1}º partida: ')))
    dicio['Gols'] = gol.copy()
    dicio['Total de Gols'] = sum(dicio['Gols'])
    geral.append(dicio.copy())
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Desja cadastrar outro jogador? [S/N]: '))[0].lower()
    if resposta in 'n':
        break

print('-' * 40)
print('Cod.', end=' ')
for i in dicio.keys():
    print(f'{i:^15}', end='')
print()
for k, v in enumerate(geral):
    print(f'{k+1:<5}', end='')
    for d in v.values():
        print(f'{str(d):^15}', end='')
    print()
print()
print('-' * 65)
'''for k, v in enumerate(geral):
    print(f'{str(v):>3}', end='')
    for d in v.values():
        print(f'{str(k):<15}', end='    ')
print()
print('-' * 30)'''

cont = 0
while True:
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('\nDeseja mostrar detalhes de algum jogador? [S/N]'))[0].lower()
    if pergunta in 'n':
        break
    else:
        print()
        cont = 0
        for n in geral:
            cont += 1
            print(f'[{cont}] {n["Nome"]}')
    while True:
        jogador = int(input('\nQual? '))
        if jogador > len(geral):
            print('Erro! Jogador inexistente.')
            print()
        else:
            break
    print()
    for v, i in geral[jogador - 1].items():
        print(f'{v} = {i}')
    print()
    for i, g in enumerate(geral[jogador - 1]['Gols']):
        print(f'Marcou {g} gols na {i + 1}º partida' if g > 1 else f'Marcou {g} gol na {i + 1}º partida')


print(f'\nPrograma Finalizado.')

