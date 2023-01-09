# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
# programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# EXTRA: Pergunte ao usuário se ele quer continuar.

# para fazer este programe precisamos criar uma tupla (que é a que ter parênteses) para ter o as frases já feitas
from time import sleep
escrita = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#n = int(input('Digite um número de 0 a 20: '))
resposta = 'sn'
# criamos um laço infinito
while True:
#while n > 20 or n < 0:

    n = int(input('Digite um número de 0 a 20: '))
#    for pos, estenso in enumerate(escrita):
#        if pos == n:
#            print(f'Você digitou o número \033[1;32m{estenso}\033[m.')

    # se o número for menor ou igual a 0 ou menor igual a 20, ou seja, se o número estiver entre 0 e 20
    if 0 <= n <= 20:
        print(f'Você digitou o número \033[32m{escrita[n]}\033[m.')
        # aqui o programa perguntará se você quer continuar
        resposta = str(input('Deseja continuar? [S/N] ')).strip().lower()
        # se o 's' estiver na resposta
        if resposta[0] in 's':
            continue
        # se não, se o usuário digitar 'Não', encerre o laço
        else:
            break
    # se o usuário digitar um número que não esteja entre 0 e 20, o programa irá retornar um erro
    else:
        print('\033[31mResposta inválida! Tente novamente.\033[m')
# quando o usuário digitar 'não' será mostrado na tela o programa sendo finalizado
print('Finalizando...')
sleep(1) # faz o computador esperar o tempo determinado
# por fim mostre na tela, programa finalizado
print('Programa finalizado com sucesso.')

 # CORREÇÃO DO EXERCÍCIO





