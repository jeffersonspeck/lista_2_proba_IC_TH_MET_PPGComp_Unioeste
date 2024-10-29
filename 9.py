# -*- coding: utf-8 -*-
#neste eu adicione a plotagem dos dados para ficar melhor de compreender nos casos de fazer manual
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados da amostra
n = 60  # número de questões
acertos = 40  # número de acertos
p_amostra = acertos / n  # proporção de acertos

# Hipótese nula: p = 0.5 (o sistema acerta ao acaso)
# Hipótese alternativa: p > 0.5 (o sistema adquiriu algum conhecimento)

p_hipotese = 0.5
nivel_significancia = 0.05

# Estatística z calculada
erro_padrao = np.sqrt((p_hipotese * (1 - p_hipotese)) / n)
z_calculado = (p_amostra - p_hipotese) / erro_padrao

# Valor crítico z para o nível de significância de 5%
z_critico = stats.norm.ppf(1 - nivel_significancia)

print(f"Estatística z calculada: {z_calculado:.4f}")
print(f"Valor crítico z para {nivel_significancia:.2f} de significância: {z_critico:.4f}")

# Conclusão
def conclusao(z_calculado, z_critico):
    if z_calculado > z_critico:
        return "Conclusão: Há evidência suficiente para rejeitar a hipótese nula. O sistema adquiriu algum conhecimento sobre o assunto."
    else:
        return "Conclusão: Não há evidência suficiente para rejeitar a hipótese nula. O sistema não demonstra ter adquirido conhecimento suficiente sobre o assunto."

print(conclusao(z_calculado, z_critico))

# Representação gráfica
t_vals = np.linspace(-3, 3, 400)
y_vals = stats.norm.pdf(t_vals, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, y_vals, label='Distribuição Normal Padrão', color='blue')
plt.fill_between(t_vals, y_vals, where=(t_vals > z_critico), color='red', alpha=0.3, label='Região Crítica (Rejeitar H0)')
plt.axvline(z_calculado, color='green', linestyle='--', label=f'Estatística z calculada ({z_calculado:.4f})')
plt.axvline(z_critico, color='red', linestyle='--', label=f'Valor crítico z ({z_critico:.4f})')
plt.xlabel('Valores z')
plt.ylabel('Densidade de Probabilidade')
plt.title('Teste de Hipótese para Avaliar o Conhecimento do Sistema Computacional')
plt.legend()
plt.grid()
plt.show()