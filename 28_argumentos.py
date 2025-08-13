"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma (x, y, z):  # ()=parametros
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)
# or             y={y}

soma(5, 10, 1)  # ()=argumentos
soma(12, 10, 1)
#or argumento nomeado 
soma (y=10, x=5, z=5)
print(1, 2, 3, sep='-')

# toda vez que nomear um argumento 
# todos os prox. terão que ser nomeados