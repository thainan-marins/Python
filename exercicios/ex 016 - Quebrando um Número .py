# Esta é uma biblioteca muito útil do python, se trata de operadores matemáticos
from math import trunc # neste programas porém, usaremos somente o método trunc, que remove qualquer número depois
# da vírgula
# o dicionário de cores
c = {'n': '\033[1m', 'v': '\033[31m', 've': '\033[32m', 'l': '\033[m'}
# pedimos ao usuário um número inteiro
n = float(input('Digite um número: '))
# criamos uma variável para o método
inte = trunc(n)
# por fim mostramos na tela a porção inteira do número digitado
print('{0}A porção inteira do número {1}{2}{3}{4} é {5}{6}{7}'.format(c['n'], c['ve'], n, c['l'], c['n'], c['v'], inte, c['l']))



