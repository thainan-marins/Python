# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final,  mostre uma listagem de preços, organizando os dados em forma tabular.

# como desta vez os dados não serão pegos de um input, podemos colocar o que queremos que esteja na tupla
produtos = 'Celular', 800, 'Monitor', 1200, 'Teclado Me.', 300, 'Mesa p/ Computdor', 500, 'Cadeira Gamer', 1250
# aqui estamos dizendo: comece no índice 1 de 'produtos' e vá até o final pulando de dois em dois
prod = produtos[1::2]
print('_' * 40)
print('{:^40}'.format('*NOTA FISCAL*'))
print('-' * 40)
# este é um laço for um pouco diferente, a primeira variável irá mostrar o índice do laço e a sugundo irá mostrar o
# valor, seja ele um número ou uma string
# neste laço usamos o método enumerate() nele eu digo comece do começo e va até o final pulando de 2 em 2, assim ele irá
# pegar somente os prodrutos da tupla
for tab, pos in enumerate(produtos[::2]):
    # então formatamos os prudutos e mostramos na tela
    # para mostrar os preços, pegamos a variável que criamos apenas com os números anteriormente e falamos para mostrar
    # cada preço em determindo índice do laço, ou seja, se for o primeriro laço, será mostrado o primeiro valor
    print('{:.<30} R$'.format(pos), prod[tab])
# por fim fazemos um print para enfeitar :)
print('-' * 40)