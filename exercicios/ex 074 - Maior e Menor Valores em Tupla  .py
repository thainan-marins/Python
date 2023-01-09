# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

# para sortear número, usamos a biblioteca random
from random import randint
# variáveis para calcular o maior e menor valor
maior = menor = 0
# para colocar vários números aleatórios em uma tupla, basta colocar, por exemplo, 5 sorteios com o método randint
numeros = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
# um contador
cont = 0
# cria uma laço para pegar um único elemento da tupla números
for n in numeros:
    # poderíamos mostrar na tela apenas dando print na variável numeros, mas para ficar mais bonito, fazemos este laço
    # para aperecer um na frente do outro
    print(f'\033[32m{n}\033[m', end=' ')
    cont += 1
    # se o contador for igual a 1, ou seja, se for o primeiro laço
    if cont == 1:
        # maior e menor recebe o valor de 'n'
        maior = menor = n
    else: # se não, se o valor de 'n' for maior que o maior valor, 'maior' recebe o novo valor de 'n'
        if n > maior:
            maior = n
        # E se 'n' for menor que o menor valor, 'menor' recebe o novo valor de 'n'
        if n < menor:
            menor = n
print()
print('\n\033[3m1ª opção:\033[m')
# Por fim mostre na tela
print(f'O maior valor foi {maior}.\nO menor valor foi {menor}.')
# Fim

# ISSO TAMBÉM PODE SER FEITO COM UMA FUNÇÃO INTERNA DA TUPLA, O "max()" E O "min()".
# (TAMBÉM PODE SER UTILIZADA EM OUTROS LUGARES).
print()
print('\033[3m2ª opção:\033[m')
print(f'O maior valor foi {max(numeros)}.')
print(f'O menor valor foi {min(numeros)}.')



