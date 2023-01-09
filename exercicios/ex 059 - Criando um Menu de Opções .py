# Crie um programa que leia dois valores e
# mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior número
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
soma = 0
mult = 0
maior = 0
resposta = 0
# Pedimos ao usuário os dois valores inteiros que vamos trabalhar
num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
# como no menu o número 5 significa sair do programa, o laço so vai continuar até ser digitado o 5
while resposta != 5:
    #sleep(2)
    print('=-' * 10)
    print('''1 > Somar
2 > Multiplicar
3 > O maior
4 > Novos números
5 > Sair so programa''')
    # pedimos ao usuário qual opção do menu, com  o tipo primitivo inteiro
    resposta = int(input('Qual sua opção: '))
    # como se trata de um menu precisamos criar uma condição para cada item dele
    if resposta == 1:
        soma = num + num2
        print('O nº {} mais o nº {} é igual a {}.'.format(num, num2, soma))
    elif resposta == 2:
        mult = num * num2
        print('O nº {} vezes o nº {} é igual a {}.'.format(num, num2, mult))
    elif resposta == 3:
        maior = num
        if num2 > maior:
            maior = num2
        print('Entre os nº {} e {}, o nº {} é o maior.'.format(num, num2, maior))
    elif resposta == 4:
        num = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
        # precismos também calcular o fator erro, se o usuário digitar algo que não esteja no menu, o programa irá
        # retornar 'resposta inválida' e recomeçará o laço
    elif resposta > 5 or resposta < 1:
        print('Opção inválida! tente novamente.')
    sleep(2)
# quando for digitado 5, mostrará na tela que o programa acabou e o programa se encerrará
print('Programa finalizado!')
