

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip().replace(' ', '')
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[1;31mERRO: \"{entrada}\" não é um número válido.\033[m')
        else:
            valido = True
            return float(entrada)




