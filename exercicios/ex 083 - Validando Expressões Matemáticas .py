# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# primeiramente pedimos ao usuário um valor
e = str(input('Digite alguma expressão numérica: '))
# inicializamos uma lista
lista = []
# criamos um laço for para verificar os elementos da variável 'e'
for simb in e:

    # se tiver parênteses em 'simb'
    if '(' == simb:
        # adicine-o  na lista
        lista.append(simb)

    # *todo* O que fizemos aqui foi: se o usuário abrir um parênteses, a lista terá o tamanho de 1, ou seja, maior que 0
    # *todo* Então, se o usuário fechar este parêntese: elif ')' == simb; e a lista for maior que zero (o parênteses já
    # *todo* estava aberto) apague o valor da lista, assim ela fica igual a zero e os parênteses ficam fechados
    #  mesmo vale para o parênteses contrário
    elif ')' == simb:
        if len(lista) > 0:
            # o método pop() serve para apagar o último elemento da lista
            lista.pop()

        # *todo* Porém se estiver apenas o parênteses que fecha, a lista ficará com valor == 1 e o laço se encerra
        else:
            lista.append(')')
            break

# Se a lista finalizou vazia, significa que todos os parênteses abertos foram fechado
if len(lista) == 0:
    print('Sua expressão está correta.')
# Mas se ela for > que 0, significa que parênteses ficaram abertos, logo a expressão está incorreta
else:
    # mostramos isso na tela e finalizamos o programa.
    print('Sua expressão está incorreta.')
