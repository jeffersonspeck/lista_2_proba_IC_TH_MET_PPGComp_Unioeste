# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats

# Dados da amostra
tempos = [12.0, 13.5, 16.0, 15.7, 15.8, 16.5, 15.0, 13.1, 15.2, 18.1, 18.5, 12.3, 17.5, 17.0]

# (a) Calcule a média e o desvio padrão da amostra do tempo de processamento
media_amostra = np.mean(tempos)
desvio_padrao_amostra = np.std(tempos, ddof=1)

print(f"(a) Média da amostra: {media_amostra:.2f} ms")
print(f"(a) Desvio padrão da amostra: {desvio_padrao_amostra:.2f} ms")

# (b) Construir um intervalo de confiança para o tempo médio de processamento, com nível de confiança de 95%
n = len(tempos)
nivel_confianca = 0.95
grau_liberdade = n - 1
t_critico = stats.t.ppf((1 + nivel_confianca) / 2, grau_liberdade)
erro_padrao = desvio_padrao_amostra / np.sqrt(n)

margem_erro = t_critico * erro_padrao
limite_inferior = media_amostra - margem_erro
limite_superior = media_amostra + margem_erro

print(f"(b) Intervalo de confiança de 95% para a média: ({limite_inferior:.2f}, {limite_superior:.2f}) ms")

# (c) Tamanho da amostra para garantir um erro amostral máximo de 0,5 ms, com nível de confiança de 99%
nivel_confianca_99 = 0.99
z_critico = stats.norm.ppf((1 + nivel_confianca_99) / 2)
erro_amostral = 0.5

tamanho_amostra = (z_critico * desvio_padrao_amostra / erro_amostral) ** 2
tamanho_amostra = int(np.ceil(tamanho_amostra))

print(f"(c) Tamanho da amostra necessário para erro máximo de 0,5 ms com 99% de confiança: {tamanho_amostra}")