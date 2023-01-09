# neste programa o intuito é criar uma tabuada, (neste momento ainda não haviamos estudo laços)

# aqui estamos importando dois métodos da biblioteca pygame
from pygame import mixer, event
# e aqui somente o método sleep
from time import sleep
# damos início a ele...
mixer.init()
# recebemos a entrada de dados inteiros
n = int(input('Digite um número: '))
# apenas um charme ao programa
print('\033[1;97mCALCULANDO...')
# estes métodos servem para importar a musica para o programa
mixer.music.load('sons/tambores.mp3')
# este a faz tocar
mixer.music.play()
# isto fará o computador 'dormir' por 4 segundos
sleep(4)
# novamente necessário para dar início a musica
print()
# dicionário de cores
c = {'v': '\033[31m', 'l': '\033[m', 'a': '\033[94m', 've': '\033[32m'}
# os prints a seguir mostrarão em forma tabular a tabuada, feita com cores
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 1, c['ve'], n*1))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 2, c['ve'], n*2))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 3, c['ve'], n*3))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 4, c['ve'], n*4))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 5, c['ve'], n*5))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 6, c['ve'], n*6))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 7, c['ve'], n*7))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 8, c['ve'], n*8))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 9, c['ve'], n*9))
print('{}{} {}X {}{:2} {}= {}'.format(c['a'], n, c['v'], c['a'], 10, c['ve'], n*10))
input()




