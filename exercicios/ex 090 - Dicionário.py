# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

dados = dict()
dados['nome'] = str(input('Qual o nome do aluno? '))
dados['media'] = float(input('Qual a média do aluno? '))
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado(a)'
elif dados['media'] >= 5 < 7:
    dados['situação'] = 'de Recuperação'
else:
    dados['situação'] = 'Reprovado(a)'
print(f'O aluno(a) {dados["nome"]} está {dados["situação"]}.')
