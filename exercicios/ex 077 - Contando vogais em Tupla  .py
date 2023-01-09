# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

# criamos então a tupla com as palavras que queremos analisar
palavras = ('gratidao', 'esperança', 'fe', 'liberdade', 'perdao', 'respeito', 'amor', 'paz', 'felicidade', 'reciprocidade',
           'amanhecer', 'autenticidade', 'arte')
# definimos quais são a vogais, colocando-as numa variável
vogais = ('a', 'e', 'i', 'o', 'u')
# criamos um laço, para cada item na tupla, ou seja para cada palavra
for x in palavras:
    # mostramos na tela a palavra
    print(f'\nNa palavra {x.upper()} temos as vogais: ', end='')
    # então criamos outro laço, para cada item na palavra, ou seja, para cada letra
    for y in x:
        # verificamos, se em y tiver a, e, i, o ou u
        if y.lower() in 'aeiou':
            # mostre-os na tela
            print(f'\033[93m{y}\033[m', end=' ')
# por fim fazemos um print dizendo que o programa está finalizado
print('acabou')
