# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
#
# — Quantidade de notas
# — A maior nota
# — A menor nota
# — A média da turma
# — A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*n, sit=False):
    """
    Esta função analisa várias notas de alunos e mostra sua situação.
    :param n: Recebe as notas
    :param sit: Mostra ou não a situação do aluno
    :return: Um dicionário com o total, a maior e a menor nota, mostra a média e como parmâmetro opicional a situação.
    """
    r = dict()
    r['TOTAL'] = len(n)
    r['MAIOR'] = max(n)
    r['MENOR'] = min(n)
    r['MEDIA'] = sum(n)/len(n)
    if sit:
        if r['MEDIA'] >= 7:
            r['SITUAÇAO'] = 'BOA'
        elif r['MEDIA'] >= 5:
            r['SITUAÇAO'] = 'RAZOAVEL'
        else:
            r['SITUAÇAO'] = 'RUIM'
    return r


# programa principal
resp = notas(5.5, 5.5, 5.5, 5.5, sit=True)
print(resp)
