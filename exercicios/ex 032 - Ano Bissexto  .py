# O objetivo deste programa é dizer se o ano que o usuário digitou é bissexto ou não

# como se trata de datas importamos o método 'date' biblioteca datetime
from datetime import date
# criamos o dicionário de cores
c = {'n': '\033[1;37m', 'l': '\033[m', 'b': '\033[7;97;40m', 'p': '\033[7;30;107m'}
# perguntamos ao usuário que ano deseja fazer a análise
ano = int(input('Qual ano desaja saber se é bissexto? {}Para saber sobre o ano atual digite 0:{} '.format(c['n'], c['l'])))
# criamos uma condição
# todo ano divisível por 4 é bissexto, porém existem algumas exeções: ele pode ser múltiplo de 400, mas não pode ser
# (todo) múltiplo de 100
if ano == 0: # se o usuário digitar 0, o programa dirá se o ano atual é bissexto
    ano = date.today().year # este método "today().year" pega o ano atual da máquina
# " Se o ano for divisível por 4 E não divisível por 100 ou divisível por 400, mostre na tela: Ano bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano de {} É um ano bissexto!{}'.format(c['b'], ano, c['l']))
# Se não, mostre: Não é um ano bissexto
else:
    print('{}O ano de {} NÃO é um ano bissexto.{}'.format(c['p'], ano, c['l']))
    
