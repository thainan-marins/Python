# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def dimensao(comprimento, largura):
    area = comprimento * largura
    print('=-=' * 15)
    print(f'''O terreno possui as seguintes dimensões:
{comprimento}m de comprimento X {largura}m de largura.
\nA área do terreno será de {area}m².''')


a = float(input('Qual a largura do terreno? '))
c = float(input('Qual o comprimento? '))
dimensao(c, a)
