# -*- coding: utf-8 -*-
#neste eu adicione a plotagem dos dados para ficar melhor de compreender nos casos de fazer manual
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# (a) Construir o intervalo de confiança para a proporção de chips adequados
n = 400  # tamanho da amostra
chips_defeituosos = 20  # número de chips defeituosos
chips_adequados = n - chips_defeituosos  # número de chips adequados

p_amostra = chips_adequados / n  # proporção de chips adequados na amostra
nivel_confianca = 0.95
z_critico = stats.norm.ppf((1 + nivel_confianca) / 2)

erro_padrao = np.sqrt((p_amostra * (1 - p_amostra)) / n)
margem_erro = z_critico * erro_padrao

limite_inferior = p_amostra - margem_erro
limite_superior = p_amostra + margem_erro

print(f"(a) Intervalo de confiança de 95% para a proporção de chips adequados: ({limite_inferior:.4f}, {limite_superior:.4f})")

# (b) Verificar se a amostra é suficiente para obter um intervalo de 99% de confiança com erro amostral máximo de 0,5%
nivel_confianca_99 = 0.99
z_critico_99 = stats.norm.ppf((1 + nivel_confianca_99) / 2)
erro_amostral = 0.005  # 0,5% = 0,005

tamanho_amostra_necessario = (z_critico_99 ** 2 * p_amostra * (1 - p_amostra)) / (erro_amostral ** 2)
tamanho_amostra_necessario = int(np.ceil(tamanho_amostra_necessario))

if n >= tamanho_amostra_necessario:
    conclusao = "A amostra atual é suficiente para obter um intervalo de 99% de confiança com erro amostral máximo de 0,5%."
else:
    conclusao = f"A amostra atual não é suficiente. O tamanho da amostra necessário é de {tamanho_amostra_necessario}."

print(f"(b) {conclusao}")

# Representação gráfica do intervalo de confiança
proporcoes = np.linspace(0, 1, 1000)
y_vals = stats.norm.pdf(proporcoes, p_amostra, erro_padrao)

plt.figure(figsize=(10, 6))
plt.plot(proporcoes, y_vals, label='Distribuição Normal da Proporção', color='blue')
plt.fill_between(proporcoes, y_vals, where=(proporcoes >= limite_inferior) & (proporcoes <= limite_superior), color='green', alpha=0.3, label='Intervalo de Confiança 95%')
plt.axvline(p_amostra, color='black', linestyle='--', label=f'Proporção amostral ({p_amostra:.4f})')
plt.axvline(limite_inferior, color='red', linestyle='--', label=f'Limite Inferior ({limite_inferior:.4f})')
plt.axvline(limite_superior, color='red', linestyle='--', label=f'Limite Superior ({limite_superior:.4f})')
plt.xlabel('Proporção de Chips Adequados')
plt.ylabel('Densidade de Probabilidade')
plt.title('Intervalo de Confiança para Proporção de Chips Adequados')
plt.legend()
plt.grid()
plt.show()