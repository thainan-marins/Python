# Neste programa iromos, ao invés de sortear apenas um aluno, sortearemos uma sequência aleatória de alunos
# então importamos da biblioteca random o método 'shuflle' que serve para embaralhar uma lista
from random import shuffle
# pedimos ao usuário pele teclado os nomes no tipo string
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
# criamos a lista para poder embaralha-los
# como o 'random' sorteia números, prcisamos colocalos em uma sequência, pois ele não sorteiaria, por exemlo, uma string
lista = [n1, n2, n3, n4]
# fizemos o dicionário de cores
c = {'an': '\033[35m', 'l': '\033[m'}
# este foi apenas um experimento
n = ['Marcelinhu', 'Priksnov', 'Abruti', 'Cratus'] # esses nomes são bem legais ☺
# O método pega uma sequência, como uma lista, e reorganiza a ordem dos itens.shuffle()
# Nota: Este método altera a lista original, não retorna uma nova lista.
shuffle(lista)
print('A ordem de alunos para apresentação será...')
# por fim mostramos na tela o valores.
print('{}{}{}'.format(c['an'], lista, c['l']))

