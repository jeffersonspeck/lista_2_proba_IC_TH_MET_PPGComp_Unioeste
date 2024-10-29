# -*- coding: utf-8 -*-
# Enunciado
# Distribuições de Probabilidades

# Admita que o número de consultas a uma página inicial de uma determinada empresa, durante um período de tempo, obedece a uma distribuição de Poisson e que em média há duas consultas por dia. Pergunta-se:

# Qual a probabilidade de que em um determinado:
# (a) Dia sejam feitas exatamente três consultas?
# (b) Semana (7 dias) sejam feitas no máximo dez consultas?
# (c) Mês (30 dias) sejam feitas pelo menos cinquenta consultas?
import math
from scipy.stats import poisson

# (a) Probabilidade de exatamente 3 consultas em um dia
lambda_day = 2
k_a = 3
prob_a = poisson.pmf(k_a, lambda_day)
print(f"(a) Probabilidade de exatamente 3 consultas em um dia: {prob_a:.4f}")

# (b) Probabilidade de no máximo 10 consultas em uma semana
lambda_week = 2 * 7
prob_b = poisson.cdf(10, lambda_week)
print(f"(b) Probabilidade de no máximo 10 consultas em uma semana: {prob_b:.4f}")

# (c) Probabilidade de pelo menos 50 consultas em um mês
lambda_month = 2 * 30
prob_c = 1 - poisson.cdf(49, lambda_month)
print(f"(c) Probabilidade de pelo menos 50 consultas em um mês: {prob_c:.4f}")