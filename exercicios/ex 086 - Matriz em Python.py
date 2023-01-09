# Crie um programa que crie uma matriz de dimensão 3X3 e preencha com
# valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatção correta.

temp = []
fila1 = []
fila2 = []
fila3 = []
cont = 0
for n in range(0, 9):
    temp.append(int(input('Diga um valor: ')))
    if n == 0:
        fila1.append(temp[:])
    if n == 1:
        fila1.append(temp[:])
    if n == 2:
        fila1.append(temp[:])
    if n == 3:
        fila2.append(temp[:])
    if n == 4:
        fila2.append(temp[:])
    if n == 5:
        fila2.append(temp[:])
    if n == 6:
        fila3.append(temp[:])
    if n == 7:
        fila3.append(temp[:])
    if n == 8:
        fila3.append(temp[:])
    temp.clear()
print(fila1)
print(fila2)
print(fila3)
