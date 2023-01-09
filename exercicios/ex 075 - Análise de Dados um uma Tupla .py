# : Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# primeiramente iremos ler os números pelo teclado, como queremos estes números em uma tupla, colocamos o input dentro
# da tupla
tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print('-==-' * 9)
# este programa acaba se tornando bem simples pois é possível fazê-lo usando métodos
# o método count() serve para literalmente contar
print(f'O valor 9 aparece {tupla.count(9)} vezes.')
# aqui criamos a condição, se 3 estiver na viável tupla,
if 3 in tupla:
    # mostre a posição em que ele aparece, usamos o método index()
    print(f'O valor 3 aparece inicialmente na {tupla.index(3)}ª.')
# agora, se não houver...
else:
    # ignore
    pass
print('Os valores pares digitados foram: ', end='')
# para verificar se há ou não um número par na tupla, criamos um laço, ele irá verficar cada elemento da tupla
for e in tupla:
    # e, SE o resto da divisão de 'e' por 2 for igual a 0, ou seja, se 'e' for par
    if e % 2 == 0:
        # mostre o 'e'
        print(e, end=' ')

# CORREÇÃO DO EXERCÍCIO
