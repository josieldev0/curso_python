adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)


# Precedência entre os operadores aritméticos
# ordem que é executado os operadore
# 1.(n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5     #7
print(conta_1) 

conta_2 = (1 + 1) ** (5 + 5)    #1024
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_3)

