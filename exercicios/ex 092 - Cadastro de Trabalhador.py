# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import datetime
aposentar = 0
temcarteira = False

dados = {'nome': ' ', 'ano': 0, 'carteira': ' '}

dados['nome'] = str(input('Nome: '))
dados['ano'] = int(input('Ano de nascimento: '))
dados['sexo'] = str(input('Sexo: '))[0].lower()
idade = datetime.now().year - dados['ano']


while len(dados['carteira']) != 8:
    dados['carteira'] = str(input('''Carteira de trabalho
(se não possuir, digite 0): '''))
    if dados['carteira'][0] in '0':
        break
    temcarteira = True
    if len(dados['carteira']) < 8:
        print('Digitos incorretos! Tente novamente.')

if len(dados['carteira']) == 8:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))

if dados['sexo'] in 'm':
    aposentar = idade + 20
if dados['sexo'] in 'f':
    aposentar = idade + 15

print(f'''{"=-" * 15}

O(a) senhor(a) {dados['nome']} tem {idade} anos;''')
if temcarteira == True:
    print(f'''Irá se aposentar aos {aposentar} anos;
Sua carteira de trabalho é: {dados['carteira']};
Foi contratado(a) em {dados['contratação']};
E seu salário é de R${dados['salario']:.2f}.

Fim.''')
else:
    print('''E não possui carteira de trabalho.
    
Fim.''')
