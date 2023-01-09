# Neste programa será um jogo que jogaremos com o computador, nós tentaremos adivinhar o número que o
# computador 'pensou'

# para isto importamos a biblioteca de números pseudoaleatórios
import random
# a biblioteca emoji para mostrar emojiscons na tela
import emoji
# e a biblioteca time somente com a função sleep para criar um interválo entra os prints
from time import sleep
# criamos um dicionário para as cores do terminal
c = {'v': '\033[31m', 'l': '\033[m', 've': '\033[32m', 'a': '\033[34m'}

# então perguntamos ao usuário se ele quer ou não jogar
user = str(input('{}Vamos jogar um jogo?{} '.format(c['ve'], c['l']))).strip().lower()
# caso responda sim, o programa irá ser executado
e = 'sim' in user
if e == True:
    a = random.randint(0, 5)
    print('{}Ok! estou pensando em um número...'.format(c['ve']))
    sleep(2)
    print('{}Pensei em um número de o a 5! Tente advinha-lo!{}'.format(c['ve'], c['l']))
    r = int(input('Resposta: '))
    # Aqui fizemos uma condição simplificada dizendo se o usuário venceu ou perdeu.
    print('{}Parabéns!, você acertou.'.format(c['a']) if a == r else '{}Que pena, você errou.'.format(c['v']))
# se não, o cumputador irá dar Tchau e o programa irá se finalizar.
else:
    print(emoji.emojize('{}Bom, então até mais... :wave:{}'.format(c['v'], c['l']), use_aliases=True))
