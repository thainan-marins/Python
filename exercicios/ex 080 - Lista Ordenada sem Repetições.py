# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Ininiamos um lista (ela também pode ser inicializada assim list().)
lista = []
# criamos um laço que vai de 0 a 5
for c in range(0, 4):
    n = int(input('Digite um número: '))
    # SE 'c' for igual a zero, ou seja, se for o primeiro elemento
    # OU se 'n' for maior que o último elemento da lista
    if c == 0 or n > lista[-1]:
        #adicionaremos o valor que o usuário digitou (n) na lista (valor).
        # * o método append() adiciona tudo ao final da lista
        lista.append(n)
    # Se não
    else:
        # iniciamos a variável
        pos = 0
        # aqui estamos varrendo a lista procurando onde colocar o número
        # com este laço verficamos todos os números que estão na lista
        while pos < len(lista): # eu vou verificar em cada posição, se o número que eu quero adicionar é maior ou igual
            # a ele, se ele for menor ou igual, eu vou inseri-lo em uma posição específica
            if pos <= lista[pos]:
                # o método insert() permite inserir valores em posições específicas
                lista.insert(pos, n)
                break
            pos += 1
print(lista)

# CORREÇÃO DO EXERCÍCIO
