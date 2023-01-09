# Neste programa iremos escolher um aluno aleatório
# para isto peguei uma biblioteca que gera números aleatórios
import random
# pedimos ao usuário os nomes do aluno, para isto o input será de uma string, por padrão, se você não colocar
# nunhum tipo no input, ele irá gerar uma string
n = input('Qual o do primeiro aluno? ')
n1 = input('Qaul o nome do segundo? ')
n2 = input('Qual o nome do terceiro? ')
n3 = input('Qual o nome do quarto aluno? ')
# esta variável é para o porcentagem
p = (1 / 4 * 100)
# o dicionário
c = {'v': '\033[31m', 's': '\033[1;4;34m', 'l': '\033[m'}
# aqui juntamos todos os valores um uma lista para poder sorteálos depois
lista = [n, n1, n2, n3]
# O método 'choice' retorna um elemento selecionado aleatoriamente a partir da sequência especificada.choice()
# A sequência pode ser uma sequência, um intervalo, uma lista, uma tupla ou qualquer outro tipo de sequência.
sorteado = random.choice(lista)
# por fim mostramos na tela a formatação dos valores, e colorida.
print('O escolhido foi o(a) {}{}{}!'.format(c['s'], sorteado, c['l']))
print('A probabilidade é de {}{:.1f}{}%.'.format(c['v'], p, c['l']))




