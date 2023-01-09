from ex115.libraly.interface import *
from ex115.libraly.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)


cabeçalho('Menu do Sistema')
while True:
    resposta = menu(['Listar pessoas cadastradas;', 'Cadastrar nova pessoa;', 'Sair do programa.'])
    if resposta == 1:
        # opção de listar pessoas cadastradas
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO:')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do programa. Até logo...')
        break
    else:
        print('\033[1;31mERRO: opção inválida!\033[m')
    sleep(2)
