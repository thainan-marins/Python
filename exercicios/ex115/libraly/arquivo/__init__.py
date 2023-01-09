from ex115.libraly.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro com a criação do arquivo')
    else:
        print('Arquivo .txt criado com sucesso!')



def lerArquivo(nome):
    try:
        a = open(nome)
    except:
        print('Não foi possível ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally: # o "finally" significa que aconteça o que acontecer, ele vai fechar o arquivo
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # a == append, ou seja, ele irá adicionar algo ao arquivo
    except:
        print('Houve um erro ao tentar abrir o arquivo.')
    else:
        try:
            a.write(f'{nome:<30}{idade:>3} anos\n')
        except:
            print('Houve um erro na hora de escrever o arqivo.')
        else:
            print(f'Novo cadastro de {nome} adicionado com secesso.')
            a.close()

