# neste programa fizemos uma verificação de uma string, tetando valores 'True' e 'False'
# como eu queria deixar o terminal vermelho se fosse falso e verde se fosse verdadeiro a
# precisei colocar várias condições compsotas
a = str(input('digite algo: '))
c = {'v': '\033[31m', 've': '\033[32m', 'l': '\033[m'}
if a.isnumeric():
    print('São números? {}{}{}'.format(c['ve'], a.isnumeric(), c['l']))
else:
    print('São números? {}{}{}'.format(c['v'], a.isnumeric(), c['l']))
if a.isalpha():
    print('São letras? {}{}{}'.format(c['ve'], a.isalpha(), c['l']))
else:
    print('São letras? {}{}{}'.format(c['v'], a.isalpha(), c['l']))
if a.isspace():
    print('São apenas espaços? {}{}{}'.format(c['ve'], a.isspace(), c['l']))
else:
    print('São apenas espaços? {}{}{}'.format(c['v'], a.isspace(), c['l']))
if a.isalnum():
    print('São letras e números? {}{}{}'.format(c['ve'], a.isalnum(), c['l']))
else:
    print('São letras e números? {}{}{}'.format(c['v'], a.isalnum(), c['l']))
if a.isupper():
    print('Está capitalizada? {}{}{}'.format(c['ve'], a.isupper(), c['l']))
else:
    print('Esta capitalizada? {}{}{}'.format(c['v'], a.isupper(), c['l']))
# por último este comando irá dizer o tipo primitivo do input recebido
print('O tipo primitivo desse valor é: {}{}{}'.format('\033[1;97m', type(a), c['l']))



