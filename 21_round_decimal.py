import decimal

numero_1 = decimal.Decimal('0.1') # decimal.Decimal tem que ser em ''
numero_2 = decimal.Decimal('0.7') # só usado em muitas casas decimais
numero_3 = numero_1 + numero_2 

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))