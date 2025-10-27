# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort() #ordenar lista
# print(lista)
# lista.sort(reverse=True) #ordenar lista
# # sorted(lista)
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista:
#     print(item)

# ou

# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()
    
# lista.sort(key=lambda item: item['nome'])
# lista.sort(key=lambda item: item['sobrenome'])

# #ou
# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)

# Trocando def por lambda
def executa(funcao, *args):
    return funcao(*args)
def soma(x, y):
    return x + y
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(10))

print(executa(lambda x, y: x + y, 2,3),
    executa(soma, 2, 3),
    soma(2, 3)
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5
    )
)