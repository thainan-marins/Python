# Neste programa diremos qual é o maior e o menor número que o usuário digitou

# da biblioteca time, importamos o métoda sleep, que fará o programa esperar (dormir)
from time import sleep
# criamos o dicionário de cores
co = {'am': '\033[93m', 'l': '\033[m', 'a': '\033[0;94m', 'a,s': '\033[4;94m'}
print('{}Digite três números...'.format(co['am']))
# um sleep de 1 segundo para o programa dormir durante 1 segundo
sleep(1)
# pedimos então ao usuário três número inteiros
a = int(input('O primeiro: '))
b = int(input('Segundo: '))
c = int(input('E terceiro:{} '.format(co['l'])))
#DEFININDO O NUMERO MENOR
# definindo "a" como o menor logo de cara, dispensa ter que fazer uma outra condição
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#DEFININDO O NUMERO MAIOR
# o mesmo para o maior... definimos ele inicialmente como o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# por fim mostramos na tela o print formatado com os valores das variáveis
print('{}O maior valor é {}{}{} e o menor valor é {}{}{}.{}'.format(co['a'], co['a,s'], maior, co['a'], co['a,s'],
                                                                    menor, co['a'], co['l']))
