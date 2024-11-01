## Enunciados

1. Admita que o número de consultas a uma página inicial de uma determinada empresa, durante um período de tempo, obedece a uma distribuição de Poisson e que, em média, há duas consultas por dia. Pergunta-se:

Qual a probabilidade de que em um determinado:
   - (a) **Dia** sejam feitas exatamente **três consultas**?
   - (b) **Semana** (7 dias) sejam feitas no **máximo dez consultas**?
   - (c) **Mês** (30 dias) sejam feitas **pelo menos cinquenta consultas**?

## Resolução

Para resolver estas questões, utilizamos a fórmula da distribuição de Poisson:

\[
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
\]

Onde:
- \( \lambda \) é a média esperada de eventos no intervalo especificado.
- \( k \) é o número de ocorrências que queremos encontrar.

### (a) Probabilidade de exatamente 3 consultas em um dia

- Média diária (\(\lambda\)) = 2 consultas
- Queremos a probabilidade de exatamente 3 consultas (\(k = 3\))

Utilizamos a função `poisson.pmf(k, lambda)` da biblioteca `scipy` para calcular a probabilidade de um número específico de ocorrências.

### (b) Probabilidade de no máximo 10 consultas em uma semana

- Média semanal (\(\lambda\)) = 2 consultas/dia * 7 dias = 14 consultas
- Queremos a probabilidade de no máximo 10 consultas (\(P(X \leq 10)\))

Utilizamos a função `poisson.cdf(k, lambda)` para calcular a probabilidade acumulada até 10 ocorrências.

### (c) Probabilidade de pelo menos 50 consultas em um mês

- Média mensal (\(\lambda\)) = 2 consultas/dia * 30 dias = 60 consultas
- Queremos a probabilidade de pelo menos 50 consultas (\(P(X \geq 50)\))

Utilizamos a complementaridade: \(P(X \geq 50) = 1 - P(X \leq 49)\). A função `poisson.cdf(k, lambda)` calcula a probabilidade acumulada até 49 ocorrências, e subtraímos o resultado de 1.


## 2. Os dados históricos de uma rede de computadores sugerem que as conexões com essa rede, em horário normal, seguem uma distribuição de Poisson com uma média de **cinco conexões por minuto**. Pergunta-se:

Qual é o tempo \( t_0 \) tal que a probabilidade de ocorrer **pelo menos uma conexão** antes do tempo \( t_0 \) seja igual a **0,90**?

## Resolução

Para determinar o tempo \( t_0 \) tal que a probabilidade de pelo menos uma conexão antes do tempo \( t_0 \) seja igual a 0,90, consideramos:

- Média de conexões por minuto (\(\lambda\)) = 5
- Queremos a probabilidade de pelo menos uma conexão (\(P(X \geq 1) = 0,90\))

Podemos usar a complementaridade:

\[
P(X \geq 1) = 1 - P(X = 0)
\]

Assim, \(P(X = 0) = 0,10\), e utilizamos a fórmula:

\[
P(X = 0) = e^{-\lambda t_0}
\]

Igualando a \(0,10\), obtemos:

\[
t_0 = -\frac{\ln(0,10)}{\lambda}
\]

Este script calcula a probabilidade de que ocorram mais de 120 requisições em um sistema de banco de dados durante o próximo minuto, utilizando a aproximação normal com correção de continuidade.

## 3. No horário de maior movimento, um sistema de banco de dados recebe, em média, **100 requisições por minuto**, segundo uma distribuição de Poisson. Pergunta-se:

Qual é a probabilidade de que no próximo minuto ocorram **mais de 120 requisições**? Use a **aproximação normal com correção de continuidade**.

## Resolução

Para resolver esta questão, utilizamos a **aproximação normal** para a distribuição de Poisson, visto que a média é grande (\(\lambda = 100\)). A aproximação normal pode ser usada para simplificar o cálculo da probabilidade.

### Parâmetros da Aproximação Normal

- Média (\(\mu\)) = 100
- Desvio padrão (\(\sigma\)) = \(\sqrt{\lambda} = \sqrt{100} = 10\)

Como queremos a probabilidade de ocorrer **mais de 120 requisições**, aplicamos a **correção de continuidade**, considerando \(P(X > 120) \approx P(X > 120.5)\).

### Cálculo do Valor-Z

\[
Z = \frac{X - \mu}{\sigma}
\]

Substituindo os valores:

\[
Z = \frac{120.5 - 100}{10} = 2.05
\]

A probabilidade desejada é \(P(X > 120.5)\), que pode ser obtida usando a função de distribuição acumulada (CDF) da distribuição normal:

\[
P(X > 120.5) = 1 - \Phi(Z)
\]

## 4. Suponha que o tempo de resposta na execução de um algoritmo seja uma variável aleatória com distribuição normal de média **23 segundos** e desvio padrão de **4 segundos**. Pergunta-se:

1. Qual é a probabilidade de que o tempo de resposta seja **menor do que 25 segundos**?
2. Qual é a probabilidade de que o tempo de resposta fique **entre 0 e 30 segundos**?

## Resolução

Para resolver esta questão, utilizamos a distribuição normal, caracterizada pela média (\(\mu\)) e o desvio padrão (\(\sigma\)). Usamos a função de distribuição acumulada (CDF) para calcular as probabilidades desejadas.

### (a) Probabilidade de o tempo de resposta ser menor do que 25 segundos

- Média (\(\mu\)) = 23 segundos
- Desvio padrão (\(\sigma\)) = 4 segundos

A probabilidade de que o tempo de resposta seja menor do que 25 segundos pode ser obtida diretamente da função de distribuição acumulada:

\[
P(X < 25) = \Phi\left(\frac{25 - 23}{4}\right)
\]

Utilizamos a função `norm.cdf(x, mu, sigma)` da biblioteca `scipy.stats` para calcular a probabilidade acumulada até 25 segundos.

### (b) Probabilidade de o tempo de resposta ficar entre 0 e 30 segundos

Para calcular a probabilidade do tempo de resposta estar entre 0 e 30 segundos, subtraímos a CDF em 0 da CDF em 30:

\[
P(0 < X < 30) = \Phi\left(\frac{30 - 23}{4}\right) - \Phi\left(\frac{0 - 23}{4}\right)
\]

## Intervalo de confiança para méedia

## 1. (5.py) Um analista de sistemas está avaliando o desempenho de um novo programa de análise numérica. Forneceu como entrada do programa **14 operações similares** e obteve os seguintes tempos de processamento (em milissegundos):

`12,0 - 13,5 - 16,0 - 15,7 - 15,8 - 16,5 - 15,0 - 13,1 - 15,2 - 18,1 - 18,5 - 12,3 - 17,5 - 17,0`

Pergunta-se:

1. (a) Calcule a **média** e o **desvio padrão** da amostra do tempo de processamento.
2. (b) Construa um **intervalo de confiança** para o tempo médio de processamento, com nível de confiança de **95%**.
3. (c) Qual deve ser o **tamanho da amostra** para garantir um erro amostral máximo de **0,5 milissegundo**, na estimação do tempo médio de processamento, com nível de confiança de **99%**?

## Resolução

### (a) Cálculo da Média e Desvio Padrão da Amostra

- **Média da amostra**: Calculada usando a fórmula da média aritmética.
- **Desvio padrão da amostra**: Calculado usando a fórmula do desvio padrão com correção de Bessel (\(ddof=1\)).

### (b) Intervalo de Confiança para a Média

O **intervalo de confiança** foi construído com nível de confiança de 95%, utilizando a distribuição **t de Student**, pois o tamanho da amostra é pequeno (\(n < 30\)). A margem de erro é dada por:

\[
ME = t_{\alpha/2} \cdot \frac{s}{\sqrt{n}}
\]

Onde:
- \( t_{\alpha/2} \) é o valor crítico da distribuição t.
- \( s \) é o desvio padrão da amostra.
- \( n \) é o tamanho da amostra.

### (c) Tamanho da Amostra para Erro Máximo de 0,5 ms

Para calcular o **tamanho da amostra** necessário para garantir um erro amostral máximo de 0,5 milissegundo com nível de confiança de 99%, utilizamos a distribuição normal padrão, pois estamos estimando um tamanho de amostra futuro:

\[
n = \left( \frac{z_{\alpha/2} \cdot s}{E} \right)^2
\]

Onde:
- \( z_{\alpha/2} \) é o valor crítico da distribuição normal.
- \( s \) é o desvio padrão da amostra.
- \( E \) é o erro amostral máximo permitido.

## 2. (6.py) Fixados certos parâmetros de entrada, o tempo de execução de um algoritmo foi medido **12 vezes**, obtendo-se os seguintes resultados, em minutos:

`15, 12, 14, 15, 16, 14, 16, 13, 14, 11, 15, 13`

Pergunta-se:

1. (a) Apresente um **intervalo de 95% de confiança** para o tempo médio de execução do algoritmo.
2. (b) Considerando as 12 mensurações como uma **amostra piloto**, avalie o **número de mensurações** (tamanho da amostra) necessário para garantir um **erro máximo de 15 segundos (0,25 minutos)**, com nível de confiança de **95%**.

## Resolução

### (a) Intervalo de Confiança de 95% para o Tempo Médio de Execução

O **intervalo de confiança** foi construído com nível de confiança de 95%, utilizando a distribuição **t de Student**, pois o tamanho da amostra é pequeno (\(n < 30\)). A margem de erro é dada por:

\[
ME = t_{\alpha/2} \cdot \frac{s}{\sqrt{n}}
\]

Onde:
- \( t_{\alpha/2} \) é o valor crítico da distribuição t.
- \( s \) é o desvio padrão da amostra.
- \( n \) é o tamanho da amostra.

### (b) Tamanho da Amostra para Erro Máximo de 0,25 Minutos

Para calcular o **tamanho da amostra** necessário para garantir um erro amostral máximo de 0,25 minutos com nível de confiança de 95%, utilizamos a distribuição normal padrão, pois estamos estimando um tamanho de amostra futuro:

\[
n = \left( \frac{z_{\alpha/2} \cdot s}{E} \right)^2
\]

Onde:
- \( z_{\alpha/2} \) é o valor crítico da distribuição normal.
- \( s \) é o desvio padrão da amostra.
- \( E \) é o erro amostral máximo permitido.

## 3. (7.py) Uma indústria afirma que as baterias usadas em seus jogos eletrônicos durarão, em média, **30 horas**. Para manter essa média, são testadas **16 baterias** a cada mês. Se os valores calculados de **T** estiverem entre **-t_{0,025}** e **t_{0,025}**, a empresa fica satisfeita com sua afirmação.

Pergunta-se: A que conclusão a empresa deveria chegar se uma amostra que tem uma **média de 27,5 horas** e **desvio-padrão de 5 horas** for utilizada? Assuma que a vida útil das baterias é aproximadamente normal.

## Resolução

Para resolver esta questão, realizamos um **teste t de Student** para avaliar se a média da amostra é significativamente diferente da média hipotética de 30 horas.

### Passos do Teste de Hipótese

1. **Hipóteses**:
   - \( H_0 \): A média de duração das baterias é igual a 30 horas (\( \mu = 30 \)).
   - \( H_1 \): A média de duração das baterias é diferente de 30 horas (\( \mu \neq 30 \)).

2. **Nível de Significância**: Utilizamos um nível de significância de 5% (\( \alpha = 0,05 \)).

3. **Estatística t Calculada**:
   - A estatística t é calculada como:
   \[
   t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
   \]
   Onde:
   - \( \bar{x} \) é a média da amostra.
   - \( \mu_0 \) é a média hipotética.
   - \( s \) é o desvio padrão da amostra.
   - \( n \) é o tamanho da amostra.

4. **Valores Críticos**:
   - Determinamos os valores críticos para o nível de significância de 0,05, usando a distribuição t com \( n - 1 \) graus de liberdade.

5. **Conclusão**:
   - Se a estatística t calculada estiver entre os valores críticos, não rejeitamos a hipótese nula.
   - Caso contrário, rejeitamos a hipótese nula.

### Representação Gráfica

## 1. (8py) O script também gera uma **representação gráfica** da distribuição t de Student, destacando a região crítica (em vermelho) e a estatística t calculada (em verde).

Uma unidade fabril da Intel produziu **500.000 chips Pentium IV** em certo período. Foram selecionados, aleatoriamente, **400 chips** para testes.

1. (a) Supondo que **20 chips** não tenham a velocidade de processamento adequada, construa um **intervalo de confiança** para a proporção de chips adequados. Use nível de confiança de **95%**.
2. (b) Verifique se essa amostra é suficiente para obter um intervalo de **99% de confiança**, com **erro amostral máximo de 0,5%**, para a proporção de chips adequados. Caso contrário, qual deveria ser o tamanho da amostra?

## Resolução

### (a) Intervalo de Confiança para a Proporção de Chips Adequados

O **intervalo de confiança** foi construído com nível de confiança de 95%, utilizando a distribuição **normal** para estimar a proporção de chips adequados. A margem de erro é dada por:

\[
ME = z_{\alpha/2} \cdot \sqrt{\frac{p (1 - p)}{n}}
\]

Onde:
- \( z_{\alpha/2} \) é o valor crítico da distribuição normal.
- \( p \) é a proporção de chips adequados na amostra.
- \( n \) é o tamanho da amostra.

### (b) Tamanho da Amostra Necessário para Intervalo de Confiança de 99%

Para calcular o **tamanho da amostra** necessário para garantir um erro amostral máximo de 0,5% com nível de confiança de 99%, utilizamos a fórmula:

\[
n = \left( \frac{z_{\alpha/2}^2 \cdot p (1 - p)}{E^2} \right)
\]

Onde:
- \( z_{\alpha/2} \) é o valor crítico da distribuição normal para um nível de confiança de 99%.
- \( p \) é a proporção de chips adequados na amostra.
- \( E \) é o erro amostral máximo permitido.

### Representação Gráfica

O script também gera uma **representação gráfica** da distribuição normal da proporção de chips adequados, destacando o intervalo de confiança de 95%.

## 1. (9.py) Para testar se um sistema computacional "inteligente" adquiriu algum conhecimento sobre determinado assunto, elaborou-se **60 questões do tipo certo-errado**. O sistema acertou **40**. Qual é a conclusão ao nível de significância de **5%**?

## Resolução

Para resolver esta questão, realizamos um **teste de hipótese para proporções**.

### Hipóteses

- **Hipótese nula (\(H_0\))**: A proporção de acertos é igual a 0,5 (\(p = 0,5\)), ou seja, o sistema acerta ao acaso.
- **Hipótese alternativa (\(H_1\))**: A proporção de acertos é maior que 0,5 (\(p > 0,5\)), ou seja, o sistema adquiriu algum conhecimento.

### Nível de Significância

Utilizamos um nível de significância de **5%** (\(\alpha = 0,05\)).

### Estatística z Calculada

A estatística z é calculada como:

\[
z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1 - p_0)}{n}}}
\]

Onde:
- \(\hat{p}\) é a proporção de acertos na amostra.
- \(p_0\) é a proporção hipotética (0,5).
- \(n\) é o tamanho da amostra (60).

### Valor Crítico z

O valor crítico \(z_{\alpha}\) para um teste unilateral à direita com nível de significância de 5% é determinado usando a **distribuição normal padrão**.

### Conclusão

- Se \(z_{calculado} > z_{crítico}\), rejeitamos a hipótese nula e concluímos que o sistema adquiriu conhecimento.
- Caso contrário, não rejeitamos a hipótese nula.

### Representação Gráfica

O script também gera uma **representação gráfica** da distribuição normal padrão, destacando a região crítica (em vermelho) e a estatística z calculada (em verde).

## 2. (10.py) Em certo banco de dados, o tempo para realização de buscas é aproximadamente normal, com média de **53 segundos** e desvio padrão de **14 segundos**. Depois de realizadas algumas modificações no sistema, observou-se que, em **30 consultas**, o tempo médio caiu para **45 segundos**. Há evidência de melhora? Admita que as 30 observações possam ser consideradas uma amostra aleatória e que não houve variação no desvio padrão. Use **α = 1%**.

## Resolução

Para resolver esta questão, realizamos um **teste t de Student** para avaliar se a média do tempo de busca após as modificações é significativamente menor do que a média anterior.

### Hipóteses

- **Hipótese nula (\(H_0\))**: A média do tempo de busca é igual a 53 segundos (\(\mu = 53\)).
- **Hipótese alternativa (\(H_1\))**: A média do tempo de busca é menor do que 53 segundos (\(\mu < 53\)).

### Nível de Significância

Utilizamos um nível de significância de **1%** (\(\alpha = 0,01\)).

### Estatística t Calculada

A estatística t é calculada como:

\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]

Onde:
- \(\bar{x}\) é a média da amostra após as modificações.
- \(\mu_0\) é a média hipotética (53 segundos).
- \(s\) é o desvio padrão (14 segundos).
- \(n\) é o tamanho da amostra (30).

### Valor Crítico t

O valor crítico \(t_{\alpha}\) para um teste unilateral à esquerda com nível de significância de 1% é determinado usando a **distribuição t de Student** com \(n - 1\) graus de liberdade.

### Conclusão

- Se \(t_{calculado} < t_{crítico}\), rejeitamos a hipótese nula e concluímos que houve melhora significativa.
- Caso contrário, não rejeitamos a hipótese nula.

### Representação Gráfica

O script também gera uma **representação gráfica** da distribuição t de Student, destacando a região crítica (em vermelho) e a estatística t calculada (em verde).

## 3. (11.py) Para comparar dois algoritmos de otimização, foi realizado um experimento com **seis ensaios**. Em cada ensaio, foram usados separadamente os dois algoritmos em estudo, mas sob as mesmas condições (dados pareados). Os tempos de resposta ao usuário são mostrados na tabela abaixo:

| Ensaio      | 1   | 2   | 3   | 4   | 5   | 6   |
|-------------|-----|-----|-----|-----|-----|-----|
| Algoritmo 1 | 8.1 | 8.9 | 9.3 | 9.6 | 8.1 | 11.2|
| Algoritmo 2 | 9.2 | 9.8 | 9.9 | 10.3| 8.9 | 13.1|

Pergunta-se: **Os tempos de resposta dos dois algoritmos são, em média, diferentes?** Use **α = 0,05**.

## Resolução

Para resolver esta questão, realizamos um **teste t pareado** para avaliar se há diferença significativa entre os tempos de resposta dos dois algoritmos.

### Hipóteses

- **Hipótese nula (\(H_0\))**: A média das diferenças dos tempos de resposta é igual a zero (\(\mu_d = 0\)), ou seja, não há diferença significativa entre os algoritmos.
- **Hipótese alternativa (\(H_1\))**: A média das diferenças dos tempos de resposta é diferente de zero (\(\mu_d \neq 0\)), ou seja, há diferença significativa entre os algoritmos.

### Nível de Significância

Utilizamos um nível de significância de **5%** (\(\alpha = 0,05\)).

### Estatística t Calculada

A estatística t é calculada como:

\[
t = \frac{\bar{d}}{s_d / \sqrt{n}}
\]

Onde:
- \(\bar{d}\) é a média das diferenças entre os tempos de resposta dos dois algoritmos.
- \(s_d\) é o desvio padrão das diferenças.
- \(n\) é o número de ensaios (6).

### Valor Crítico t

O valor crítico \(t_{\alpha/2}\) para um teste bilateral com nível de significância de 5% é determinado usando a **distribuição t de Student** com \(n - 1\) graus de liberdade.

### Conclusão

- Se \(|t_{calculado}| > t_{crítico}\), rejeitamos a hipótese nula e concluímos que os tempos de resposta são, em média, diferentes.
- Caso contrário, não rejeitamos a hipótese nula.

### Representação Gráfica

O script também gera uma **representação gráfica** da distribuição t de Student, destacando a região crítica (em vermelho) e a estatística t calculada (em verde).

## 4. (12.py) Sabe-se que é ideal um sono de **8 horas por dia**. Pesquisadores acreditam que o número médio de horas de sono dos alunos de certo curso pode ser **maior ou menor que 8 horas**. Podemos considerar que o número médio de horas de sono segue uma distribuição normal. Uma amostra de **10 alunos** forneceu os seguintes valores para o número de horas de sono:

`8; 7; 7; 8; 7; 8; 9; 7; 7; 6,5`

1. **(a)** Quais hipóteses estão sendo testadas?
2. **(b)** Construa a região crítica adotando nível de significância de **5%** e conclua o teste.
3. **(c)** Se agora temos uma amostra de **100 alunos** e obtemos uma média amostral igual a **7,55 horas** e desvio padrão amostral de **0,81 hora**, como fica a região crítica e a conclusão do teste adotando nível de significância de **5%**?

## Resolução

### (a) Hipóteses

- **Hipótese nula (\(H_0\))**: O número médio de horas de sono dos alunos é igual a 8 horas (\(\mu = 8\)).
- **Hipótese alternativa (\(H_1\))**: O número médio de horas de sono dos alunos é diferente de 8 horas (\(\mu \neq 8\)).

### (b) Teste de Hipótese com Amostra de 10 Alunos

Utilizamos um **teste t de Student** para avaliar se há uma diferença significativa, dado o tamanho pequeno da amostra (\(n = 10\)). Calculamos a estatística t e comparamos com o valor crítico da distribuição t com 9 graus de liberdade e nível de significância de 5%.

### (c) Teste de Hipótese com Amostra de 100 Alunos

Com uma amostra maior (\(n = 100\)), utilizamos a **distribuição normal padrão** para calcular a estatística z e o valor crítico z para o nível de significância de 5%. O teste determina se a média de 7,55 horas é significativamente diferente de 8 horas.

### Representação Gráfica

O script também gera uma **representação gráfica** da distribuição t de Student para a amostra de 10 alunos, destacando a região crítica e a estatística t calculada.

## Bibliotecas Utilizadas
- `math`: Utilizada para calcular o logaritmo natural.
- `math`: Utilizada para calcular a raiz quadrada.
- `numpy`: Utilizada para calcular a média e operações matemáticas.
- `numpy`: Utilizada para operações matemáticas.
- `scipy.stats`: Utilizada para calcular valores críticos da distribuição t.
- `scipy.stats`: Utilizada para calcular valores críticos da distribuição t e normal.
- `scipy.stats`: Utilizada para calcular a distribuição normal acumulada.
- `scipy.stats`: Utilizada para calcular as probabilidades da distribuição de Poisson.
- `scipy.stats`: Utilizada para calcular a distribuição normal acumulada.
- `matplotlib`: Utilizada para gerar a representação gráfica.

## Como Executar
Para executar este script, é necessário ter Python e a biblioteca `scipy` instalados. Você pode instalar a biblioteca usando o seguinte comando:

```
pip install scipy
```

Depois, basta rodar o script em um terminal Python:

```
python nome_do_script.py
```

"""