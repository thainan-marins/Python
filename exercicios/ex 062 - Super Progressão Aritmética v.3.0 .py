# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

# como no exercício anterior pedimos os valores ao usuário
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão:'))

# inicializamos as variáveis aqui, para podermos trabalhar com elas mais tarde
contador = 1
mais = 10
total = 0

# crimos este laço: enquanto 'mais' for diferente de 0, ou seja, quando o usuário disser que quer mostrar 0 termos
# o laço ira acabar
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo, end=' → ')
        termo += razao
        contador += 1
    print('Pausa;')

    # este comando é o que diferencia o ex 61 deste ex
    mais = int(input('Quantos termos deseja mostrar a mais? '))

# por fim mostramos na tela quantos termos foram mostrados
print('Programa finalizado com {} termos'.format(total))
