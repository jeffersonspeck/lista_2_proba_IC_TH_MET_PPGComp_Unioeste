# -*- coding: utf-8 -*-
import math
from scipy.stats import norm

# (3) Probabilidade de mais de 120 requisições em um minuto
# Média de requisições por minuto
lambda_requests = 100

# Aproximação normal com correção de continuidade
mu = lambda_requests
sigma = math.sqrt(lambda_requests)

# Correção de continuidade: queremos P(X > 120) -> P(X > 120.5)
z = (120.5 - mu) / sigma
prob_more_than_120 = 1 - norm.cdf(z)

print(f"Probabilidade de mais de 120 requisições em um minuto: {prob_more_than_120:.4f}")