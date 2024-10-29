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


## Bibliotecas Utilizadas
- `scipy.stats`: Utilizada para calcular as probabilidades da distribuição de Poisson.

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