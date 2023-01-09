# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de
# pagamento:

# Aqui fazemos um print bonitinho
print('{:=^40}'.format(" MARINS'S LOJAS "))
# pedimos ao usuário o valor do produto
valor = float(input('Qual o valor do produto? R$ '))
# e criamos um menu de opções de pagamento
print('''1 > À vista dinheiro/cheque;
2 > À vista no cartão;
3 > Em até 2X no cartão;
4 > 3X ou mais no cartão.''')
pg = int(input('Qual será o método de pagamento? N°'))
# criamos uma condição para cada meio de pagamento no menu
if pg == 1:
    # a vista recebe desconto, e formatamos isto diretamente nos prints a seguir
    print('O valor total do produto é de R${:.2f}.'.format(valor - (valor / 100 * 10)))
elif pg == 2:
    print('O valor total do produto é de R${:.2f}.'.format(valor - (valor / 100 * 5)))
elif pg == 3:
    print('O produto sirá em 2X de {:.2f} SEM JUROS'.format(valor / 2))
    print('O valor total do produto é R${:.2f}.'.format(valor))
elif pg == 4: # aqui as coisas mudam um pouco, faremos o cálculo de parcelas e seus juro
    # primeiro perguntamos ao usuário quantas parcela deseja fazer
    pa = int(input('Quantas parcelas deseja fazer? '))
    # depois formatamos isto no print
    print('O produto sairá em {}X de {:.2f} COM JUROS'.format(pa, (valor + valor / 100 * 20) / pa))
    print('O valor total do produto é de R${:.2f}.'.format(valor + (valor / 100 * 20)))
else:
    print('\033[31mOpção de pagamento inválida!')
