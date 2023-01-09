# Refaça o DESAFIO 009, mostrando a tabuada de um número que
# o usuário escolher, só que agora utilizando um laço for.

# isso é simples, como sabemos até onde queremos ir o for é bem útil
# perguntamos então o número ao usuário
num = int(input('Digite um número: '))
# criamos o laço de 1 a 11, pois o python sempre ignora o último número
for c in range(1, 11):
    #m = num * c | isso pode ser simplificado assim...
    # então substituímos os valores, formatando-os no próprio print
    print('{} X {:2} = {}'.format(num, c, num * c)) # num * c é quem vai nos dar o resultado
