# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.

# inicializamos a variáveis
maior = 0
menor = 0
# criamos um laço para ler o peso de 5 pessoas
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    # se c == 1, ou seja, se for o primeiro laço...
    if c == 1:
        # maior e menor vão recerber o valor de 'peso'
        maior = peso
        menor = peso
    # se não, maior irá receber o próximo valor maior
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
# mostramos na tela os valores
print('O maior peso é o {}, e o menor é o {}. '.format(maior, menor))
