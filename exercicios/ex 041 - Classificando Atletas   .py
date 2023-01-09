# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade.

# impormos o método data da biblioteca datetime para trabalhar com datas
from datetime import date
# perguntamos ao usuário em que ano nasceru
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year # a variável 'ano' recebe o valor do ano atual na máquina
# para saber a idade do atleta subitraimos os valores dos anos, assim obteremos o idade
idade = ano - nasc
print('Você tem {} anos:'.format(idade))
# agora é só criar as condições respectivas as idades...
if idade <= 9:
    print('Está na categoria Mirim.')
elif idade <= 14:
    print('Está na categoria Infantil.')
elif idade <= 19:
    print('Está na categoria Junior.')
elif idade <= 25:
    print('Está na categoria Sênior.')
else:
    print('Está na categoria Master.')
