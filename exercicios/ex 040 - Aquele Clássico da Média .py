# Crie um programa que leia duas notas de um aluno e
# calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida.

# pedimos então os valores das notas...
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite a outra: '))
# para saber a média somamos as notas e dividimos
m = (n1 + n2) / 2
# se a nota for menor que 5 o aluno está reprovado
if m < 5.0:
    print('Sua média é {:.1f}. Você está REPROVADO.'.format(m))
# se não, se a média estive entre tais valores, estará de recuperação
elif m >= 5.0 and m <= 6.9:
    print('Sua média é {:.1f}. Você esta de RECUPERAÇÃO.'.format(m))
# se não, se a nota for acima disto o aluno está aprovado
else:
    print('Sua média é {:.1f}. Você está APROVADO.'.format(m))


