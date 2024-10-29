# -*- coding: utf-8 -*-
#neste eu adicione a plotagem dos dados para ficar melhor de compreender nos casos de fazer manual
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados dos tempos de resposta dos algoritmos
algoritmo_1 = np.array([8.1, 8.9, 9.3, 9.6, 8.1, 11.2])
algoritmo_2 = np.array([9.2, 9.8, 9.9, 10.3, 8.9, 13.1])

# Diferenças pareadas
diferencas = algoritmo_1 - algoritmo_2

# Hipóteses
# H0: μ_d = 0 (não há diferença significativa entre os algoritmos)
# H1: μ_d ≠ 0 (há diferença significativa entre os algoritmos)

# Estatística t calculada
media_diferencas = np.mean(diferencas)
desvio_padrao_diferencas = np.std(diferencas, ddof=1)
n = len(diferencas)
erro_padrao = desvio_padrao_diferencas / np.sqrt(n)
t_calculado = media_diferencas / erro_padrao

# Valor crítico t para o nível de significância de 5%
nivel_significancia = 0.05
grau_liberdade = n - 1
t_critico = stats.t.ppf(1 - nivel_significancia / 2, grau_liberdade)

print(f"Estatística t calculada: {t_calculado:.4f}")
print(f"Valor crítico t para {nivel_significancia:.2f} de significância: ±{t_critico:.4f}")

# Conclusão
def conclusao(t_calculado, t_critico):
    if abs(t_calculado) > t_critico:
        return "Conclusão: Há evidência suficiente para rejeitar a hipótese nula. Os tempos de resposta dos dois algoritmos são, em média, diferentes."
    else:
        return "Conclusão: Não há evidência suficiente para rejeitar a hipótese nula. Os tempos de resposta dos dois algoritmos não são significativamente diferentes."

print(conclusao(t_calculado, t_critico))

# Representação gráfica
t_vals = np.linspace(-4, 4, 400)
y_vals = stats.t.pdf(t_vals, grau_liberdade)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_vals, label='Distribuição t de Student', color='blue')
plt.fill_between(t_vals, y_vals, where=(t_vals < -t_critico) | (t_vals > t_critico), color='red', alpha=0.3, label='Região Crítica (Rejeitar H0)')
plt.axvline(t_calculado, color='green', linestyle='--', label=f'Estatística t calculada ({t_calculado:.4f})')
plt.axvline(-t_critico, color='red', linestyle='--', label=f'Valor crítico -t ({-t_critico:.4f})')
plt.axvline(t_critico, color='red', linestyle='--', label=f'Valor crítico t ({t_critico:.4f})')
plt.xlabel('Valores t')
plt.ylabel('Densidade de Probabilidade')
plt.title('Teste de Hipótese para Comparação de Algoritmos de Otimização')
plt.legend()
plt.grid()
plt.show()