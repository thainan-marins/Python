# neste programo precisávamos mostrar na tela o dobro o triplo e a raiz quadrado de um númro inteiro
# então recebemos e entrada de dados formatada
n1 = int(input('digite um numero '))
# criamos as variáveis que irão multiplicar o valor
d = n1*2
t = n1*3
# para a raiz quadrada usei um princípio matemático, porem o python também tem  uma função para isso, o '.sqr'
r = n1**(1/2)
# por último printamos o valor das variáveis formatadas, sendo a raiz quadrada com até 3 casas flutuantes.
print('o dobro de {} é {} o triplo é {} e a raiz quadrada é {:.3f}'.format(n1, d, t, r))

