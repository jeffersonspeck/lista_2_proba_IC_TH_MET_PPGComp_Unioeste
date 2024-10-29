# -*- coding: utf-8 -*-
#neste eu adicione a plotagem dos dados para ficar melhor de compreender nos casos de fazer manual
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados da amostra
media_amostra = 27.5  # média da amostra em horas
desvio_padrao_amostra = 5  # desvio padrão da amostra em horas
n = 16  # tamanho da amostra
media_hipotese = 30  # média hipotética em horas

# Nível de significância
alpha = 0.05
grau_liberdade = n - 1

# Estatística t calculada
erro_padrao = desvio_padrao_amostra / np.sqrt(n)
t_calculado = (media_amostra - media_hipotese) / erro_padrao

# Valores críticos t para o nível de significância de 0,05
t_critico = stats.t.ppf(1 - alpha / 2, grau_liberdade)

print(f"Estatística t calculada: {t_calculado:.4f}")
print(f"Valor crítico t para {alpha / 2:.3f} de significância: ±{t_critico:.4f}")

# Conclusão
if -t_critico <= t_calculado <= t_critico:
    conclusao = "A empresa deve concluir que não há evidência suficiente para rejeitar a afirmação de que a média de duração das baterias é de 30 horas."
else:
    conclusao = "A empresa deve concluir que há evidência suficiente para rejeitar a afirmação de que a média de duração das baterias é de 30 horas."

print(f"Conclusão: {conclusao}")

# Representação gráfica
t_vals = np.linspace(-4, 4, 400)
y_vals = stats.t.pdf(t_vals, grau_liberdade)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_vals, label='Distribuição t de Student', color='blue')
plt.fill_between(t_vals, y_vals, where=(t_vals < -t_critico) | (t_vals > t_critico), color='red', alpha=0.3, label='Região Crítica')
plt.axvline(t_calculado, color='green', linestyle='--', label=f'Estatística t calculada ({t_calculado:.4f})')
plt.axvline(-t_critico, color='red', linestyle='--', label=f'Valor crítico -t ({-t_critico:.4f})')
plt.axvline(t_critico, color='red', linestyle='--', label=f'Valor crítico t ({t_critico:.4f})')
plt.xlabel('Valores t')
plt.ylabel('Densidade de Probabilidade')
plt.title('Teste de Hipótese para Vida Útil de Baterias')
plt.legend()
plt.grid()
plt.show()