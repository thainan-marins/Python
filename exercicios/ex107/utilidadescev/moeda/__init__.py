def aumentar(n, taxa, monetario=False):
    """
    'A função aumentar irá calcular quantos porcentos a mais será atribuido ao valor.'
    :param n: número a ser calculado.
    :param taxa: a quantidade em porcentagem a ser aumentada.
    :param monetario: é um valor booleano que determinará se o valor será ou não codificado em moeda.
    :return: o valor total calculado
    """
    res = n + n / 100 * taxa
    if monetario:
        return moeda(res)
    else:
        return res


def diminuir(n, taxa, monetario=False):
    res = n + n / 100 * taxa
    if monetario:
        return moeda(res)
    else:
        return res


def dobro(n, monetario=False):
    res = n*2
    if monetario:
        return moeda(res)
    else:
        return res


def metade(n, monetario=False):
    res = n / 2
    if monetario:
        return moeda(res)
    else:
        return res


def moeda(preco=0, forma='R$'):
    return f'{forma:<3}{preco:.2f}'.replace('.', ',')


def resumo(num=0, taxamais=0, taxamenos=0, formato=False):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    res = {'Preço analisado:': moeda(num), 'Dobro do preço:': dobro(num, formato), 'Metade do preço:': metade(num, formato),
           f'Aumento de {taxamais}%:': aumentar(num, taxamais, formato),
           f'Diminução de {taxamenos}%:': diminuir(num, taxamenos, formato)}
    for c, n in res.items():
        print(f'{c:<20} {n}', end=' ')
        print()
    print('-'*30)


def linha(tam=0):
    print('-'*tam)


