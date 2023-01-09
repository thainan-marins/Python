# fizemos a atribuição de uma entrada de dados a uma variável, porém desta vez o valor é float(ponto flutante)
n = float(input('Quantos metros deseja converter?  '))
# este é o dicionario de cores para o terminal
c = {'ne': '\033[1;4;7;97m', 'l': '\033[m'}
# aqui mostraremos o número que o usuário digitou
print('{}{}{} metros são:'.format('\033[1;97m', n, c['l']))
print('')
# neste sequência de prints mostraremos a conversão do número para diferentes grandezas usando apenas operadores
# matemáticos e códigos de cores.
print('{}> {:.3f} QUILÔMETROS;{}'.format(c['ne'], n/1000, c['l']))
print('{}> {:.3f} HECTÔMETROS;{}'.format(c['ne'], n/100, c['l']))
print('{}> {:.3f} DECÂMETROS;{}'.format(c['ne'], n/10, c['l']))
print('{}> {:.3f} DECÍMETROS;{}'.format(c['ne'], n*10, c['l']))
print('{}> {:.3f} CENTÍMETROS;{}'.format(c['ne'], n*100, c['l']))
print('{}> {:.3f} MILÍMETROS.{}'.format(c['ne'], n*1000, c['l']))








