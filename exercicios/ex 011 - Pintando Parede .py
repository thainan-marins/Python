# aqui teremos dois inputs de valores float, queremos calcular quanta tinta será necessário para pintar uma certa
# parede
altura = float(input('Qual é a altura? '))
largura = float(input('Qual é a largura? '))
# dicionário de cores
c = {'c': '\033[4;36m', 'l': '\033[m'}
# aqui multiplicamos a variáveis para ter o valor quadrado da parade
area = altura * largura
# no enunciado cada litro de tinta pinta 2 metros quadrados, então dividimos por 2
tinta = area/2
# formatamos os valores e mostramos na tela.
print('A área da parede é de {}{}m²{} e será preciso {}{}L{} de tinta para pintá-la.'
      .format(c['c'], area, c['l'], c['c'], tinta, c['l']))
