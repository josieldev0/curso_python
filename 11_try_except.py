'''
Introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_int = int(numero_str)
    print(f'O dobro de {numero_str} é {numero_int * 2}')
except:
    print('Não foi digitado um número')
    
'''
if numero_str.isdigit():
    numero_int = int(numero_str)
    print(f'O dobro de {numero_str} é {numero_int * 2}')
else: 
    print('Não foi digitado um número')
'''