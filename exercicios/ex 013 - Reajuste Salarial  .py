# Aqui calcularemos um aumento ao salário de um funcionário
# recebemos os dados através do teclado
salario = float(input('Qual o seu salário? '))
# operação simples para a porcentagem
porc = salario/100*15
# como é um acréscimo, somamos as variáveis
resu = salario + porc
# o dicionário de cores
c = {'ne': '\033[7;37m', 've,s': '\033[4;32', 've': '\033[32m', 'l': '\033[m'}
# mostramos na tela o valor das variáveis formatada com cores e, como se trata de dinheiro usei :.2f para mostrar
# apenas duas casa depois da vírgula
print('{}Houve o aumento de {}R${}{:.2f}, Seu salario agora é de {}R${}{:.2f}.{}'
      .format(c['s'], c['ve'], c['s'], porc, c['ve'], c['s'], resu, c['l']))

