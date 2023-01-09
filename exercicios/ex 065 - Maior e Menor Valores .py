# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

# inicializamos as variáveis para trabalhar com elas mais tarde
resposta = 'Ss'
contador = 0
valor = 0
media = 0
maior = menor = 0

# neste laço a condição é: se o usuário digitar SIM, o laço continuará
while resposta in 'Ss':
    valor = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar? ')).strip().lower()
    # aqui somamos os valores
    contador += valor
    # aqui contamos quantos números foram digitados
    media += 1

    # isto é o mesmo que: se o 'contador' for igual a 1, ou seja, se estiver no primeiro laço
    if contador == 1:
        # este valor será o maior e o menor (já que não existe outro valor ainda)
        maior = menor = valor

    # se não:
    else:
        # se o 'valor' (o novo valor) for maior que 'maior' (maior que o valor atribuído a variável 'maior')
        if valor > maior:
            # então a variável receberá este novo valor
            maior = valor

        # o mesmo irá acontecer com a variável 'menor'
        if valor < menor:
            menor = valor

# não criamos uma variável para colocar as operações, fizemos no próprio .format. Mostramos tudo na tela e o programa
# está finalizado.
print('Você digitou {} números, a média entre eles é {:.1f} \nO maior número é o {} e o menor {}.'.format(media, contador / media, maior, menor))
