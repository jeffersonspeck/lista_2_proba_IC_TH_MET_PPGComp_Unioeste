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

## 5. Um analista de sistemas está avaliando o desempenho de um novo programa de análise numérica. Forneceu como entrada do programa **14 operações similares** e obteve os seguintes tempos de processamento (em milissegundos):

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


## Bibliotecas Utilizadas
- `math`: Utilizada para calcular o logaritmo natural.
- `math`: Utilizada para calcular a raiz quadrada.
- `numpy`: Utilizada para calcular a média e operações matemáticas.
- `scipy.stats`: Utilizada para calcular valores críticos da distribuição t e normal.
- `scipy.stats`: Utilizada para calcular a distribuição normal acumulada.
- `scipy.stats`: Utilizada para calcular as probabilidades da distribuição de Poisson.
- `scipy.stats`: Utilizada para calcular a distribuição normal acumulada.

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