# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.

# para este ununciado precisaremos de três listas
lista = []
lista2 = []
lista3 = []

# criamos um laço infinito
while True:
    # e naturalmente pedimos um valor inteiro ao usuário
    n = int(input('Digite um número: '))
    # todos os valores digitados por ele serão adicionados na primeira lista
    lista.append(n)
    # Mas se o número for divisível por 2
    if n % 2 == 0:
        # ele será adicionado na 'lista2'
        lista2.append(n)
    # E se ele for ímpar será adicionado na lista 3
    elif n % 2 == 1:
        lista3.append(n)

    # Sempre que o usuário digitar um número o programa irá perguntar se ele quer ou não continuar. O programa não irá
    # aceitar outra resposta como válida
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quer continuar? [S/N] ')).strip().lower()

    # SE ele responder 'sim', o laço continua
    if resposta in 's':
        continue

    # SENÃO o laço é interrompido
    elif resposta in 'n':
        break

# Por fim mostramos todos os valores na tela.
print(f'''Todos os valores: {lista};
Os valores pares: {lista2};
Os valores ímpares: {lista3}.''')
