# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# inicializamos as vaiázeis
total = 0
caro = 0
menor = 0
cont = 0

# também iniciamos uma variável aqui, mas desta vez ela receberá um dado tipo str (string)
pronome = ' '

# criamos um laço infinito
while True:
    # recebemos um entrada de dados do tipo str (frase)
    nome = str(input('Qual o nome do produto? '))
    # float (números com vírgulas)
    valor = float(input('Qual o preço do produto? '))
    # aqui também uma string
    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    # criamos uma verificação aqui, se a resposta não for sim ou não, o programa irá continuar perguntando
    while resposta not in 'sn':
        resposta = str(input('Quer continuar? [S/N] '))
    # nesta variável estamos somando todos os valores que o usuário digitar
    total += valor
    # este é um contador de laços
    cont += 1
    # outra condição, se valor for maior que 1000
    if valor > 1000:
        # soma-se 1 a variável 'caro'
        caro += 1
    # iremos verificar qual valor é maior e o menor
    # se for o primeiro laço, ou o valor for menor que 'menor'
    if cont == 1 or valor < menor:
        # a variável menor recebe o 'valor'
        menor = valor
        # a variável 'pronome' está aqui porque queremos também o nome do produto mais caro, então quando o valor de
        # algum produto entrar na variável  'menor', o nome também será coletado
        pronome = nome
    '''else:
        if valor < menor:
            menor = valor
            pronome = nome'''
    # esta é a condição de parada, se o usuário digitar não, o programa se encerrará
    if resposta == 'n':
        break

print('')
# e pro fim mostramos na tela os valores na tela conforme se pede no enunciado
print(f'> O produto mais barato é o {pronome} de R${menor:.2f}.')
print('-' * 30)
print(f'> O total gasto foi de R${total:.2f}.')
print('-' * 30)
print(f'> {caro} produtos custam mais de R$1000.')
