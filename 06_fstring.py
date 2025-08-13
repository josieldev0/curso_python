'''
nome = 'Josiel Lira'
altura = 1.90
peso = 85
imc = peso//(1.80*2) # ou peso / altura ** 2

#"f-strings"
#print(nome, 'tem', altura, 'de altura, pSesa', peso, 'e seu IMC é', imc )
linha_1 = f'{nome} tem {altura:.2f} de altura pesa {peso} e seu IMC é {imc:.1f}'
print(linha_1)

a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f} {}'
formato = string.format(a, b, c)

print(formato)
'''

#-------------------------------------------------------------------------------

'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro
= Força o número aparecer antes dos zeros
Sinal - +ou-
Ex. 0>100,.1f
conversion flags - !r !s !a
'''
'''
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:$^10}')
print(f'{10000.464123:0>10.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
'''

#-------------------------------------------------------------------------------


# Fatiamento de strings
#  0123456789
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] [::] 
# A função len retorna a qtd de caracter da str

variavel = 'Olá mundo'
print(variavel[4])
print(variavel[0:7])
print(variavel[0:8:2]) # pula caracter
print(len(variavel[0:7])) # len() contagem de caracteres
print(variavel[::-1])


#-------------------------------------------------------------------------------

'''
# Interpolação básica de strings %
# S - string
# d e i - int
# f float 
x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Josiel'
preco = 1000.9876543
variavel = '%s, o preço total é R$%.2f' %(nome,preco)
print(variavel)
print('O hexadecimal de %d é %010x' % (15, 15))
'''

#-------------------------------------------------------------------------------

