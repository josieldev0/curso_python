"""
 Introdução ás funções (def) em Python
 Funções são trechos de códigos usados para
 replicar determinada ação ao longo do seu código.
 Elas podem receber valores para parâmetros (argumentos)
 e retornar um valor específico.
 Por padrão, funções Python retornam None (nada).
"""

# def feira(a, b, c):
#     print('Banana')
#     print('Morango')
#     print('Laranja')

# feira(1, 2, 3)

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

# def saudacao(nome = 'Sem nome'):
#     print(f'Olá, {nome}!')

# saudacao('Josiel')
# saudacao('Ana')
# saudacao()

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1,2)
soma(3,5)
soma(100,200)
soma(100,200, 0)
soma(x=7, z=9, y=0) # fora de ordem