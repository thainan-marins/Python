# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import datetime # colocar a importação aqui fará com que ela funcione somente aqui, mas também import
    # vai economizar memória.
    anoatual = datetime.today().year
    idade = anoatual - ano
    if 18 <= idade <= 70:
        return print(f'Com {idade} anos o voto é OBRIGATÓRIO.')

    if idade < 16:
        return print(f'Com {idade} anos o voto é NEGADO.')

    if 16 >= idade < 18 or idade > 70:
        return print(f'Com {idade} anos o voto é OPICIONAL.')


voto(int(input('Qual seu ano de nascimento? ')))
