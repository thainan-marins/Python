# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

# Gerando a lista
valores = list()
# declarando as variáveis
maior = menor = 0
# fazendo o laço para perguntar 5 vezes ao usuário
for v in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    # verificando se o primeiro número é o maior
    if v == 0:
        # neste comando o '[v]' indica o indice do número que o 'maior' e 'menor' receberá em 'valores'
        # ex: [1, 2, 3, 4, 5] → maior = valores[v] → maior = valores[0] → maior = 1
        maior = menor = valores[v]
    # se o primeiro número não for o maior nem o menor..
    else:
        # se '[v]' for maior que o valor incial, então 'maior' receberá '[v]'
        if valores[v] > maior:
            maior = valores[v]
        # se '[v] for menor que o valor inicial, então menor recebe [v]'
        if valores[v] < menor:
            menor = valores[v]
    # adicionando os números a lista

print(f'Você digitou o valores {valores}')
# mostramos o valor e, o end='' no final serve para que o valores aparecem um após o outro
print(f'O maior número é {maior} na(s) posição(ões): ', end='')
# fazendo o laço para achar a posição do número maior
for c, n in enumerate(valores):
    # aqui verificamos se 'n' for igual a maior
    if n == maior:
        # se sim, então é o numero que queremos, dizemos então para printar o seu índice
        # e damos um end=' ' para o próximo número aparecer logo em seguida
        print(c, end=', ')
# este print em vazio serve para quebrar a linha após o comando acabar
print()
# mostramos os valores
print(f'O menor número é {menor} na(s) posição(ões): ', end='')
# desta vez fazemos o laço, mas é para verificar o índice do menor valor
for c, n in enumerate(valores):
    # caso 'n' seja o menor..
    if n == menor:
        # printamos seu índices.
        print(c, end=', ')
print()
