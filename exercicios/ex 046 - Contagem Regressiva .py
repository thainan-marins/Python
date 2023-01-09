# Faça um programa que mostre na tela uma
# contagem regressiva para o estouro de fogos de artifício, indo de
# 10 até 0, com uma pausa de 1 segundo entre eles.

# importamos o método emojize para trancrever a palavres em emojis na tela
from emoji import emojize
# o sleep para fazer o compuador dormir por quantos segundo determinarmos
from time import sleep
# este é o principal ele que fará com que a música ocorra
from pygame import mixer
# criamos um dicionário de cores
co = {'l': '\033[m', 'r': '\033[3;97m', 'a': '\033[3;94m', 'am': '\033[3;93m'}
# iniciamos o método mixer, é uma peculiaridade da biblioteca
mixer.init()
# importamos os son com método load()
mixer.music.load('sons/coutdown.mp3')
# podemos adicionar outra em sequência com método queue()
mixer.music.queue('sons/fireworks.mp3')
# aqui ajustamos o volume, que é um float entre 0.0 e 1
mixer.music.set_volume(0.2)

# usamos o laço 'for' para fazer uma contagem regrassiva
for c in range(10, -1, -1):
    # cada número terá aproximadamente um segundo para ficar mais armoniozo
    sleep(0.9)
    # mostramos na tela a contagem
    print('{}> {}{}{}'.format(co['r'], co['a'], c, co['l']))
    # nesta conição dizemos 'se o 'c' for igual a 10', ou seja, quando a contagem começar...
    if c == 10:
        # inicie a música de contagem regrassiva
        mixer.music.play(start=-0.1)
# este print vazio serve para pular uma linha
print()
# espera dois segundos...
sleep(2) # este é o tempo até o sons dos fogos começar a reproduzir
# mostre na tela os emojis
print(emojize('{}:fireworks:{}      '.format(co['am'], co['l']) * 3, use_aliases=True))
print(emojize('     {}:fireworks:{}'.format(co['am'], co['l']) * 3, use_aliases=True))
# este comando é preciso para que o mixer funcione, sem ele o mixer não abre
input()




