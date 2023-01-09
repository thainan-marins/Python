# Neste programa iremos fazer a análise de uma string para descobrir quantos "A" existe na frase

# criamos o dicionário de cores
c = {'l': '\033[m', 'r': '\033[35m', 'b': '\033[4;97m', 'i': '\033[3;97m'}
# recebemos pedimos os dados ao usuário, se não dissermos o tipo primitivo o input sempre retornará uma string
# aqui a formatamos para ficar sem epaços e em letras minúsculas
frase = input('Digite uma frase qualquer e contarei quantos "A" ela tem!: ').strip().lower()
# no método .format já utilizamos as ferramentas para contar quantas vezes a letra 'a' aparece
# com outro método o count()
print('{}> A letra {}A{}{} aparece {}{}{} vezes'.format(c['i'], c['b'], c['l'], c['i'], c['r'], frase.count('a'), c['i']))
# neste dizemos onde a letra "A" aparece pela primeira vez e utilizamos o método find()
print('{}> Ela aparece pela primeira vez na posição {}{}{}'.format(c['i'], c['r'], frase.find('a')+1, c['l']))
# e também na última posição com o rfind() que irá verificar da direita (right) para esquerda.
print('{}> E pela última vez na posição {}{}{}'.format(c['i'], c['r'], frase.rfind('a')+1, c['l']))



