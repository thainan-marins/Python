# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

# inicializamos as variáveis
valor = 0
contador = 0
soma = 0

# este programa terá um 'flag', que é a condição de parada. Criamos o laço com a condição de que se o valor for
# diferente do nosso flag (999), continue recebendo dados
while valor != 999:
    valor = int(input('Digite um número: '))
    # aqui fazemos a análise para ver se o usuário digitou ou não a condição de parada. Esse comando precisa
    # necessáriamente estar aqui pois se ele estivesse no final, quando o usuário digitasse o flag iria contar como
    # um outro valor quanquer digitado e como queremos a soma dos números não podemos deixar que ele entre na contagem
    if valor != 999:
        contador += 1
        soma += valor
# por fim formatamos a quantidade de números digitados e a soma entre eles
print('Foram digitados {} números e a soma entre eles é {}.'.format(contador, soma))
# O 'Flag' é o 999, que podemos chamar de condição de parada.