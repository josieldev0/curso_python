'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
'''
'''
condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':  
        break
print('Você saiu')
'''
'''
contador = 0

while contador < 10 :
    print(contador)
    contador = contador + 1

print('Acabou')
'''

"""
Operadores de atribuição
= += -= *= /= //= **= %=

contador = 10

contador -= 5
print(contador) 
"""
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 10:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 30:
        print(f'Não vou mostrar o {contador} ')
        continue

    print(contador)
    
    if contador == 50:
        break

print('Acabou')
"""
"""
qnt_linhas = 5
qnt_colunas = 5

linha = 1 
while linha <= qnt_linhas:
    coluna = 1
    while coluna <= qnt_colunas:
        print(f'{linha=} {coluna=}')
        coluna +=1
    linha += 1 

print ('Acabou')
"""

"""
# while/else
string = 'Valor Qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
        
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string')
print('Fora do while')
"""


frase = 'aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)