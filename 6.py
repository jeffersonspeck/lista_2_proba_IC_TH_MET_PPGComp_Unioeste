# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats

# Dados da amostra
tempos = [15, 12, 14, 15, 16, 14, 16, 13, 14, 11, 15, 13]

# (a) Construir um intervalo de confiança de 95% para o tempo médio de execução do algoritmo
media_amostra = np.mean(tempos)
desvio_padrao_amostra = np.std(tempos, ddof=1)
n = len(tempos)
nivel_confianca = 0.95
grau_liberdade = n - 1
t_critico = stats.t.ppf((1 + nivel_confianca) / 2, grau_liberdade)
erro_padrao = desvio_padrao_amostra / np.sqrt(n)

margem_erro = t_critico * erro_padrao
limite_inferior = media_amostra - margem_erro
limite_superior = media_amostra + margem_erro

print(f"(a) Intervalo de confiança de 95% para a média: ({limite_inferior:.2f}, {limite_superior:.2f}) minutos")

# (b) Tamanho da amostra necessário para garantir um erro máximo de 0,25 minutos com nível de confiança de 95%
nivel_confianca_95 = 0.95
z_critico = stats.norm.ppf((1 + nivel_confianca_95) / 2)
erro_amostral = 0.25

tamanho_amostra = (z_critico * desvio_padrao_amostra / erro_amostral) ** 2
tamanho_amostra = int(np.ceil(tamanho_amostra))

print(f"(b) Tamanho da amostra necessário para erro máximo de 0,25 minutos com 95% de confiança: {tamanho_amostra}")
