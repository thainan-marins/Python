# Desenvolva uma lógica que leia o peso e a altura de uma
# pessoa, calcule seu IMC e mostre seu status:

# Para fazer esta calculadora precisamos da altura e peso da pessoa
p = float(input('Qual o seu peso? kg '))
a = float(input('Qual a sua altura? Cm '))
# a fórmula é simples, multiplique a altura por 100 (se a grandeza for em metros não precisa fazer a multiplicação),
# então divida pelo peso e eleve ao quadrado
imc = p / (a / 100) ** 2
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está em sobrepeso.')
elif imc < 40:
    print('Você está em obesidade.')
else:
    print('Você está em obecsidade mórbida.')

