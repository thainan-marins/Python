# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# pedimos um valor interio ao usuário
valor = int(input('Quanto deseja sacar? R$'))
total = valor
# como se trata de saques, pegaremos o maior nota possível para dar ao 'cliente'
ced = 50
# está variável irá contar quantas cédulas foram dadas
totced = 0
# criamos um laço infinito
while True:
    # se o total for maior que a cédula, ou seja, quando o valor for maior que minha cédula com o valor de $50
    if total >= ced:
        # o valor receberá uma subtração do valor da cédula, ou seja, o valor menor 50 reais
        total -= ced
        # e é contado mais uma cédula
        totced += 1
    else: # se não
        # se o total de cédula for diferente de 0, mostre na tela o total de cédulas e seu valor
        # esse comando só será executado quando uma contagem se cédulas for finalizado
        if totced != 0:
            print(f'{totced} cédulas de {ced}.')
        # se a cédula for igual a 50, cédula recebe o valor de 20
        if ced == 50:
            ced = 20
        # se cédula for igual a 20, cédula recebe 10
        elif ced == 20:
            ced = 10
        # se cédula for igual a 10, cédula recebe 1
        elif ced == 10:
            ced = 1

        totced = 0
        # se o total for igual a 0, ou seja, quando o valor tiver chegado ao 0 o programa irá se finalizar
        if total == 0:
            break


