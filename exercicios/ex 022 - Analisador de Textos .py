# importamos esta biblioteca apenas para fins estéticos
from time import sleep
# pedimos ao usuáro uma string
n = input('Qual o seu nome? ')
# criamos um dicionàrio para cores
c = {'a,i': '\033[3;94;100m', 'l': '\033[m'}
# nesta variável, tiramos os espaços no valor digitado, para que possemos contar somente a letras do nome do usuário
su = n.replace(' ', '')
# também precisaremos dizer quantas letras tem apenas o primeiro nome do usuário, então dividimos o nome
# com o splip que separa cada palavre em índices
div = n.split()
print('Veja o que sei fazer...')
sleep(1)
# mostramos na tela ua formatção da variável 'n' em caixa alta
print('> Seu nome em maiúsculo, {}{}{}!'.format(c['a,i'], n.upper(), c['l']))
print()
# nesta mostramos ela em minúsculo
print('> Seu nome em minúsculo, {}{}{}!'.format(c['a,i'], n.lower(), c['l']))
print()
# agora mostramos quantas letras tem o nome ao todo. Usando a fução len(), podemos saber o tamnho de vários objetos
print('> Seu nome ao todo tem {}{}{} letras!'.format(c['a,i'], len(su), c['l']))
print()
# como vimos antes, aqui mostramos somente as letras do primeiro nome
print('> E seu primeiro nome tem {}{}{} letras!'.format(c['a,i'], len(div[0]), c['l']))
print()
print('(ADICIONAL)')
# aqui o nome esta capitalizado, o que significa que apenas a primeira letra da frase ficará em letra maiuscula
print('> Seu nome capitalizado, {}{}{};'.format(c['a,i'], n.capitalize(), c['l']))
print()
# ja no método title, toda letra de cada palavra irá ficar em maiúsculo, ele irá verficar, em todo espaço que achar
# Irá colocar um letra maiúscula
print('> Seu nome titularizado, {}{}{}.'.format(c['a,i'], n.title(), c['l']))
