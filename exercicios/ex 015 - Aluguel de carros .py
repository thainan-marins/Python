# aqui já fizemos o dicionário de cores
c = {'am': '\033[93m','ve': '\033[92m', 'l': '\033[m', 'i,b': '\033[3;97m', 'n,b': '\033[1;97m'}
# Neste programa iremos calcular o valor de um carro de aluguel
# pedimos os dados pelo teclado através do input
km = float(input('\033[1;37mQuantos Km o carro percorreu? '))
dia = int(input('Por quantos dias o carro foi alugado?\033[m '))
# estas variáveis calcularão o valor da km rodado e o valor dos dias respectivamente
vkm = km * 0.15
vdia = dia * 60
# por fim mostramos na tela, formatado com cores e 2 pontos flutantes por ser dinheiro
print('{}voce andou {}{:.2f}{}KM e ficou {}{}{} dias. O custo total foi de R${}{:.2f}{}'
      .format(c['i,b'], c['am'], km, c['i,b'], c['am'], dia, c['i,b'], c['am'], vkm + vdia, c['l']))
print('{}{:.2f} KM {}= {}R${:.2f} \n{} dias {}= {}R${:.2f}'.
      format(c['i,b'], km, c['ve'], c['i,b'], vkm, dia, c['ve'], c['i,b'], vdia))
