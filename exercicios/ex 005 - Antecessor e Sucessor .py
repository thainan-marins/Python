# neste programa fizemos com que ele dissesse qual o antecessor e o sucessor de algum número
# para isto rebemos uma entrada de dados formatados para números inteiros 'int'
n1 = int(input('Digite um número: '))
# então criamos a variáveis que irá somar e subtrair o número
r1 = n1-1
r2 = n1+1
# por fim printamos o resultado da variável.
print('O antecessor é {}{}{}, e o sucessor é {}{}{}.'.format('\033[7;97m', r1, '\033[m', '\033[7;97m', r2, '\033[m'))


