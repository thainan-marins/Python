# Faça um programa que leia um número inteiro e diga se ele é ou
# não um número primo.

# os número primos são aqueles que só são divisíveis por 1 e por ele mesmo
n = int(input('Digite um valor: '))
count = 0
# criamos um laço para fazer a verificação de todos os números até chegar no valor digitado pelo usuário
for c in range(1, n+1):
    # se no número for divisível pelo c:
    if n % c == 0:
        # esse comando de print irá dar a cor ao número no terminal, este em específica deixará verde
        print('\033[32m', end='')
        # o contador irá contar +1
        count += 1
    else:
        # e este deixará vermelho, indicando que não foi divisível
        print('\033[31m', end='')
    # então mostramos na tela nos número, usamos o end=' ' para que eles não pulem de linha
    print(c, end=' ')
print('\n\033[mO número {} é divisível {} vezes'.format(n, count))
# se o contador for igual a zero significa que ele só foi divisível por 1 e ele mesmo, assim sendo ele é um número primo
if count == 2:
    print('Por isso ele É um número PRIMO.')
# se não, ele pode ter sido dividido mais ou menos vezes e já não seria um número primo
else:
    print('Por isso ele NÃO é um número PRIMO.')
