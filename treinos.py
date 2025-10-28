# from random import randint
# from time import sleep

# computador = randint(0, 5)

# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# numero = int(input('em que numero eu pensei? ' ))
# print('Processando')
# sleep(3)

# if numero == computador:
#     print(f'Você me ganhou em pensei em {computador}')
# else:
#     print(f'Você perdeu em pensei em {computador}')

#-------------------------------------------------------------------------------

# velocidade_carro = int(input('Qual é a velocidade atual do carro? '))
# valor_multa = (velocidade_carro - 80) * 7

# if velocidade_carro > 80:
#     print(f'Voce excedeu o limite de velocidade'
#             f' e foi multado em R${valor_multa:.2f} ')
# print('Tenha um bom dia! Dirija com segurança! ')

#-------------------------------------------------------------------------------

# numero = float(input(('Me diga um número qualquer')))

# if numero % 2 == 0:
#     print('Seu numero é par')
# else: 
#     print('Seu número e ímpar')

#-------------------------------------------------------------------------------

# 0,50 por km ate 200km
# 0,45 por km acima

# distancia = float(input('Qual a distacia da sua viagem?'))
# preco1 = distancia * 0.50
# preco2 = distancia * 0.45

# if distancia <= 200:
#     print(f'Você está prestes a começar uma viagem de {distancia:.2f}KM'
#     f' e preeço da sua passagem será R${preco1:.2f}')
# else:
#     print(f'Você está prestes a começar uma viagem de {distancia:.2f}KM'
#     f' e preeço da sua passagem será R${preco2:.2f}')
#or
#versão simplificada
# preco = distancia * 0.50 if <= 200 else distancia * 0.45
# nesse caso a variavel usada seria somente 'preco'

#-------------------------------------------------------------------------------

# from datetime import date
# ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual'))

# if ano == 0:
#     ano = date.today().year

# if ano % 4 == 0 and ano % 100 != 400 == 0 :
#     print(f'O ano {ano} é bissexto ')
# else: 
#     print(f'O ano {ano} não é bissexto ')

#-------------------------------------------------------------------------------

# a = input('Primeiro  valor: ')
# b = input('Segundo  valor: ')
# c = input('Terceiro  valor: ')

# menor = a
# maior = a

# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c

# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c

# print()
# print(f"o menor valor digitado foi {menor}")
# print(f"o maior valor digitado foi {maior}")

#-------------------------------------------------------------------------------

# salario = float(input ('Qual o salário do funcionário? '))

# if salario <= 1250:
#     novo_salario = salario + (salario * 15 / 100)
# else:
#     novo_salario = salario + (salario * 10 / 100)

# print(f'quem ganahava R${salario:.2f} passa a ganhar R${novo_salario:.2f}')

#-------------------------------------------------------------------------------

# print('Analisador de Triângulos')
# print()
# r1 = input('Primeiro segmento')
# r2 = input('Segundo segmento')
# r3 = input('Terceiro segmento')

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
#     print(f'Os segmetos {r1},{r2},{r3} podem formar um triângulo')
# else:
#     print(f'Os segmetos {r1},{r2},{r3} não podem formar um triângulo')

#-------------------------------------------------------------------------------
 
