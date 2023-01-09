# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no  final quantos palpites foram necessários para vencer.


from time import sleep
# Como vamos sortear números inteiros importamos o método randint da biblioteca random
from random import randint
print('Ei, vamos jogar uma jogo!')
sleep(1)
print('''Vou pensar em um número de 1 a 10
e você terá de avinhar, ok?''')
sleep(2)
print('PENSANDO...')
sleep(1)
# aqui difinimos a amplitudo do sorteio, no caso de 1 a 10
sorte = randint(1, 10)
acertou = False #Também pode-se criar uma variavel False, e se o resultado for real torna-la True
#while resposta != sorte:
count = 0
# enquando 'acertou' não é verdadeiro:
while not acertou:
    resposta = int(input('Tente adivinha-lo! . R: '))
    # este 'count' serve para dizer quantas tentativas foram necessárias para acertar o número
    count += 1
    # se o usuário responder o mesmo número que a máquina sorteou, o laço se torna verdadeiro e se encerra
    if resposta == sorte:
        acertou = True
    else:
        # para ficar mais interessante iramos dizer se está perto ou longe do número
        # se 'resposta' for maior que 'sorte', ou seja, se o que o usuário digitou for maior que número que o computador
        # sorteou, ele irá dizer
        if resposta < sorte:
            print('É um número maior...')
        # o mesmo acontece se for menor
        elif resposta > sorte:
            print('É um número menor...')
print('Parabéns, você acertou em {} tentativas!'.format(count))
