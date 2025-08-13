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

def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Josiel')
saudacao('Ana')
saudacao()
