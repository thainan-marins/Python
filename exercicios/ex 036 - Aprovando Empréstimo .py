# ENUNCIADO:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.

# Aqui importamos da biblioteca math o método ceil, que é responsável por arredondar valores para cima
from math import ceil
# dividir a viriável 'valor' pela variável 'anos' para saber o valor da parcela
# pedimos ao usuário um valor float com se trata de dinheiro
valor = float(input('Qual o valor da casa? R$'))

# tirar a porcentagem da variável 'salario' para saber qual o limite da parcela
# pedimos ao usuário um valor float com se trata de dinheiro
salario = float(input('Qual a quantia do seu salário? R$'))

# multiplicar a variável 'anos' por 12 para saber quantos meses serão necessarios para dividi-la pela variável 'valor'
# mas em anos pedimos um valor inteiro
anos = int(input('Em quantos anos deseja financiar? :'))

# para saber quantas parcelas o usuário terá de pagar multiplicamos os anos por 12, assim teremos a quantidade de meses
meses = anos * 12
# agora dividimos o valor da casa para saber o valor de cada parcela
parcela = valor / meses
# como o valor da parcela não pode passar de 30% do valor de salário do usuário, calculamos nesta variável
porcentagem = salario / 100 * 30
# multiplicar a variável 'porcentagem' pela variável 'parcela' para saber o valor mínimo de parcelas para o usuário
# criei esta variável para saber o valor máximo da parcelas que o usuário poderia fazer
parmin = valor / porcentagem
# comdição composta: se a parcela for maior que a porcentagem, usuário não poderá comparar a casa
if parcela > porcentagem:
    print('Você não pode financiar essa casa.')
# se não, se o valor for menor, o usuário poderá comprar a casa
else:
    print('Você pode financia esta casa!')
# neste print mostramos todas as informações geradas anteriormente: quantidade de parcela e seu valor, quantidade mínima
# de parcelas a serem feitas e seu valor.
print('Serão {:.0f} parcelas no valor de R${:.2f}. Você pode finacia-la em até {} parcelas de R${:.2f}'
      .format(meses, parcela, ceil(parmin), porcentagem))



