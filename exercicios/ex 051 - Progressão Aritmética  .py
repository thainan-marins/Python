# Desenvolva um programa que leia o primeiro termo e a razão de
# uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# pedimos ao usuário então o valores para o cálculo
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
# e usamos a boa e velha matemática pra fazer isto. 'Décimo' recebe a fórmula da PA, que voltar o valor da posição do
# 10º elemento
decimo = primeiro + (10 - 1) * razao
# para mostrar 10 termos usamos um laço, que está dizendo mais ou menos o seguinte:
# conte no espaço do primeiro elemento (primeiro) até o segundo elemento (decimo), pulando entre tal valor (razao)
for c in range(primeiro, decimo, razao,):
    # por fim, mostre os valores na tela
    print('{}'.format(c), end=' → ')
print('___fim___')
