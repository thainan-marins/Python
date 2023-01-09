# Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de
# cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

general = list()
dados = []
while True:
    dados.append(str(input('Qual é o nome? ')))
    dados.append(float(input('Qual é a nota? ')))
    dados.append(float(input('Qual é a segunda nota? ')))
    general.append(dados[:])
    dados.clear()
    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja continuar? S/N ')[0].lower()
    if resposta == 'n':
        break
print('\n{:-^40}'.format('BOLETIM DOS ALUNOS'))
cont = 0
for c in general:
    print(f'[{cont}] {c[0]:<15}', end='   ')
    cont += 1
    print(f'MÉDIA: {(c[1] + c[2]) / 2}')
while True:
    nota = int(input('\nDeseja mostrar as médias de qual aluno? (999 interrompe): '))
    if nota != 999:
        print(f'As notas de {general[nota][0]} são {general[nota][1]} e {general[nota][2]}')
    else:
        if nota == 999:
            break

