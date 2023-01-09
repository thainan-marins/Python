# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

# inicializamos a variáveis
cont = soma = 0

# criamos um laço infinito
while True:
    # pedimos uma entrada de dados ao usuário
    n = int(input('''(999 para parar)
Digite um número: '''))

    # como nossa condição de parada é o 999, se o usuário o digitar será executado o comando 'Break'
    if n == 999:
        break

    # é importante que estas variáveis estejam aqui pois se estivessem antes da condição de parada, o 999 seria somado
    # junto com os outros números assim como iria contar como um número digitado. Elas estando aqui o programa irá se
    # encerrar antes de o valor entrar na variável
    soma += n
    cont += 1

# por fim mostramos na tela.
print(f'Foram digitados {cont} números, a soma entre eles é {soma}.')
