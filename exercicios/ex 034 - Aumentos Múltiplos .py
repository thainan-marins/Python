# Neste programa iremos ler o valor do salário do usuário e dizer de quanto foi seu aumento. Para salários
# menores ou iguais a 1250, o aumento será de 15%, acima disso, 10% de aumento.

# criamos o dicionário de cores
c = {'i': '\033[0;3;97m', 'v': '\033[3;31m', 'n': '\033[1;37m', 've': '\033[32m', 'l': '\033[m'}
# pedimos ao usuário o valor de seu salário
salario = float(input('{}Digite seu salário para calcular o aumento: {}R${}'.format(c['n'], c['ve'], c['l'])))
# criamos uma condição composta. Se o salário for menor ou igual a 1250
if salario <= 1250.0:
    # esta variável está com o valor da porcentagem
    au = salario / 100 * 15
    # como é um aumento somamos ambas
    por = au + salario
    # mostramos na tela os valores com o terminal colorido
    print('{}Com um aumento de {}15% {}({:.2f}){}, seu salário agora é de {}R${:.2f}{}'.
          format(c['i'], c['v'], c['n'], au, c['i'], c['ve'], por, c['l']))
# Agora, se o salário for maior...
else:
    # variável com o valor de 10% do valor do salário
    aum = salario / 100 * 10
    # somamos ambas ter o valor final do salário
    porc = aum + salario
    # e fazemos o último print, também com cores
    print('{}Com um aumento de {}10% {}({:.2f}){}, seu salário agora é de {}R${:.2f}'
          .format(c['i'], c['v'], c['n'], aum, c['i'], c['ve'], porc))
