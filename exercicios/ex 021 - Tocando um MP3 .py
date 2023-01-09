# Este é um player de musica!

# Aqui importamos as bibliotecas necessárias para o programa
# esta para tocar a musica
import pygame
# para mostar emojis
import emoji
# para que usemos o método 'sleep'
import time
# iniciamos o pygame (biblioteca)
pygame.init()
# carregamos a musica para o programa
pygame.mixer.music.load('sons/exec.mp3')
# o método 'queue' em inglês fila, serve para adicionar uma música na sequência
pygame.mixer.music.queue('sons/exec2.mp3')
# Aqui começamos a tocar ela, usei o parâmetro start para difinir quando a musica começará
pygame.mixer.music.play(start=150)
# este método regula o volume da musica, um número float de 0.0 a 1
pygame.mixer.music.set_volume(0.2)
# mostramos na tela emojis de nota musical
print(emoji.emojize('\033[96m:notes: ' * 7, use_aliases=True))
# esta pode ser outra forma de mostrar emojis, você pode fazê-los através do 'tab' e alguns números
print('☺')

#valor necessário para fechar o código, sem ele o mp3 não é iniciado
input()
















