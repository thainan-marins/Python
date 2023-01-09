# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# inicializamos a lista
lista = []
# e também duas variáveis de string
esta = ' '
nesta = ' '

# criamos um laço infinito, logo depois há sua condição de parada
while True:
    # iremos pedir ao usuário um valor e adicioná-lo na lista
    lista.append(int(input('Digite um valor: ')))

    resposta = ' '
    # aqui fazemos a verificação se o usuário digitou 'sim' ou 'não'. O programa não irá aceitar outra resposta como
    # válida
    while resposta not in 'sn':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().lower()

    # se o usuário digitar 'sim', o laço continua
    if resposta in 's':
        continue
    # se ele digitar 'não' o laço é interrompido
    elif resposta in 'n':
        break

# o método sort por padrão, organiza o valores de forma crescente (menor para o maior), mas também é possível fazer o
# inverso, usando-o com o parâmetro 'reverse=True', assim o valores ficaram em ordem decrescente
lista.sort(reverse=True)
# mostramos na tela o comprimento da 'lista' com o método len()
print(f'Foram digitados {len(lista)} valores.')
# e a lista em ordem descrencente, como já havíamos feito antes
print(f'A lista em ordem descrescente: {lista}.')
# o ununciado também pede para verificar se há ou não o número 5 na lista. Criamos a condição seguinte:
# SE 5 estiver na 'lista'
if 5 in lista:
    # mostre na tela:
    print('O valor 5 está na lista.')
else:
    # SE NAO, mostre na tela:
    print('O valor 5 não está na lista.')


