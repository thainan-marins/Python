def emp():
    print('Ops! deu empate.')


def usu():
    print('Você venceu!')


def pc():
    print('Eu venci!')


from random import choice
from time import sleep

print(f'\n{"-=" * 15}')
print(f'{"JO KEN PÔ":^30}')
print('-=' * 15)
opcoes = ['pedra', 'papel', 'tesoura']
veri = ' '
while True:
    while veri not in 'sn':
        veri = str(input('Ei! Vamos jogar Jokenpô? (s/n) ')).lower().strip()[0]
    if veri in 'n':
        break
    resposta = ' '
    while resposta not in opcoes:
        resposta = str(input('\nO que você escolhe? (pedra, papel ou tesoura): ')).lower().strip()
    sortepc = choice(opcoes)
    print('Eu escolho...')
    sleep(1.1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(0.9)
    print('PÔ!')
    print(f'\n--> {sortepc}')
    print()
    if resposta == opcoes[0] and sortepc == opcoes[1]:
        pc()
    if resposta == opcoes[0] and sortepc == opcoes[2]:
        usu()
    if resposta == opcoes[1] and sortepc == opcoes[0]:
        usu()
    if resposta == opcoes[1] and sortepc == opcoes[2]:
        pc()
    if resposta == opcoes[2] and sortepc == opcoes[0]:
        pc()
    if resposta == opcoes[2] and sortepc == opcoes[1]:
        usu()
    if resposta in sortepc:
        emp()
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('\nQuer jogar novamente? (s/n) ')).lower().strip()[0]
    if pergunta in 'n':
        break
