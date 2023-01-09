# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

# Aqui criamos uma lista vazia
valores = list()
# fazemos um laço infinito
while True:
    # e pedimos um número para o usuário
    num = int(input('Digite algum número para registro: '))
    # verficamos então, SE 'num' não estiver em 'valores'
    if num not in valores:
        # adicione 'num' em 'valores'
        valores.append(num)
        # mostre na tela a ação
        print('Valor adicionado!')
    # SENAO
    else:
        # mostre um mensagem dizendo que não foi possivel
        print('Valor duplicado, tente novamente.')
    # iniciamos esta variável aqui para podermos fazer uma verificação com o while depois
    resposta = ' '
    # enquando 'resposta' não está em 'sn'
    while resposta not in 'sn':
        # o programa irá continuar perguntado ao usuário
        resposta = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    # se o usuário digitar sim
    if resposta in 's':
        # o programa continua
        continue
    # se ele digitar não
    else:
        # o laço é interrompido
        break
# com o método sort() colocamos a lista valores em ordem crescente
valores.sort()
# mostramos na tela quais valores foram digitados e já em ordem crescente
print(f'Os valores únicos digitados foram: {valores}.')
# e por fim dizemos que o programa se finalizou!
print('Fim do programa.')

