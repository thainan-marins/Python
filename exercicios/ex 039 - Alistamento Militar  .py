# ENUNCIADO: Faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com sua idade os procedimentos necessários
# para de alistar.

# Sempre que tratamos de datas estas bibliotecas não podem ficar de fora
from datetime import date
# 'atual' reberá o ano atual da máquina
atual = date.today().year
# perguntamos o ano de nascimento do usuário
ano = int(input('Em que ano você nasceu? '))
# e também seu sexo
genero = str(input('Qual seu sexo? ')).strip().lower()
# a idade dela será igual a seu ano de nascimento menos o ano atual
idade = atual - ano
# como verificaremos homens e mulheres criamos esta condição
if genero == 'masculino':
    # se a idade for igual a 18 significa qua esta na hora de se alistar
    if idade == 18:
        print('Você tem {} anos e deve se alistar o mais breve possível!'.format(idade))
    # porém se a idade for menor que dezoito, terá de esperar
    elif idade < 18:
        # a variável 'saldo' recebe o valor de quantos anos ainda faltam para ele se alistar
        saldo = 18 - idade
        # então mostramos na tela
        print('Você tem {} anos e, ainda faltam {} anos para se alistar.'.format(idade, saldo))
        # também diremos em que ano ele deve se alista, para isto pegamos quantos anos ainda faltam e somamos ao ano
        # aual
        alis = atual + saldo
        # mostramos na tela o valor:
        print('Você deverá se alistar em {}.'.format(alis))
    # temos também a condição de que se o usuário for mais velho
    elif idade > 18:
        # neste caso a variável 'saldo' receberá o valor de quantos anos se passaram
        saldo = idade - 18
        print('Você tem {} ano(s) e, já se passaram {} do seu alistamento.'.format(idade, saldo))
        # e também mostraremos em que ano ele deveria ter se alistado subritraindo os valores
        alis = atual - saldo
        print('Você deveria se alistar em {}.'.format(alis))
# 'se não', se o usuário for do sexo feminino, mostraremos na tela:
else:
    print('Você não precisa passar pelo alistamento obrigatório ao exército. Obrigado por sua disposição!')
