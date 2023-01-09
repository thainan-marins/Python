# Neste programa o intuito é dizer se um número é par ou não

# pedimos ao usuário um número inteiro
n = int(input('Digite um número: '))
# dividimos este número por 2
pi = n % 2
c = {'ve': '\033[4;32m', 'l': '\033[m'}
# então mostramos na tela um condição simplificada
# mostre 'ele é par' se a variável pi for igual a 0 (todo número par divido por 2 o resto é 0)
# se não mostre 'este número é ímpar'.
print('Esse número é {}PAR{}.'.format(c['ve'], c['l']) if pi == 0 else 'Esse número é {}IMPAR{}.'
      .format(c['ve'], c['l']))



