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
 
# valor = float(input('Qual o valor da casa: '))
# salario = float(input('Qual o salário do comprador: '))
# anos = float(input('Quantos anos de financiamento? '))

# meses = anos * 12
# parcela = valor / meses # or parcela = valor / (anos * 12)
# salario_parcelado = (salario * 30 / 100)

# if salario_parcelado >= parcela:
#     print(f'Para pagar um casa de {valor:.2f} em {anos} anos'
#           f' a prestação será de R${parcela:.2f} Empréstimo aprovado!')
# else:
#     print(f'Para pagar um casa de {valor:.2f} em {anos} anos'
#           f' a prestação será de R${parcela:.2f} Empréstimo negado!')

#-------------------------------------------------------------------------------

# numero = int(input('Digite um número inteiro: '))
# opcao = int(input('Escolha uma das bases para conversão:\n'
#                   ' [1] converter para BINÁRIO\n'
#                   ' [2] converter para OCTAL\n'
#                   ' [3] converter para HEXADECIMAL\n'
#                   ' Sua opção: '))

# binario = bin(numero)
# octal = oct(numero)
# #hexadecimal = hex(numero)
                  
# if opcao == 1:
#     print(binario[2:])
# elif opcao == 2:
#     print(octal[2:])
# elif opcao == 3:
#     print(hex(numero)[2:]) # or <-
# else:
#     print("Número inválido")

#-------------------------------------------------------------------------------

# nmr1 = int(input('Digite um número inteiro'))
# nmr2 = int(input('Digite outro número inteiro'))

# if nmr1 > nmr2:
#     print('O primeiro valor é maior')
# elif nmr1 < nmr2:
#     print('O segundo valor é maior')
# else:
#     print('Não existe maior os dois são iguais')

#-------------------------------------------------------------------------------

# from datetime import date

# nascimento  = int(input('Digite o ano de de nascimento: '))

# ano_atual = date.today().year
# idade = ano_atual - nascimento

# print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')
# if idade < 18:
#     print('Você ainda vai se alistar')
# elif idade == 18:
#     print('Está na hora de se alistar')
# elif idade > 18:
#     print('Já passou do tempo de se alisatr')

#-------------------------------------------------------------------------------

# nota1 = float(input('Primeira nota: '))
# nota2 = float(input('segunda nota: '))

# media = (nota1 + nota2) / 2

# print(f'Sua média foi: {media}')

# if media < 5:
#     print('Reprovado')
# elif media >= 5 and media <= 6.9:
#     print('Recuperação')
# elif media >= 7:
#     print('Aprovado')

#-------------------------------------------------------------------------------

# from datetime import date

# nascimento = int(input('Digite o ano de seu nascimento: '))

# data_atual = date.today().year
# idade = data_atual - nascimento

# print(f'O atleta em {idade} anos')

# if idade <= 9:
#     print('Categoria mirim')
# elif idade > 9 and idade <= 14:
#     print('Categoria infantil')
# elif idade > 14 and idade <= 19:
#     print('Categoria junior')
# elif idade > 19 and idade <= 20:
#     print('Categoria senior')
# else:
#     print('Categoria master')

#-------------------------------------------------------------------------------

# print('Analisador de Triângulos')
# print()
# r1 = input('Primeiro segmento')
# r2 = input('Segundo segmento')
# r3 = input('Terceiro segmento')

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
#     print(f'Os segmetos {r1},{r2},{r3} podem formar um triângulo')
#     if r1 == r2 and r1 == r3:
#         print('Equilátero: todos os lado são iguais')
#     elif r1 == r2 or r1 == r3 or r2 == r3:
#         print('Isósceles: dois lados são iguais')
#     else:
#         print('Isósceles: dois lados são diferentes')
# else:
#     print(f'Os segmetos {r1},{r2},{r3} não podem formar um triângulo')

#-------------------------------------------------------------------------------

# peso = float(input('Qual o seu peso? Kg '))
# altura = float(input('Qual sua altura? M '))

# imc = peso / (altura ** 2)

# print(f"Seu IMC é de {imc}")

# if imc < 18.5:
#     print("Abaixo do peso")
# elif imc >= 18.5 and imc < 25:
#     print("Peso ideal")
# elif imc >= 25 and imc < 30:
#     print("Sobrepeso")
# elif imc >= 30 and imc < 40:
#     print("Obesidade")
# elif imc >= 40:
#     print("Obesidade mórbida")

#-------------------------------------------------------------------------------

# print("LOJINHA DO JOSIEL")
# preco = float(input("Qual o preço das suas compras: "))

# pagamento = int(input('FORMAS DE PAGAMENTO:\n'
#                   ' [1] à vista dinheiro/cheque\n'
#                   ' [2] à vista cartão\n'
#                   ' [3] 2x no cartão\n'
#                   ' [4] 3x ou mais no cartão\n'
#                   ' Qual é a opção: '))

# if pagamento == 1:
#     preco_final = preco - (preco * 2 // 100)
#     print(f'Sua compra será R${preco:.2f} à vista com desconto ')

# elif pagamento == 2:
#     preco_final = preco - (preco * 5 // 100)
#     print(f'Sua compra será à vista R${preco:.2f} com desconto ')
    
# elif pagamento == 3:
#     valor_parcela = preco // 2
#     print(f'Sua compra será parcelada em 2x de {valor_parcela:.2f} sem juros ')

# elif pagamento == 4:
#     preco_final = preco + (preco * 20 // 100)
#     qtd_parcelas = int(input('Quantas parcelas?'))
#     valor_parcela = preco_final // qtd_parcelas
#     print(f'Sua compra será parcelada em {qtd_parcelas}x de {valor_parcela:.2f} com juros ')

# print(f'Sua compra de R${preco:.2f} vai custar R${preco_final:.2f} no final.')

#-------------------------------------------------------------------------------

# from random import randint
# from time import sleep

# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0, 2)

# jogador = int(input('Suas opções: \n'
#                     '[0] PEDRA\n'
#                     '[1] PAPEL\n'
#                     '[2] TESOURA\n' 
#                  'Qual é a sua jogada? '))

# sleep(1)
# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!')

# print(f'Computador jogou {itens[computador]}')
# print(f'Jogador jogou {itens[jogador]}')

# if computador == 0:
#     if jogador == 0:
#         print('Empate')
#     elif jogador == 1:
#         print('Jogador venceu')
#     elif jogador == 2:
#         print('computador venceu')
#     else:
#         print('Jogada inválida')

# elif computador == 1:
#     if jogador == 0:
#         print('Computador venceu')
#     elif jogador == 1:
#         print('Empate')
#     elif jogador == 2:
#         print("Jogador venceu")
#     else:
#         print('Jogada inválida')

# elif computador == 2:
#     if jogador == 0:
#         print('Jogador venceu')
#     elif jogador == 1:
#         print('Computador venceu')
#     elif jogador == 2:
#         print("Empate")
#     else:
#         print('Jogada inválida')

#-------------------------------------------------------------------------------    

# from time import sleep

# for numero in range(10, -1, -1):
#     print(numero)
#     sleep(1)
# print('BOOOMM')

#-------------------------------------------------------------------------------

# for numero in range(1, 51):
#     if numero % 2 == 0:
#         print(numero)

#-------------------------------------------------------------------------------

# soma = 0
# total = 0
# for numero in range(1, 501, 2):
#     if numero % 3 == 0:
#         soma += numero
#         total += 1 

# print(f'A soma de todos os {total} valores é {soma}')

#-------------------------------------------------------------------------------

# numero = int(input('Digite um número para ver sua tabela: '))

# for x in range(1, 11):
#     print(f'{numero} x {x:2} = {numero*x}')

#-------------------------------------------------------------------------------

