# Este conversor será de graus Célcios para Farenheit
# pedimos ao usuário um valor float(ou não) pelo teclado
celsius = float(input('Quantos graus está fazendo? °C '))
# pesquisando na internet se acha a fórmula para o cálculos destea conversão
conv = celsius * 1.8 + 32
# dicionário para colorir o terminal
c = {'i': '\033[1;3m', 'f,v': '\033[41;97m', 'f,a': '\033[44;97m', 'l': '\033[m'}
# por fim mostramos na tela a formatção com cores e as repectivas variáveis
print('{}{} {}°C{}{} equivalem a {} {}°F{}{}!'.format(c['i'], celsius, c['f,a'], c['l'], c['i'],
                                                      conv, c['f,v'], c['l'], c['i']))
