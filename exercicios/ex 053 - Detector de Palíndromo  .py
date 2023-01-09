# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.

# Perguntamos ao usuário a frese que deseja analisár
frase = input('Digite uma frase qualquer: ').strip().upper() # o strip() vai tirar os espaços da frase e upper vai
# colocar tudo em maiúsculo
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''
#inverso = [::-1]
#podemos também fazer desta forma, começamos do começo ':' e vamos até o fim ':', no sentido contrário '-1'
#é um macete para o Python.

# Eu preciso ir da última até a primeira letra, para isso eu pego o
# comprimento de junto len(junto), (se uma palavra tem 20 letras, no índice ela irá do 0 ao 19,
# por isso o comprimento de junto -1 que vai dar o valor do último indice)
# e tiro -1, ou seja, ele vai começar no último índice e irá até a ultima letra, porém o python sempre a
# ignora então para ir até o indice 0 colocamos -1, para invertê-la precisamos ir na ordem inversa,
# então colocamos -1 para que o laço vá contando cada letra no sentido inverso
#for letra in range(len(junto) -1, -1, -1):
for letra in range(len(junto) -1, -1, -1):
    # para juntar todas essas letras na ordem inversa usamos a variável junto que vai receber as letras
    inverso += junto[letra]
print('O inverso da frase {} é {};'.format(frase, inverso))

# então comparamos as duas para saber se elas são palíndromos
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo.')
