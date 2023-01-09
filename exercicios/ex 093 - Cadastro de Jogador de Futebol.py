# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dicio = dict()
dicio['nome'] = str(input('Nome: '))
dicio['partida'] = int(input('Partidas jogadas: '))
gol = []
for n in range(dicio['partida']):
    gol.append(int(input(f'Gols feitos na {n+1}º partida: ')))
golsdocampeonato = sum(gol)
dicio['gols'] = gol
dicio['totgols'] = golsdocampeonato
print('=-=' * 12)
print(f'''O jogador {dicio["nome"]} jogou {dicio["partida"]} partidas no compeonato
e marcou {dicio['totgols']} gols no total.''')
for i, g in enumerate(dicio['gols']):
    print(f'    Na {i+1}º partida ele marcou {g} gols')
print('''

Fim.''')

