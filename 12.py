# -*- coding: utf-8 -*-
#neste eu adicione a plotagem dos dados para ficar melhor de compreender nos casos de fazer manual
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# (a) Hipóteses
# H0: μ = 8 (o número médio de horas de sono dos alunos é igual a 8 horas)
# H1: μ ≠ 8 (o número médio de horas de sono dos alunos é diferente de 8 horas)

# (b) Teste de Hipótese com amostra de 10 alunos
amostra_10 = np.array([8, 7, 7, 8, 7, 8, 9, 7, 7, 6.5])
n = len(amostra_10)
media_amostra_10 = np.mean(amostra_10)
desvio_padrao_amostra_10 = np.std(amostra_10, ddof=1)
nivel_significancia = 0.05

erro_padrao_10 = desvio_padrao_amostra_10 / np.sqrt(n)

# Estatística t calculada
t_calculado_10 = (media_amostra_10 - 8) / erro_padrao_10

# Valor crítico t para o nível de significância de 5%
grau_liberdade = n - 1
t_critico_10 = stats.t.ppf(1 - nivel_significancia / 2, grau_liberdade)

print("(b) Teste de Hipótese com Amostra de 10 Alunos")
print(f"Estatística t calculada: {t_calculado_10:.4f}")
print(f"Valor crítico t para {nivel_significancia:.2f} de significância: ±{t_critico_10:.4f}")

# Conclusão
def conclusao(t_calculado, t_critico):
    if abs(t_calculado) > t_critico:
        return "Conclusão: Há evidência suficiente para rejeitar a hipótese nula. O número médio de horas de sono é significativamente diferente de 8 horas."
    else:
        return "Conclusão: Não há evidência suficiente para rejeitar a hipótese nula. O número médio de horas de sono não é significativamente diferente de 8 horas."

print(conclusao(t_calculado_10, t_critico_10))

# Representação gráfica do teste com amostra de 10 alunos
t_vals = np.linspace(-4, 4, 400)
y_vals = stats.t.pdf(t_vals, grau_liberdade)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_vals, label='Distribuição t de Student', color='blue')
plt.fill_between(t_vals, y_vals, where=(t_vals < -t_critico_10) | (t_vals > t_critico_10), color='red', alpha=0.3, label='Região Crítica (Rejeitar H0)')
plt.axvline(t_calculado_10, color='green', linestyle='--', label=f'Estatística t calculada ({t_calculado_10:.4f})')
plt.axvline(-t_critico_10, color='red', linestyle='--', label=f'Valor crítico -t ({-t_critico_10:.4f})')
plt.axvline(t_critico_10, color='red', linestyle='--', label=f'Valor crítico t ({t_critico_10:.4f})')
plt.xlabel('Valores t')
plt.ylabel('Densidade de Probabilidade')
plt.title('Teste de Hipótese para Número de Horas de Sono (Amostra de 10 Alunos)')
plt.legend()
plt.grid()
plt.show()

# (c) Teste de Hipótese com amostra de 100 alunos
n_100 = 100
media_amostra_100 = 7.55
desvio_padrao_amostra_100 = 0.81

erro_padrao_100 = desvio_padrao_amostra_100 / np.sqrt(n_100)

# Estatística z calculada
z_calculado_100 = (media_amostra_100 - 8) / erro_padrao_100

# Valor crítico z para o nível de significância de 5%
z_critico_100 = stats.norm.ppf(1 - nivel_significancia / 2)

print("\n(c) Teste de Hipótese com Amostra de 100 Alunos")
print(f"Estatística z calculada: {z_calculado_100:.4f}")
print(f"Valor crítico z para {nivel_significancia:.2f} de significância: ±{z_critico_100:.4f}")

# Conclusão para amostra de 100 alunos
if abs(z_calculado_100) > z_critico_100:
    conclusao_100 = "Conclusão: Há evidência suficiente para rejeitar a hipótese nula. O número médio de horas de sono é significativamente diferente de 8 horas."
else:
    conclusao_100 = "Conclusão: Não há evidência suficiente para rejeitar a hipótese nula. O número médio de horas de sono não é significativamente diferente de 8 horas."

print(conclusao_100)