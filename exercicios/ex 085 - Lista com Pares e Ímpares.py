# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma única lista que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

valor = [[], []]

num = 0
for v in range(0, 7):
 num = int(input('Digite um valor: '))
 if num % 2 == 0:
  valor[0].append(num)
 else:
  valor[1].append(num)

print('-=-' * 11)
valor[0].sort()
valor[1].sort()
print(f'Os valores pares são: {valor[0]}')
print(f'Os valores ímpares são: {valor[1]}')


