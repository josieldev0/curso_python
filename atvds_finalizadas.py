'''nome = 'Josiel Lira'
altura = 1.90
peso = 85
imc = peso//(1.80*2) # ou peso / altura ** 2

print(nome, 'tem', altura, 'de altura, pesa', peso, 'e seu IMC é', imc )'''

#-------------------------------------------------------------------------------

'''primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=} ')

elif primeiro_valor_int < segundo_valor_int:
    print(f'{segundo_valor=} é maior que {primeiro_valor=} ')

elif primeiro_valor == segundo_valor:
    print('ambos números são iguais')

else:
    print('Você não digitou um número')'''

#-------------------------------------------------------------------------------

'''nome = input('Digite seu nome: ')
idade = input ('Digite sua idade: ')
nome_invertido = (nome[::-1])
nmr_letras = len(nome)
pmr_letra = (nome[0])
utm_letra = (nome[-1])

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')

    if ' ' in nome:
        print('Seu nome contém espaçoes')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {nmr_letras} letras')
    print(f'A ultima letra do seu nome é {utm_letra}')

else: 
    print('Desculpe, campos vazios')'''

#-------------------------------------------------------------------------------

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
entrada = input ("Digite um número inteiro")

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'par'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else: 
    print('Você não digitou um número inteiro')
"""
"""
entrada =  input('Digite um Número: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'par'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except: 
    print('Você não digitou um número inteiro')
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
entrada = input('Digite o horario em numeros inteiros ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <=11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >=18 and hora <=23:
        print('Boa noite')
    else:
        print('horario invalido')

except:
    print('Você não digitou um número inteiro')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é curto')

else:
    print('Digite mais de uma letra')
"""

#-------------------------------------------------------------------------------

"""
# Iterando com while
#       012345
nome = 'josiel'  #string são iteráiveis
# -     654321 -
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[2])
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1 

print(novo_nome)
"""

#-------------------------------------------------------------------------------

"""
# Exiba os indices

lista = ['Maria', 'Helena', 'João' ]
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""

#-------------------------------------------------------------------------------

"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# import os
# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')
    
#     if opcao == 'i':
#         os.system('cls')
#         valor = input('Valor: ')
#         lista.append(valor)


#     elif opcao == 'a':
#         indice_str = input('Escolha o indice para apagar: ')
        
#         try:
#             indice = int(indice_str)
#             del lista[indice]

#         except ValueError:
#             print('Por favor digite número inteiro')
#         except IndexError:
#             print('Índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
        

#     elif opcao == 'l':
#         os.system('cls')

#         if len(lista) == 0:
#             print('Vazio')

#         for i, valor in enumerate(lista):
#             print(i, valor)

            
#     else:
#         print('Escolha uma opção válida. ')

#-------------------------------------------------------------------------------

# Exercícios com funções
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def multiplicador(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# resultado = multiplicador(2, 2, 2)
# print(resultado)

#-------------------------------------------------------------------------------

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# def par_impar(numero):
#     if numero % 2 == 0:
#         return f' o {numero} é par' # não preciso do else
#     return f' o {numero} é impar' # só colocar o return fora do bloco

# print(par_impar(1))
# print(par_impar(2))
# print(par_impar(3))
# print(par_impar(4))
    
#-------------------------------------------------------------------------------

