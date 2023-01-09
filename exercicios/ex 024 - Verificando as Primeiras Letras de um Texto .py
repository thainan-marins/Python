# Criamos o dicionário para as cores
c = {'b': '\033[1;37m', 'su': '\033[4;97m', 'l': '\033[m'}
# pedimos ao usuário uma entrada de dados pelo teclado, uma string
nome = input('Qual o nome da sua cidade? ').strip()
# como faremos uma verificação do que o usuário digitou, formatamos para que os erros sejam diminuidos
min = nome.lower() # deixa todas as letras em minúsculo
ana = 'santo' in min[0:5] # fazemos a verificação se o nome da cidade começa com santo
# criamos a condição de que, se isto for verdadeiro, mostre na tela uma mensagem referente a isto
if ana == True:
    print('{}Que legal, o nome de sua cidade começa com {}"Santo"{}{}!'.format(c['b'], c['su'], c['l'], c['b']))
# se não, apenas elogio o nome da cidade.
else:
    print('{}Sua cidade tem um belo nome!{}'.format(c['b'], c['l']))





