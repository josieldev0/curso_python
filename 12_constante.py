'''
CONSTANTE = variáveis que não vão mudar
Muitas condições no mesmo if (ruim)
... <- complexidade (ruim)
'''

velocidade = 61 # velocidade do carro
local_carro = 104 # local que o carro está

RADAR_1 = 60 # velocidade máxima radar
LOCAL_1 = 100 # local radar 1
RADAR_RANGE = 1 # distancia que radar pega

vel_carro_passou = velocidade > RADAR_1
carro_passou_cima = local_carro >=(LOCAL_1 - RADAR_RANGE)
carro_passou_baixo = local_carro<= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_cima and carro_passou_baixo and vel_carro_passou

if vel_carro_passou:
    print('Passou da velocidade')

if carro_passou_cima and carro_passou_baixo:
    print('Carro passou no radar')
    
if carro_multado:
    print('Carro multado')