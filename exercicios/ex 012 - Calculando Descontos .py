# Neste programa calcularemos a porcentagem do valor de um certo produto
# pedimos ao usuário um valor float através do input
preço = float(input('qual é o preço do produto? '))
# para calcular a porcentagem fiz uma operação matemática simples
porc = preço/100*5
# como será uma porcentagem de desconto, subitraímos as variáveis
resu = preço - porc
# então mostramos na tela formatado, com cores.
print('''\033[7;35;107m O preço do produto com desconto sairá 
\033[7;4;35;107m R${:.2f}\033[0;7;35;107m !!! \033[m'''.format(resu))

# A diferença deste programa para o outro é que, somente adicionamos mais funções, além de dispensar uma variável
'''valor = float(input('qual o valor do produto? R$ '))
desc = valor / 100 * 10
print('Com um desconto de R${:.2f} ou 10%, o produto a vistá sairá R${:.2f}.'.format(desc, valor - desc))
desc1 = valor / 100 * 5
# neste exemplo calculamos um juro ao usuário
print('Com um acréscimo de R${:.2f} ou 5%, o produto a prazo sairá R${:.2f}.'.format(desc1, valor + desc1))'''


