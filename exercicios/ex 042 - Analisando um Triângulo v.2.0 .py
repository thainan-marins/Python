# 	Refaça o DESAFIO 035 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:

# como no exercício 035 pedimos ao usuário três valores
a = float(input('Digite o comprimento da reta: '))
b = float(input('Digite o segundo: '))
c = float(input('Digite o terceiro: '))
# e também fazemos a fórmula para verificar se é ou não um triângulo
if a < b + c and b < a + c and c < a + b:
    print('Essas retas formam um triangulo', end=' ')
    # agora é simples, o triângulo equilátero tem todos os lados iguais
    if a == b == c:
        print('Equilátero.')
    # e o escaleno ter todos os lados diferentes
    elif a != b != c != a:
        print('Escaleno.')
    # se não for nunhem acima, só pode ser o isósceles
    else:
        print('Isósceles.')
# se a fórmula não for verdadeira, mostrará que não é possível formar um triângulo
else:
    print('Essas retas não formam um triângulo.')
