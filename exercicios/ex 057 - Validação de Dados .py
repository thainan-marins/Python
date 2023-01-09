# Faça um programa que leia o sexo de uma
# pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

# Perguntamos o sexo do usuário
ge = input('Qual seu sexo [M/F]: ').lower().strip()
# e criamos um laço infinito, que enquanto não for dado um comando 'break' ou ele se tornar falso, vai continuar infini-
# tamente, neste caso ele se tornará falso quando for digitado 'f' ou 'm'
while ge not in 'fm':
    ge = input('Dados inválidos! Digite novamente. [M/F]: ').lower().strip()
