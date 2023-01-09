# aqui importamos duas bibliotecas
import emoji
# porém neste aqui importamos somente o método
from pygame import mixer
# é uma peculiaridade desta biblioteca ter que iniciá-la
mixer.init()
# recebendo uma entrada de dados, números inteiros
nota = int(input('Digite sua nota: '))
nota2 = int(input('Digite a outra: '))
# neste programa temos que calcular a média de duas notas de um aluno...
# então criamos esta variável com operados para fazer o cálculo
s = (nota + nota2)/2
# este é um dicionário de cores para o terminal
c = {'v': '\033[1;31m', 've': '\033[1;32m', 'l': '\033[m'}
# criamos uma condição para que, se a média for maior que 5, o aluno será aprovado
if s >= 5:
    # usamos a função print para que mostre na tela
    print('Sua media é {}{}{}!'.format(c['ve'], s, c['l']))
    # aqui também mostramos uma mensegem junto de um emoji
    print(emoji.emojize('Parabéns!:clap:', use_aliases=True))
    # o método .mixer() serve para tocar sons no python
    mixer.music.load('sons/tada.mp3')
    mixer.music.play()
    # deixamos este input para que o programa continue tocando a música
    input()
# se não, estará reprovado
else:
    print('Sua média é {}{}{}.'.format(c['v'], s, c['l']))
    print(emoji.emojize('Estude mais!:punch:', use_aliases=True))
    mixer.music.load('sons/sadtrambone.mp3')
    mixer.music.play()
    # 'input' valor necessário para fechar o código, sem ele o programa de som não iniciaria
    input()
