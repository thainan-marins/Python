# Faça um programa que ajude um jogador da Mega Sena a criar
# palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
quant = int(input('Quantos jogos deseja realizar? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, v in enumerate(jogos):
    print(f'{i+1}º JOGO> {v}')
    sleep(1)
print()
print(f'{"BOA SORTE!":^30}')



