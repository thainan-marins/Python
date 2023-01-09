# Crie um programa que faça o computador jogar Jokempô com você!

# Como este é um jogo de sorteios, importamos da bilioteca random o método choice, que sorteia itens numa lista
from random import choice
# Já este método é para dar mais plástica ao programa
from time import sleep
# criamos um dicionário de cores
c = {'l': '\033[m', 'v': '\033[0;97;41m', 'al': '\033[1;31m', 's,v': '\033[1;3;91m',
     'a': '\033[1;94m', 've': '\033[1;92m', 'n': '\033[1;97m', 'i,a': '\033[3;93m',
     'ci': '\033[1;37m', 'c': '\033[1;96m', 's,p': '\033[1;3;30m'}
print('{}Vamos jogar Jokenpô?'.format(c['n']))
sleep(1.5)
# e perguntamos ao usuário o que ele escolhe, formatamos a resposta para eviar erros
r = str(input('O que você escolhe? '.format(c['l']))).strip().title()
# então criamos a lista que contém as jogadas do computador
ppt = ['Pedra', 'Papel', 'Tesoura']
# queremos que o usuário escolha somente entre as três opções, para isto criamos esta condição
if 'Pedra' in r or 'Papel' in r or 'Tesoura' in r:
    print('E eu escolho...{}'.format(c['n']))
    sleep(1)
    print('{}JO...'.format(c['i,a']))
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO!{}'.format(c['l']))
    print('{}-{}'.format(c['n'], c['l']) * 15)
    sorteio = choice(ppt) # nesta variável já está o que o cumputador escolheu
    # mostramos na tela o que ele escolheu
    print('{}> {}{}'.format(c['s,v'], sorteio, c['l']))
    print('{}-{}'.format(c['n'], c['l']) * 15)
    # agora teremos de ver que ganhou e quem perdeu
    # a partir de agora criamos uma condição para cada jogada realizada, analisando as três opções
    if r != sorteio and sorteio == ppt[0] and r == ppt[1]:
        print('{}Parabéns! Você venceu.'.format(c['a']))
    elif r != sorteio and sorteio == ppt[0] and r == ppt[2]:
        print('{}Oba! Eu venci.'.format(c['ve']))
    elif r != sorteio and sorteio == ppt[1] and r == ppt[0]:
        print('{}Oba! Eu venci.'.format(c['ve']))
    elif r != sorteio and sorteio == ppt[1] and r == ppt[2]:
        print('{}Parabéns! Você venceu.'.format(c['a']))
    elif r != sorteio and sorteio == ppt[2] and r == ppt[0]:
        print('{}Parabéns! Você venceu.'.format(c['a']))
    elif r != sorteio and sorteio == ppt[2] and r == ppt[1]:
        print('Oba! Eu venci.'.format(c['ve']))
    else:
        print('{}Ops! Deu empate.'.format(c['ci']))
# se o usuário não dizer pedra, papel ou tesoura o programa irá avisar.
else:
    print('{}Hm, não tem essa opção para jogar!'.format(c['al']))
