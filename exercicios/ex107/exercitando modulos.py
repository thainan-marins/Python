#  Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#  Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex107.utilidadescev import moeda, dado

num = dado.leiadinheiro('Digite um valor: R$')
"""print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'O valor de {moeda.moeda(num)} com um aumento de 100% é {moeda.aumentar(num, 100)}')"""
moeda.resumo(num, 25, 5, True)

