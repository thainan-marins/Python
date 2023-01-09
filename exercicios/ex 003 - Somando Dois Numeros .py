# aqui recebemos outra entrada de dados, porém desta vez está formatado para números inteiros (int)
n1 = int(input('digite um número: '))
n2 = int(input('digite outro: '))
# como queria colorir fiz um dicionário com as cores que iria usar
cores = {'vermelho': '\033[4;32m', 'azul': '\033[4;32m', 'roxo': '\033[1;35m', 'limpa': '\033[m'}
# então criamos a variável responsável por fazer a soma dos números
s = n1 + n2
# printamos com formatação .format e colorido
print('O número {}{}{} mais {}{}{} é igual a {}{}{}!'.format(cores['vermelho'], n1, cores['limpa'], cores['azul'],
                                                      n2, cores['limpa'], cores['roxo'], s, cores['limpa']))
