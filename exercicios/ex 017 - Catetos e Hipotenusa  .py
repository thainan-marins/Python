# Novamente importamos a biblioteca math, neste programa usaremos somente o método 'sqrt', que serve para calcular
# a raiz quadrada de um número
from math import sqrt
# criamos o dicionário
c = {'am': '\033[93m', 'r': '\033[35m', 'l': '\033[m'}
# então pedimos os dados para o usuário
co = float(input('Qual o valor do cateto oposto? {}cm:{}'.format(c['am'], c['l'])))
ca = float(input('Qual o valor do cateto adjascente? {}cm:{}'.format(c['am'], c['l'])))
# os operadores '**' fazem o potenciação do número
n = (co ** 2) + (ca ** 2)
# criamos a variável para calcular a raiz quadrada da variável 'n' que contém os dois valores antes pedidos
raiz = sqrt(n)
# mostramos na tela o resultado colorido
print('A hipotenusa é {}{:.2f}{}.'.format(c['r'], raiz, c['l']))

