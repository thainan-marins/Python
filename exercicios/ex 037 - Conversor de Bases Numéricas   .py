#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:

# Pedimos então ao usuário que digite um número inteiro pelo teclado
n = int(input('Digite um número inteiro qualquer: '))
# voce pode usar três aspas (''') para pular de linha sem precisar fazer outro 'print'.
print('''Escolha uma das bases para conversão:
 [1] BINÁRO;
 [2] OCATAL;
 [3] HEXADECIMAL.''')
# criamos um pequeno menu para facilitar as escolhas
opçao = int(input('Sua escolha: '))
# depois é só criar as condições para cada número do menu
if opçao == 1:
    # o python ter seus próprios conversores:
    print('{} em BINÁRIO é {}.'.format(n, bin(n)[3:])) # o bin(), para números binarios
elif opçao == 2:
    print('{} em OCTAL é {}.'.format(n, oct(n)[2:])) # o oct(), para números octais
elif opçao == 3:
    print('{} em HEXADECIMAL é {}.'.format(n, hex(n)[2:])) # e o hex(), para números hexadecimais
# se o usuário não digitar nunhum dos números do menu, o programa irá retornar resposta inválida.
else:
    print('Opção inválida.')
