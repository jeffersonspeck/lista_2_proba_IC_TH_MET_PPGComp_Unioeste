# -*- coding: utf-8 -*-
import math

# (2) Tempo t0 para probabilidade de pelo menos uma conexão em uma rede de computadores
# Média de conexões por minuto
lambda_connections = 5

# Probabilidade de pelo menos uma conexão antes do tempo t0 deve ser 0,90
# Calculamos o tempo t0 tal que P(X = 0) = 0,10
prob_zero = 0.10
t_0 = -math.log(prob_zero) / lambda_connections
print(f"Tempo t0 para probabilidade de pelo menos uma conexão: {t_0:.4f} minutos")