# importamos os métodos da biblioteca math para realizar operações
from math import sin, cos, tan, radians
# criamos o dicionário
c = {'c': '\033[36m', 'n': '\033[1m', 'l': '\033[m', 've': '\033[32m'}
# pedimos ao usuário um valor com ponto flutuante
angulo = float(input('Qual é o angulo? :'))
# nesta variável estamos convertendo o valor digitado de graus  para radianos
sen = sin(radians(angulo))
# aqui calculamos o cosseno do valor digitado
cos = cos(radians(angulo))
# e este calculamos a tangente
tg = tan(radians(angulo))
# mostramos na tela com a formatação de cor e os respectivos valores
# a função '\n' serve para pular a linha dentro do print
print('O valor do seno de {}{}°{} é {}{:.2f}{}; \nDo cosseno é {}{:.2f}{}; \nE da tangente é {}{:.2f}{}.'
      .format(c['ve'], angulo, c['l'], c['c'], sen, c['l'], c['c'], cos, c['l'], c['c'], tg, c['l']))








