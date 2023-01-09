# O objetivo deste programa é ler o nome do usuário, se tiver Silva em seu nome iremos comprimentá-lo
# se não iremos apenas dar um Bom Dia.

# Criamos o dicionário de cores
c = {'a': '\033[34m', 've': '\033[32m', 'l': '\033[m'}
# pedimos uma entrada de uma string, deixamos isto explícito ao formatar o tipo primitivo antes do input
nome = str(input('\033[1mQual o seu nome completo? ')).strip().title() # aqui deixamos a variável formatada sem
# sem espaços e todas as palavras com sua primeira letra em maiúsculo
m = nome.lower() # nesta variável o nome está com todas a letras em minúculo
# na variável 'tf', com a ferramenta 'in' fazemos a verificação se 'silva' estará na variável m
tf = 'silva' in m
# nesta variável dividimos o nome, formando uma lista
div = nome.split()
if tf == True: # Se a variável tf for verdadeira:
    print('{}Olá Sr.Silva, que prazer em te ver!'.format(c['ve']))
else: # se não:
    # neste print usamos também o método len() para formatar o último nome do usuário.
    print('{}Bom dia Sr.{}, como vai?{}'.format(c['a'], div[len(div)-1], c['l']))




