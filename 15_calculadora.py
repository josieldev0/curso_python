'''Calculadora com While'''

while True:
    nmr_1 = input('digite um número: ')
    nmr_2 = input('digite outro número: ')
    operador = input('digite o operador: ')
    
    numeros_validos = None
    nmr_1_float = 0
    nmr_2_float = 0

    try:
        nmr_1_float = float(nmr_1)
        nmr_2_float = float(nmr_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('número digitado inválido')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('operador digitado inválido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue   

    print('Confira o resultado a seguir: ') 

    if operador == '+':
        print(f'{nmr_1_float} + {nmr_2_float}=', nmr_1_float + nmr_2_float)

    elif operador == '-':
        print(nmr_1_float - nmr_2_float)

    elif operador == '*':
        print(nmr_1_float * nmr_2_float)

    elif operador == '/':
        print(nmr_1_float / nmr_2_float)

    else:
        print('Não era pra chgar aqui, pois ja teve validação')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break   