# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'Nome': 'Josiel',
#     'sobrenome': 'Lira',
#     # 'idade': 21,
# }

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print(pessoa.setdefault('idade', 30))

# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# d2 = copy.deepcopy(d1) #or copy.copy

# d2['c1'] = 100
# d2['l1'] = 999

# print(d1)
# print(d2)

p1 = {
    'nome': 'Josiel',
    'sobrenome': 'Lira',
}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

p1.update({
    'nome': 'ana',
    'idade': 20,
})
#or
p1.update(nome='bruno', idade=30)
#or
tupla = (('nome', 'Carol'), ('idade', 19))
lista = [['nome', 'Buddy'], ['idade', 8]]

p1.update(tupla)
p1.update(lista)
print(p1)
