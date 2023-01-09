# Neste programa crimos uma espécie de calculadora para saber se três valores formam ou não um triângulo

# da biblioteca emoji importamos o método emojize, responsável por mostrar emojis escritos, em imagens na tela
from emoji import emojize
# criamos o dicionário de cores
co = {'v': '\033[31m', 've': '\033[32m', 'l': '\033[m'}
# nos três seguintes inputs iremos perguntar ao usuário os valores da retas que deseja testar
a = float(input('\033[1mQual o menor comprimento da reta? '))
b = float(input('Qual o segundo menor comprimento da reta? '))
c = float(input('E qual o comprimento da terceira reta? '))
# como este é um princípio matemático, ele possui uma fórmula:
if a < b + c and b < a + c and c < a + b: # se esta fórmula for verdadeira então ao retas formaram um triângulo
    print(emojize('{}Essas retas formam um triangulo.:white_check_mark:'.format(co['ve']), use_aliases=True))
# 'se não' mostre na tela estas retas não formam um triângulo
else:
    print(emojize('{}Essas retas não formam um triangulo.:negative_squared_cross_mark:'
                  .format(co['v']), use_aliases=True))
