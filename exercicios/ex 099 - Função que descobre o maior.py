# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(* num):
    mai = cont = 0
    for m in num:
        if cont == 0:
            mai = m
        else:
            if m > mai:
                mai = m
        cont += 1
    print()
    print(f'''Foram analisados {len(num)} números: {num}
o maior deles é o {mai}''')
    print('=-' * 30)




maior(2, 5, 6, 7, 2, 4)
maior(4, 7, 3)
maior(1)
maior(23, 53, 25, 63, 72)

