# Operadores lógicos

# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# and
'''
entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Sair') 
'''

# or
'''
entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Sair')
senha = input('digite uma senha') or 'Sem senha'
print(senha)
'''

# not
# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

# Operadores in e not in
# Strings são iteráveis
#   0 1 2 3 4 5 
#   J o s i e l
#  -6-5-4-3-2-1

# in
'''
nome = 'Josiel'
# print(nome[2])
# print(nome[-4])
print('s' in nome)
print('z' in nome)
print('s' and 'o' in nome)
'''
'''
#not in
print('iel' not in nome)
'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')