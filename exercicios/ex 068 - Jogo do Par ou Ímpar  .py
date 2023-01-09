# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# como iremos lidar com sorteios, esta biblioteca é a melhor, ela sorteia números pseudo aleatórios
from random import randint

# iniciamos as variáveis
cont = 0
resposta = ' ' # se as aspas forem vazias o programa não irá lê-las, é preciso que elas estejam abertas.

print('Vamos jogar par ou ímpar?')

# criamos um laço infinito
while True:
    # pedimos ao usuários um valor
    valor = int(input('Diga um valor? '))
    # aqui o programa irá sortear um número de 1 a 10
    sorteio = randint(1, 10)
    # como no jogo de par ou ímpar, somamos os valores colocados por nós, faremos a mesma coisa aqui, somaresmos estes
    # valores e depois iremos ver se são pares ou ímpares
    resultado = valor + sorteio

    # aqui o usuário irá escolher se ele que par ou ímpar, com este laço ele não poderá dizer outra coisa a não ser
    # par ou ímpar, caso tente, o programa irá perguntar novamente até ter a resposta esperada
    while resposta not in 'pi':
        resposta = str(input('Par ou impar? P/I: ')).strip().lower()[0]
        print(f'O computador sorteou {sorteio}')

        # aqui fizemos uma condição simplificada, calculamos se o resultado é par ou ímpar
        print(f'O total é {resultado}. Deu PAR' if resultado % 2 == 0 else f'O total é {resultado}. Deu íMPAR')

    # então, se 'p' estiver em 'resposta', ou seja, se o usuário tiver escolhido par
    if 'p' in resposta:
        # e se o resultado for divisível por 2, ou seja, se for par
        if resultado % 2 == 0:
            # você irá vencer
            print('Você venceu!')
            # e será contada uma vitória
            cont += 1

        # Se não:
        else:
            # interrompa
            break

    # este é o mesmo caso do par!
    if 'i' in resposta:
        if resultado % 2 == 1:
            print('Você venceu!')
            cont += 1
        else:
            break

# por fim mostraresmos na tela que o usuário perdeu e quantas vezes conseguiu ganhar
print(f'Você perdeu! Com {cont} vitórias!')
