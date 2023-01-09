# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média.


dados = {}
geral = []
tot = cont = 0
mulheres = []
velho = []

# Criei um laço infinito com uma condição de parada
while True:
    # colocamos a variável dentro do laço para que ele possa ser resetada cada vez que precise fazer a pergunta
    resposta = ' '
    # adicionamos os dados no dicionário
    dados['nome'] = str(input('Nome: '))
    # criamos uma verificação para que o usuário digite somente o sexo
    while resposta not in 'mf':
        dados['sexo'] = str(input('Sexo [M/F]: '))[0].lower()
        resposta = dados['sexo']
    # adicionamos mais dados ao dicionário
    dados['idade'] = int(input('Idade: '))
    # somamos todas as idades
    tot += dados['idade']
    # fazemos a contagem do laço
    cont += 1
    # fazemos a cópia dos dados do dicionário para a lista
    geral.append(dados.copy())
    # limpamos os dados que estavam no dicionário
    dados.clear()
    # verificamos se o usuário irá continuar
    while resposta not in 'sn':
        resposta = str(input('Deseja cadastrar outra pessoa? '))[0].lower()
    if resposta in 'n':
        break
# aqui pegamos a média de idade das pessoas cadastradas
media = tot/cont
print('\nPrograma finalizado!')
print(f'\nForam cadastradas {len(geral)} pessoas.')
print(f'A média de idade destas pessoas é de {media:.0f} anos.')
# para extrair algum valores colocamos a lista em um laço for
for m in geral:
    # a variável 'm' contém o dicionário da lista 'geral'
    if m['sexo'] in 'f': # se a chave 'sexo' tiver o valor de 'f', ou seja, se for uma mulher
        mulheres.append(m['nome']) # adicionamos seu nome para a lista

# precisamos mostrar isto, porém para ficar bonito usamos outro laço for
print(f'As mulheres cadastradas foram: ', end='')
# para cada elemento na lista 'mulheres'. 'n' tem o valor de cada nome
for n in mulheres:
    # se for o último nome da lista
    if n == mulheres[-1]:
        print(n, end='') # imprima o nome e mais nada

    # se não for o penúltimo nome da lista
    elif n != mulheres[-2]:
        print(n, end=', ') # imprima o nome mais uma vírgula

    else: # caso contrário, ou seja, se for o penúltimo nome da lista
        print(n, end=' e ') # imprima na tela o nome mais 'e'

# para cada elemento na lista 'geral'
for i in geral: # ele irá retornar um dicionário
    # se o valor da chave ['idade'] for maior que a idade média
    if i['idade'] > media:
        # adicione o nome a lista 'velho'
        velho.append(i['nome'])

# novamente iremos usar o laço for para mostrá-los
print('\nAs pessoas que estam com a idade acima da média são: ', end='')
# para cada elemento na lista, irá retornar o nome dentro dela
for e in velho:
    # se o for o último nome
    if e == velho[-1]: # mostre ele e mais nada
        print(e, end='')
    # se não for o penúltimo nome
    elif e != velho[-2]: # mostre ele e mais uma vírgula
        print(e, end=', ')
    # se não, ou seja se ele for o penúltimo número
    else:
        print(e, end=' e ') # mostre ele e mais um 'e' no final

print('''

Fim.''')



