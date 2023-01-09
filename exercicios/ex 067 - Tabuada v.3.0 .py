# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# novamente criamos um laço infinito (só podemos fazer isto se colocarmos uma condição de parado ou um comando Break
# depois)
while True:
    # pedimos o valor inteiro ao usuário
    n = int(input('''(Número negativo para encerrar)
    Digite um número: '''))

    # e criamos uma verificação: se 'n' for menor que 0, Interrompa (Break), ou seja, se ele for um número negativo
    if n < 0:
        break

    # aqui usaremos o laço for, pois sabemos o limite e isso nos ajuda muito neste laço. Queremos ir de 1 a 10, então
    # colocamos até 11, o Python sempre ignora o último número
    for c in range(1, 11):
        # aqui formatamos o número que o usuário digitou, o laço de repetição e o produto deles que será o resultado da
        # tabuada
        print(f'{n} X {c:2} = {n*c}')

# fazemos este print para sabermos que o programa acabou.
print('Programa finalizado.')
