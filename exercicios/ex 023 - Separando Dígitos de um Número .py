# Aqui criamos o dicionário de cores
co = {'a': '\033[1;34m', 'b': '\033[1;97m', 'l': '\033[m'}
# pedimos uma entrada de dados, neste caso são números inteiros
n = int(input('{}Digite um número entre {}o{} e {}9999{}: '.format(co['b'], co['a'], co['b'], co['a'], co['b'])))
# precisamos converter o número que o usuário digitou para as seguintes grandezas, então usaremos estas
# variáveis com operadores aritiméticos
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
# formatamos o resultado utilizando o .format com o terminal colorido. Os caracteres {} se referem onde a
# variável será substituída.
print('{}Milhar:{}{}{}'.format(co['b'], co['a'], m, co['l']))
print('{}Centena:{}{}{}'.format(co['b'], co['a'], c, co['l']))
print('{}Dezena:{}{}{}'.format(co['b'], co['a'], d, co['l']))
print('{}Unidade:{}{}{}'.format(co['b'], co['a'], u, co['l']))



