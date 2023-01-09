# usamos a função 'input' para receber a entrada de dados, que neste exemplo o é uma string, mas pode ser vários outros
# tipos de valores
nome = input('digite seu nome... ')
# por fim usamos a função 'print' para mostrar na tela e, o tipo de formatação é  o .format com códigos de cores
print('É um prazer te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
