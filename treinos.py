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

# soma = 0
# qtd = 0

# for c in range(1, 7):
#     numero = int(input(f'Digite o {c} número: '))
#     if numero % 2 == 0:
#         soma += numero
#         qtd += 1 

# if qtd == 1:
#     print(f'Você informou {qtd} número par e o resultado foi {soma}')
# else:
#     print(f'Você informou {qtd} números pares e a soma foi {soma}')

#-------------------------------------------------------------------------------

# print ('10 TERMOS DE UMA PA')


# termo = int(input('primeiro termo: '))
# razao = int(input('Razão'))
# decimo = termo + (10 - 1) * razao

# for c in range(termo, 11, razao):
#     print(f'{c}', end=' -> ')

# print('Acabou')

#-------------------------------------------------------------------------------

# numero = int(input('Digite um número inteiro: '))
# contador = 0

# for c in range(1, numero + 1):
#     if numero % c == 0:
#         print('\033[33m', end=' ')
#         contador += 1
#     else:
#         print('\033[31m', end=' ')

#     print(f'{c}', end=' ')
    
# print('\n\033[m' f'O numero {numero} foi divisível {contador} vezes ')

# if contador == 2:
#     print('E por isso ele é primo!')
# else:
#     print('E por isso ele não primo!')
    
#-------------------------------------------------------------------------------

# frase = str(input('Digite uma frase: ')).strip().upper()
# palavaras = frase.split()
# juntar = ''.join(palavaras)
# inverso = ''

# for letra in range(len(juntar) - 1, -1, -1): # or inverso == junto[::-1]
#     inverso += juntar[letra]

# print (f'O inverso de {frase} é {inverso}')

# if juntar == inverso:
#    print('Sua frase é um palíndromo')
# else: 
#     print('Sua frase não é um palíndromo')

#-------------------------------------------------------------------------------

# from datetime import date
# data_atual = date.today().year
# maior = 0
# menor = 0

# for c in range(1, 8):
#     nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
#     idade = data_atual - nasc
#     if idade >= 21:
#         maior += 1
#     else:
#         menor += 1

# print(f'Ao todo tivemos {maior} pessoas maiores de idade ')
# print(f'E também tivemos {menor} pessoas menore de idade')

#-------------------------------------------------------------------------------

# maior = 0
# menor = 0

# for p in range(1, 6):
#     peso = float(input(f'Digite o peso da {p} pessoa'))

#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso

# print(f'O maior peso lido foi de {maior}Kg')
# print(f'O menor peso lido foi de {menor}Kg')

#-------------------------------------------------------------------------------

# idade_total = 0
# idade_homem = 0
# nome_homem_velho = ''
# mulheres_menos_20 = 0

# for c in range(1, 5):
#     nome = str(input(f'Nome da {c} pessoa: '))
#     idade = int(input(f'Idade da {c} pessoa: '))
#     sexo = str(input(f'Sexo da {c} pessoa [M] ou [H]: ')).strip
    
#     if idade > 0:
#         idade_total += idade

#     if sexo == 'Hh':
#         if idade > idade_homem:
#             idade_homem = idade
#             nome_homem_velho = nome

#     if sexo == 'Mm':
#         if idade < 20:
#             mulheres_menos_20 += 1

# media_idade = idade_total / c
# print(f'A média de idade do grupo é de {media_idade} anos')
# print(f'O nome do homem mais velho do grupo é {nome_homem_velho}')
# print(f'No grupo {mulheres_menos_20} mulheres tem menos de 20 anos')

#-------------------------------------------------------------------------------

# sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Dados inválidos. Por favor informe seu sexo')).strip().upper()[0]
# print(f'Sexo {sexo} registrado com sucesso')

#-------------------------------------------------------------------------------

# from random import randint
# from time import sleep

# tentativas = 1

# numero = int(input('Vou pensar em um número de 1 a 10\n' 
#                     'tente adivinhar qual é: '))
# print('Processando...')
# sleep(3)
# pensado = randint(0, 10)

# while numero != pensado:
#     if numero < pensado:
#         print('maior... tente mais uma vez. ')
#     else:
#         print('menor... tente mais uma vez. ')
#     numero = int(input(f'Errou, tente novamente'))
#     print('Processando...')
#     sleep(3)
#     tentativas += 1
    
# print(f'Você acertou eu pensei em {pensado}, foram necessárias {tentativas} tentativas ')

#-------------------------------------------------------------------------------

# from time import sleep

# primeiro_valor = int(input('Primeiro valor: '))
# segundo_valor = int(input('Segundo valor: '))
# menu = 0

# while menu != 5:
#     menu = int(input('[1] Somar\n' 
#                     '[2] Multiplicar\n' 
#                     '[3] Maior\n' 
#                     '[4] Novos números\n' 
#                     '[5] Sair\n'))
#     if menu == 1:
#         soma = primeiro_valor + segundo_valor
#         print(f'A soma de {primeiro_valor}+{segundo_valor} é igual a {soma}')
#     elif menu == 2:
#         multiplicacao = primeiro_valor * segundo_valor
#         print(f'A multiplicação de {primeiro_valor} x {segundo_valor} é igual a {multiplicacao}')
#     elif menu == 3:
#         if primeiro_valor > segundo_valor:
#             print(f'O maior valor entre {primeiro_valor} e {segundo_valor} é o primeiro valor digitado: {primeiro_valor}')
#         elif primeiro_valor == segundo_valor:
#             print(f'Os dois números tem o mesmo valor')
#         else:
#             print(f'O maior valor entre {primeiro_valor} e {segundo_valor} é o segundo valor digitado: {segundo_valor}')
#     if menu == 4:
#         print('Informe os número novamente')
#         primeiro_valor = int(input('Primeiro valor: '))
#         segundo_valor = int(input('Segundo valor: '))
#     else:
#         print('Finalizando...')
#         sleep(3)
        
# print('Você saiu do programa')

#-------------------------------------------------------------------------------

# numero = int(input('Calcular seu fatorial: '))
# valor = numero
# fatorial = 1

# print(f'Calculando {numero}! = ', end='')

# while valor > 0:
#     print(f'{valor}', end='' )
#     print(f' x ' if valor > 1 else ' = ', end='' )
#     fatorial *= valor
#     valor -= 1
    
# print(fatorial)
    
#-------------------------------------------------------------------------------

# numero = int(input('Calcular seu fatorial: '))
# fatorial = 1

# for valor in range (numero, 0, -1):
#     print(valor, end='')
#     print(' x ' if valor > 1 else ' = ', end= '')
#     fatorial *= valor

# print(fatorial)

#-------------------------------------------------------------------------------

# print('Gerador de PA')
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10 - 1) * razao
# total = primeiro

# while total != decimo:
#     print(f'{total} → ', end='')
#     total += razao

# print(total, end=' ')
# print('Fim')

#-------------------------------------------------------------------------------
# print('Gerador de PA')

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# total = primeiro
# continuar = ''
# qtd = 0
# contador = 1

# while contador <= 10:
#     print(f'{total} → ', end='')
#     total += razao
#     contador += 1
# print(total)
# contador = 1

# while continuar != 'N':
#     continuar = str(input('Você quer ver mais termos? [S/N]')).strip().upper()[0]

#     if continuar != 'N':
#         qtd = int(input('Quantos'))
    
#         while contador <= qtd:
#             print(f'{total} → ', end='')
#             total += razao
#             contador += 1
#         print(total)
#         contador = 1

# print('FIM')

#-------------------------------------------------------------------------------

# print('Sequencia de Fibonacci')

# numeros = int(input('Quantos termos você quer mostrar'))
# contador = 0
# termo1 = 0
# termo2 = 1

# print(f'{termo1} → {termo2}', end=' → ')

# while contador != numeros:
#     termo3 = termo1 + termo2
#     print(f'{termo3} → ', end='')
#     termo1 = termo2
#     termo2 = termo3
#     contador += 1

# print('FIM')

#-------------------------------------------------------------------------------

# numero = 0
# contador = 0 
# soma = 0
# # or numero = contador = soma = 0

# numero = int(input('Digite um número [999 para parar]'))
# while numero != 999:
#     contador += 1
#     soma += numero
#     numero = int(input('Digite um número [999 para parar]'))

# print(f'Você digitou {contador} números e a soma entre eles foi de {soma}')

#-------------------------------------------------------------------------------

# pergunta = 'S'
# contador = media = soma = maior = menor = 0

# while pergunta not in 'N':
#     numero = int(input('Digite um número: '))

#     contador += 1
#     soma += numero

#     if contador == 1:
#         maior = menor = numero
#     else:
#         if numero > maior:
#             maior = numero
#         if numero < menor:
#             menor = numero

#     pergunta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    
# media = soma / contador

# print(f'Você digitou {contador} número e a média foi de {media}')
# print(f'O maior valor foi {maior} e o menor valor foi {menor}')

#-------------------------------------------------------------------------------

# numero = soma = qntd = 0
# while True:
#     numero = int(input('Digite um número: [ou 999 para parar]'))
#     if numero == 999:
#         break
#     soma += numero
#     qntd += 1
    
# print(f'Você digitou {qntd} números e a soma entre eles foi de {soma}')

#-------------------------------------------------------------------------------

# contador = 1

# while True:
#     numero = int(input(f'Quer ver a tabuada de qual número: '))
#     if numero < 0:
#         break
#     while contador <=10: 
#         soma = numero * contador
#         print(f'{numero} x {contador} = {soma}')
#         contador += 1
#     contador = 1
# print('Encerrado')

#-------------------------------------------------------------------------------

# from random import randint

# vitorias = 0

# while True:
#     computador = randint(0, 10) 
#     escolha_jogador = str(input('Impar ou Par? [I/P]')).strip().upper()[0]
#     jogador = int(input('Escolha um número: '))

#     soma = jogador + computador
#     par = soma % 2 == 0

#     print(f'Você jogou {jogador} e o computador {computador}. O total foi de {soma}')
#     print('Deu Par' if par == True else 'Deu impar')

#     if escolha_jogador == 'I' and par == True:
#         print('Você perdeu')
#         break
#     if escolha_jogador == 'P' and par == False:
#         print('Você perdeu')
#         break
    
#     print('Você ganhou')
#     vitorias += 1

# print(f'Acabou, Você venceu {vitorias}x')

#-------------------------------------------------------------------------------

# maior_idade = total_homens = mulher_menos_20_anos = 0

# while True:

#     idade = int(input('Digite sua idade: '))
#     sexo = ' '

#     while sexo not in 'MF':
#         sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]

#     if idade >= 18:
#         maior_idade += 1

#     if sexo in 'Mm':
#         total_homens += 1

#     if sexo in 'Ff' and idade < 20:
#          mulher_menos_20_anos += 1

#     continuar = ' '

#     while continuar not in 'SN':
#         continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    
#     if continuar in 'Nn':
#         break
    
# print(f'{maior_idade} pesoas tem mais de 18 anos')
# print(f'{total_homens} homens foram cadastrados')
# print(f'{mulher_menos_20_anos} mulheres tem mais de 20 anos')

#-------------------------------------------------------------------------------

# total = mais_mil = mais_barato = contador = 0
# nome_mais_barato = ' '

# while True:
        
#     nome = str(input('Digite o nome do produto: '))
#     preco = float(input('Digite o valor do produto: '))
    
#     contador += 1
#     total += preco
    
#     if preco > 1000:
#         mais_mil += 1
    
#     if contador == 1 or preco < mais_barato:
#         mais_barato = preco
#         nome_mais_barato = nome

#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
#         print('Opção invalida, digite [S/N]')

#     if continuar in 'Nn':
#         break

# print(f'O total de gasto na compra foi de R${total:.2f}')
# print(f'{mais_mil} produtos custam mais de R$1000')
# print(f'{nome_mais_barato} foi o pruduto mais barato e custou R$ {mais_barato}')

#-------------------------------------------------------------------------------

# valor = int(input('Qual o valor você quer sacar? R$'))

# total = valor
# cedula = 50
# total_cedula = 0

# while True:
#     if total >= cedula:
#         total -= cedula
#         total_cedula += 1

#     else:
#         if total_cedula > 0:
#             print(f'Total de {total_cedula} cédulas de R$ {cedula}')

#         if cedula == 50:
#             cedula = 20

#         elif cedula == 20:
#             cedula = 10

#         elif cedula == 10:
#             cedula = 1

#         total_cedula = 0

#         if total == 0:
#             break

# print('Volte sempre')

#-------------------------------------------------------------------------------

# tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
#          'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
#          'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
#          'dezenove', 'vinte')

# while True:
#     numero = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= numero <= 20:
#         break
#     print('Tente novamente. ', end='')

# print(f'Voce digitou o número {tupla[numero]}')

#-------------------------------------------------------------------------------

# tupla = ('palmeiras', 'flamengo', 'cruzeiro', 'mirassol', 'bahia', 'botafogo', 'fluminense',
#          'são paulo', 'atlético-mg', 'vasco', 'bragantino', 'ceará', 'corinthians', 'grêmio',
#          'internacional', 'vitória', 'santos', 'juventude', 'fortaleza',
#          'sport')

# primeiros = tupla[0:5]
# ultimos = tupla[-4:]
# pos_santos = tupla.index('santos')
# ordem = sorted(tupla)

# print(f'Os 5 primeiros colocados são {primeiros}')
# print(f'Os 4 últimos colocados são {ultimos}')
# print(f'Tabela em ordem alfabética{ordem}')
# print(f'O santos está na {pos_santos+1}º posição')

#-------------------------------------------------------------------------------

# from random import randint

# tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

# print(f'Os valores sorteados foram: ', end='')

# for numero in tupla:
#     print(f'{numero} ', end='')
# print(f'\nO maior valor foi {max(tupla)}')
# print(f'O menor valor foi {min(tupla)}')

#-------------------------------------------------------------------------------

# tupla = (int(input('Digite o primeiro valor')),
#         int(input('Digite o segundo valor')),
#         int(input('Digite o terceiro valor')),
#         int(input('Digite o quarto valor')))

# contador_nove = tupla.count(9)
# posicao_tres = tupla.count(3)

# if contador_nove == 0:
#     print('O valor nove não apareceu nenhuma vez')
# else:
#     print(f'O valor 9 apareceu {contador_nove}x')

# if posicao_tres == 0:
#     print('O 3 não apareceu em nenhuma posição')
# else:
#     print(f'o primeiro valor 3 está na {tupla.index(3)+1}° posição')

# print(f'Os números pares foram: ')
# for numero in tupla:
#     if numero % 2 == 0:
#         print(numero, end=',')

#-------------------------------------------------------------------------------

# tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25)

# for posicao in range(0, len(tupla)):
#     if posicao % 2 == 0:
#         print(f'{tupla[posicao]:.<30}', end='')
#     else:
#         print(f'R$ {tupla[posicao]:>7.2f}')

#-------------------------------------------------------------------------------

# tupla = ('aprender', 'programar', 'linguagem')
# vogais = ('a', 'e', 'i', 'o', 'u')

# for palavra in (tupla):
#     print(f'\nNa palavra {palavra} temos: ', end='')

#     for letra in palavra:
#         if letra.lower() in vogais:
#             print(f'{letra}', end='')

#-------------------------------------------------------------------------------

