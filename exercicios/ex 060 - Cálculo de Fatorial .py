# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Ainda bem que o python tem um método para isto, ele está na biblioteca 'math'
from math import factorial
# perguntamos qual o número para fazer o factorial
n = int(input('Digite um número: '))
# então usando o método, fatoramos o valor de 'n'
f = factorial(n)
print('O factorial do número {} é {}'.format(n, factorial(n)))
# atribuimos o valor de n a variável c
c = n
print('{}! ='.format(n), end=' ')
# para mostrar essa fatoração por extenso, iremos usar um laço
# enquanto c > 0, ou seja, enquanto c não chegar no final:
while c > 0:
   # mostre o número atual no laço, no caso o valor de 'c'
   print(c, end=' ')
   # esta condição simplifica foi para deixar o comando um pouco mais plástico, ela fará com que
   # se ainda tiver mais um número coloque 'x', se não, coloque o sinal de igual
   print('x ' if c > 1 else '= ', end='')
   # como queremos que ele vá em uma ordem decerescente, subutraímos um número toda vez que ele passa pelo laço
   c -= 1
# mostramos na tela o valor do factorial com final igual a nada para que quando o laço acabar ele apareça na frente
print(f, end='')
