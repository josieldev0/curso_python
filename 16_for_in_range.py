"""
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_digitada != senha_salva:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Saiu do laço')
"""

"""
texto = 'python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
"""

"""
For + Range
range -> range(start, stop, step)
(onde começa, onde termina-1, de qnt em qnt)
"""
"""
numeros = range(0, 10, 2)

for numero in numeros:
    print(numero)
"""

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
# texto = 'Josiel'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

#   for letra in texto:
#       print(letra)

"""
O que aprendemos com while também funciona no for
(continue, break, else, etc)
"""

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else: 
    print('For completo com sucesso')