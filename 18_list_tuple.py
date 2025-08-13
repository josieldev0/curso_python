"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Josiel',  1.2, []]
lista[-3] = 'João'
print(lista)
print(lista[2], type(lista[2]))
"""

# Create Read Update   Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)

"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] #apagou indice 2
# print(lista)
# print(lista[2])
lista.append(50) #adiciona esse indice ao final da lista
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)
"""

"""
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(4, 5)
print(lista[4])
"""

# Concatenando e estendendo listas em Python

"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.extend(lista_b)
lista_c = lista_a + lista_b

print(lista_a)
print(lista_c)
"""


# Cuidado com os dados mutáveis

"""
# = - copiado o valor
nome = 'Josiel'
outra = nome 
nome = 'João'

print(nome)
print(outra)

# = - aponta para o mesmo valor na memória
lista_a = ['Josiel', 'Maria']
lista_b = lista_a
#lista_b = lista_a.copy() #para copiar
lista_a[0] = 'banana'

print(lista_b)
"""

# for in com listas

"""
lista = ['Josiel', 'João', 'Maria']

for nome in lista:
    print(nome, type(nome))
"""

"""
# Exiba os indices

lista = ['Maria', 'Helena', 'João' ]
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""

# Introdução ao empacotamento e desempacotamento

"""
_, nome2, *_ = ['João', 'Maria', 'Josiel']
print(nome2)
"""

# Tipo tupla -> uma lista imutável

nomes = ('João', 'Maria', 'Josiel') # trocar o [] para () ou nada
# nomes = tuple(nomes) # Tranforma uma lista em tupla
# nomes = list(nomes) # Transforma uma tupla em lista
# nomes = [1] = 'outro' # Não muda e o código da erro
print(nomes)









