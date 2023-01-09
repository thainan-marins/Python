# Neste programa analizaremos a ditância de uma viagem e diremos seu valor total

# criamos o dicionário para as cores
c = {'l': '\033[m', 'i': '\033[3;97m', 've': '\033[3;32m'}
# perguntamos ao usuário a distância da viagem, um número com vírgula
km = float(input('Qual foi a distância de sua viagem? Km: '))
# criamos aqui uma condição composta
if km <= 200.0: # se o comprimento da viagem for menor ou igual a 200 Km
    # cada Km custurá 50 centavos
    preço = 0.50 * km
    print('{}Sua viajem custou {}R${:.2f}{}.'.format(c['i'], c['ve'], preço, c['l']))
else: # se ela for acima de 200 Km
    # cada Km custará 45 centavos.
    preço2 = km * 0.45
    print('{}Sua viajem custou {}R${:.2f}{}.'.format(c['i'], c['ve'], preço2, c['l']))
    


