# Desenvolva um programa que leia o nome, idade e sexo de
# 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, ** qual é o nome do homem mais velho ** e quantas mulheres
# têm menos de 20 anos.

# incializamos várias variáveis
media = 0
soma = 0
maiori = 0
menori = 0
maioridadehomem = 0
homem = 0
velho = 0
count = 0

# crimos o laço para receber os dados
for p in range(1, 5):
    nome = str(input('O nome da {}ª pessoa: '.format(p)))
    sexo = str(input('O sexo da {}ª pessoa: '.format(p)))
    idade = int(input('A Idade da {}ª pessoa: '.format(p)))

    # calculamos qual destes é o maior, assim como anteriormente
    # se for o primeiro laço maiori e menori irão receber o valor de idade
    if p == 1:
        maiori = idade
        menori = idade
    # se não, se o próximo valor de idade for maior que maiori, maiori receberá idade
    else:
        if idade > maiori:
            maiori = idade
        if idade < menori:
            menori = idade

    # aqui analisamos qual é o nome do homem mais velho
    # se for o primeiro laço e na variável 'sexo' tiver m ou  M
    if p == 1 and sexo in 'mM':
        # maioridadehomem receberá o valor de idade
        maioridadehomem = idade
        # e para dizermos seu nome, 'homem' recebe 'nome'
        homem = nome
    # agora, se sexo ainda estiver em m o M, mas idade for maior que maioridadehomem
    if sexo in 'mM' and idade > maioridadehomem:
        # maioridadehomem receberá o novo valor de 'idade'
        maioridadehomem = idade
        # e 'homem' receberá o novo valor de 'nome'
        homem = nome

    # e aqui calculamos quais são as mulheres com menos de 20 anos
    if 'fem' in sexo and idade < 20:
        count += 1

    # o problema também pede a média, isso é simples, apenas somar todos os valores da idade e dividir pela quantidade
    # de pessoas registradas, no caso 4
    soma += idade
media = soma / 4

# por fim mostramos tudo isso na tela, apenas formatando os valores no print
print('\nA idade média destas pessoas é de {} anos.'.format(media))
print('A pessoa mais velha tem {} anos e a mais nova {} anos.'.format(maiori, menori))
print('O nome do homem mais velho é {}.'.format(homem))
print('E, existem {} mulheres abaixo dos 20 anos.'.format(count))
