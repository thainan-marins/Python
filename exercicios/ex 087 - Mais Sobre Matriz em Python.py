# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados;
# b) A soma dos valores da terceira coluna;
# c) O maior valor da segunda linha.

lista1 = []
lista2 = []
lista3 = []
soma = 0
somadaterceira = 0
num = 0
mai = 0
for n in range(0, 9):
    num = int(input('Diga um número: '))
    if num % 2 == 0:
        soma += num
    if n == 0:
        lista1.append(num)
    if n == 1:
        lista1.append(num)
    if n == 2:
        lista1.append(num)
        somadaterceira += num
    if n == 3:
        lista2.append(num)
        mai = num
    if n == 4:
        lista2.append(num)
        if num > mai:
            mai = num
    if n == 5:
        lista2.append(num)
        somadaterceira += num
        if num > mai:
            mai = num
    if n == 6:
        lista3.append(num)
    if n == 7:
        lista3.append(num)
    if n == 8:
        lista3.append(num)
        somadaterceira += num

princ = [lista1[:], lista2[:], lista3[:]]
print('-=' * 11)

print('MATRIZ:')
print(f'[ {lista1[0]} ]  [ {lista1[1]} ]  [ {lista1[2]} ]')
print(f'[ {lista2[0]} ]  [ {lista2[1]} ]  [ {lista2[2]} ]')
print(f'[ {lista3[0]} ]  [ {lista3[1]} ]  [ {lista3[2]} ]')
print('-=' * 11)

print(f'A soma de todos os valores pares digitados é  {soma};')
print(f'\nA soma dos valores da terceira colula é  {somadaterceira};')
print(f'\nO maior número da segunda linha é  {mai}.')

