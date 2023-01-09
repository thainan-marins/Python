# neste programa a inteção é criar um conversor de moedas, do real para o dólar
# perguntamos ao usuário quanto ele irá converter
d = float(input('Quantos reais você tem? \033[32mR$'))
# o dicionário de cores
c = {'p': '\033[1;30m', 've': '\033[0;32m', 'l': '\033[m'}
# mostramos na tela os dados, usando formatação .format com cores
print('{}Com {}R${:.2f} {}você pode comprar {}US${:.2f} {}e sobrará {}R${:.2f}{}. '
        # aqui usamos operadores aritiméticos para fazer a conversão, sem variável
      .format(c['p'], c['ve'], d, c['p'], c['ve'], d/5.60, c['p'], c['ve'], d % 5.60, c['p']))
print('{}Agora, com {}R${:.2f} {}você pode comprar {}£{:.2f}{}.'
      .format(c['p'], c['ve'], d, c['p'], c['ve'], d/6.36, c['p']))




