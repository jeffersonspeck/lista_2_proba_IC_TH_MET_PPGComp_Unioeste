# -*- coding: utf-8 -*-
from scipy.stats import norm

# (4) Tempo de resposta de um algoritmo com distribuição normal
# Média e desvio padrão
mu = 23  # média em segundos
sigma = 4  # desvio padrão em segundos

# (a) Probabilidade de o tempo de resposta ser menor do que 25 segundos
prob_less_than_25 = norm.cdf(25, mu, sigma)
print(f"(a) Probabilidade de o tempo de resposta ser menor do que 25 segundos: {prob_less_than_25:.4f}")

# (b) Probabilidade de o tempo de resposta ficar entre 0 e 30 segundos
prob_between_0_and_30 = norm.cdf(30, mu, sigma) - norm.cdf(0, mu, sigma)
print(f"(b) Probabilidade de o tempo de resposta ficar entre 0 e 30 segundos: {prob_between_0_and_30:.4f}")