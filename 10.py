# -*- coding: utf-8 -*-
#neste eu adicione a plotagem dos dados para ficar melhor de compreender nos casos de fazer manual
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados da amostra
n = 30  # número de consultas
media_antes = 53  # média antes das modificações (em segundos)
media_depois = 45  # média depois das modificações (em segundos)
desvio_padrao = 14  # desvio padrão (em segundos)
nivel_significancia = 0.01

# Hipóteses
# H0: μ = 53 (não houve melhora significativa)
# H1: μ < 53 (houve melhora significativa)

# Estatística t calculada
erro_padrao = desvio_padrao / np.sqrt(n)
t_calculado = (media_depois - media_antes) / erro_padrao

# Valor crítico t para o nível de significância de 1%
grau_liberdade = n - 1
t_critico = stats.t.ppf(nivel_significancia, grau_liberdade)

print(f"Estatística t calculada: {t_calculado:.4f}")
print(f"Valor crítico t para {nivel_significancia:.2f} de significância: {t_critico:.4f}")

# Conclusão
def conclusao(t_calculado, t_critico):
    if t_calculado < t_critico:
        return "Conclusão: Há evidência suficiente para rejeitar a hipótese nula. Houve melhora significativa no tempo de busca."
    else:
        return "Conclusão: Não há evidência suficiente para rejeitar a hipótese nula. Não houve melhora significativa no tempo de busca."

print(conclusao(t_calculado, t_critico))

# Representação gráfica
t_vals = np.linspace(-4, 4, 400)
y_vals = stats.t.pdf(t_vals, grau_liberdade)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_vals, label='Distribuição t de Student', color='blue')
plt.fill_between(t_vals, y_vals, where=(t_vals < t_critico), color='red', alpha=0.3, label='Região Crítica (Rejeitar H0)')
plt.axvline(t_calculado, color='green', linestyle='--', label=f'Estatística t calculada ({t_calculado:.4f})')
plt.axvline(t_critico, color='red', linestyle='--', label=f'Valor crítico t ({t_critico:.4f})')
plt.xlabel('Valores t')
plt.ylabel('Densidade de Probabilidade')
plt.title('Teste de Hipótese para Tempo de Busca no Banco de Dados')
plt.legend()
plt.grid()
plt.show()
