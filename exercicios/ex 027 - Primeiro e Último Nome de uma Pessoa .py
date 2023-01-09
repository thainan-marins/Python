# Neste programa iremos pedir o nome do usuário e diremos qual é seu primeiro e último nome.

# Criamos novamente o dicionário de cores
c = {'l': '\033[m', 'ci': '\033[1;97;100m', 'n': '\033[1m', 'su': '\033[4m'}
# pedimos ao usuário uma string pelo teclado
n = input('{}Digite seu nome completo:{} '.format(c['ci'], c['l'])).strip().title()
# dividimos o nome com o método split() criando uma lista com os elementos da variável
d = n.split()
# agora mostramos na tela o primeiro elemento da lista, que será o primeiro nome
print('{}Seu primeiro nome é: {}{}{}'.format(c['n'], c['su'], d[0], c['l']))
# e o último utilizamos o -1 para mostrá-lo como não sabemos o comprimento da lista, pois -1 sempre será o último
# elemento de uma lista.
print('{}Seu último nome é: {}{}{}'.format(c['n'], c['su'], d[len(d)-1], c['l']))


