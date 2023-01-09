# Neste programa iramos verificar se o motorista passou do limite de velocidade e foi multado ou não

# criamos o dicionário de cores
c = {'l': '\033[m', 'a': '\033[34m', 'v': '\033[31m', 'b': '\033[97m'}
# pedimos ao usuário a velocidade em um input do tipo float
kmh = float(input('{}Qual era a velocidade do veículo? Km/h:{}'.format(c['b'], c['l'])))
# aqui verificamos se ele passou de 80 km/h, se sim será multado
if kmh > 80.0:
    mul = (kmh - 80) * 7.0 # nesta variável calculamos o valor da multa
    print('{}Você foi multado!{}'.format(c['v'], c['l']))
    # mostramos na tela o valor da multa
    print('{}O valor da multa será de R${}{:.2f}{}.'.format(c['b'], c['v'], mul, c['l']))
# se ele estava dentro do limite recebera uma mensagem para prosseguir.
else:
    print('{}Nada a relatar. Tenha um bom dia.{}'.format(c['a'], c['l']))


