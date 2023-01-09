# Faça um programa que leia o nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas;
# b) Uma listagem com as pessoas mais pesadas;
# c) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? '))[0].lower()
    if resp in 'n':
        break
print(f'Ao todo {len(princ)}  foram cadastradas')
# para cada elemento na lista 'princ':
print('As pessoas mais pesadas foram ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print('As pessoas mais leves foram ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')

