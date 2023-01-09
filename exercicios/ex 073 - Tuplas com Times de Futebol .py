# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# também criamos uma tupla aqui para poder manipular as frases mais tarde
times = ('Flamengo', 'Palmeiras', 'Athlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo',
         'Internacional', 'Fluminense', 'Corinthinas', 'Fortaleza', 'Bahia', 'Ceara', 'Cruzeiro', 'América Mineiro',
         'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')
c = {'l': '\033[m', 'b': '\033[1;97m'}
print('{}{:-^50}'.format(c['b'], 'RANKING DA CBF PARA 2022'))
print('Os 5 primeiros colocados foram respectivamente:{}'.format(c['l']))

# este laço fará com que a variável t pega apenas um elemento da tupla times, a formatação nas chaves serve para pegar
# os 5 primeiros
for t in times[:5]:
    print(t)
#for p, al in enumerate(times, start=1):
    #print(p, al)
print(' ------//------ ' * 3)
print('{}Os últimos 4 colocados foram:{}'.format(c['b'], c['l']))
# aqui também criamos uma laço para pegar apenas um elemento por fez (para formar uma lista), mas desta vez o 4 últimos
for i in times[-4:]:
    print(i)
#for po, alf in enumerate(times[16:], start=17):
#    print(po, alf)
print(' ------//------ ' * 3)
print('{}Organização dos times por ordem alfabética:{}'.format(c['b'], c['l']))
# a variável 'm' receberá a tupla 'times' em hordem alfabética, feita pelo método sorted()
for m in sorted(times):
    print(m)
#al = sorted(times)
#for pos, alfa in enumerate(al):
    #print(f'{alfa}')
print(' ------//------ ' * 3)
# este último print irá mostrar em que posição está o time da chapecoence pelo método index()
print('{}A Chapecoense está na {}ª posição.{}'.format(c['b'], times.index('Chapecoense')+1, c['l']))
# CORREÇÃO DO EXERCÍCIO


