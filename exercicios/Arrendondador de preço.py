from math import ceil
from time import sleep
valor = 0
soma = 0
while True:
    resposta = ' '
    valor = float(input('Qual é o valor do produto? '))
    soma += ceil(valor)
    print('-=-' * 10)
    print(f'Valor atual: ${soma:.2f}')
    print('-=-' * 10)
    while resposta not in 'sn':
        resposta = input('\nDeseja continuar? [S/N]')[0].lower()
    if resposta in 'n':
        break
print('Finalizando...')
sleep(1.5)
print('Fim do programa!')
print('-=-' * 5)
print(f'O valor total dos produtos foram de ${soma:.2f}.')

