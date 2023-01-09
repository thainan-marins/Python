# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

# como no desafio 51, vamos perguntar o termo e razão
termo = int(input('Qual o primeiro termo? ')) #2
razao = int(input('Qual a razão? ')) #2 | decimo termo == 20
count = razao
contador = 1
# 'enquanto o valor de 'contador' for menor ou igaul a 10 (isso daria em um laço infinito, porém como somamos um número
# ao contador sempre que ele passo pelo laço, em algum momento ele chegará ao valor 10
while contador <= 10:
    # mostramos na tela então o valor de termo, end=' → ' serve para mostrar um número na frente do outro de um jeiro
    # mais harmonioso
    print(termo, end=' → ')
    # 'termo' recebe a soma de 'termo' mais a 'razão', isso fará com que cada vez que o laço ocorra o valor vai se somar
    # ao termo, dando assim o próximo valor da PA
    termo += razao
    # por esta variável o ciclo não se torna infinito
    contador += 1
# e por fim quando o laço terminar, mostraremos na tela 'Fim'
print('Fim.')
