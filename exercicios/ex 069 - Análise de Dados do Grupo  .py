# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# iniciamos as variáveis que iremos trabalhar
maiores = 0
homens = 0
jovens = 0

# criamos um laço infinito
while True:
    # perguntamos ao usuário sua idade e sexo
    idade = int(input('Qual sua idade? '))

    # inicializmos a variável gênero e crimos um laço para que o usuário não digite algo que não seja o esperado
    genero = ' '
    # enquanto não estiver 'm' ou 'f' em 'genero':
    while genero not in 'mf':
        genero = str(input('Qual seu sexo? [M/F] ')).strip().lower()[0]

    # fazemos o mesmo que anteriormente, o programa irá perguntar até obter a resposta certa
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quar continuar? [S/N] ')).strip().lower()[0]

    # como isto é uma análise criamos as condições para averiguá-las

    # 'Se for uma mulher e sua idade for menor que 20, conte +1
    if genero == 'f' and idade < 20:
        jovens += 1

    # 'Se o usuário tiver mais de 18 anos, conte +1
    if idade > 18:
        maiores += 1

    # 'Se for um homem, conte +1
    if genero == 'm':
        homens += 1

    # Se o usuário digitar que não quer continuar, encerre o programa (novamente, é importante a posição onde se poem o
    # break, ele pricisa estar aqui para que todos os dados possam ser atribuído as variáveis antes de o programa
    # encerrar).
    if resposta == 'n':
        break

# Fazemos estes prints para dizer que o programa está finalizado
print('=-' * 11)
print('Fim do cadastramento.')
print('=-' * 11)
print(f'{maiores} pessoas com mais de 18 anos; \n{homens} homens foram cadastrados; \n{jovens} mulheres tem menos de 20 anos.')


