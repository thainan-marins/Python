# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep


c = ('\033[m',         # cor 0 limpa
     '\033[1;97;41m',  # cor 1 vermelho
     '\033[1;97;42m',  # cor 2 verde
     '\033[1;97;44m',  # cor 3 azul
     '\033[1;30;107m',  # cor 4 preto fundo branco
     )


def ajuda(com):
    titulo(f'Acessando o manul do comando \'{com}\'', 3)
    sleep(1)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# programa principal


comando = ' '
while True:
    titulo('SISTEMA DE AJUDA INTERATIVA PYTHON!', 2)
    sleep(2)
    comando = input('Função ou biblioteca >> ')
    if 'fim' in comando.lower():
        sleep(1)
        break
    else:
        ajuda(comando)

titulo('Até logo!', 1)
