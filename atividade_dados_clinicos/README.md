# Modelagem Experimental — Árvore de Decisão

## Alunos:
Thiago Plancke,  
Kauê Lima,  
Vladimir Queiroz,  

## 1. Objetivo

Nesta atividade foi realizada uma modelagem experimental utilizando uma árvore de decisão aplicada a um conjunto de dados clínicos relacionados a doenças cardíacas.

Foram utilizados os conceitos de **partição recursiva** e **pureza dos nós**, analisando o comportamento das folhas, do índice de Gini e das probabilidades estimadas, com foco na construção e interpretação do modelo com profundidade limitada.

---

## 2. Conjunto de dados

O conjunto de dados utilizado contém informações clínicas de pacientes e possui 21 atributos:

- Idade
- Gênero
- Pressão Arterial
- Nível de Colesterol
- Hábitos de Exercício
- Tabagismo
- Histórico Familiar de Doença Cardíaca
- Diabetes
- IMC
- Pressão Arterial Alta
- Colesterol HDL Baixo
- Colesterol LDL Alto
- Consumo de Álcool
- Nível de Estresse
- Horas de Sono
- Consumo de Açúcar
- Nível de Triglicerídeos
- Glicemia em Jejum
- Nível de PCR
- Nível de Homocisteína
- Status de Doença Cardíaca

O atributo utilizado como **target** foi:  
`Status de Doença Cardíaca`

O target possui duas classes:
- `No`
- `Yes`

---

## 3. Pré-processamento

Inicialmente, os registros que continham valores ausentes foram removidos utilizando `dropna()`.

O conjunto original possuía aproximadamente 10.000 registros. Após a remoção dos registros com valores ausentes, restaram:

- **7.067 registros**
- **20 atributos utilizados como features**
- **1 atributo utilizado como target**

As variáveis categóricas binárias foram convertidas para valores numéricos utilizando:

| Valor original | Valor utilizado |
|---|---:|
| No | 0 |
| Yes | 1 |

As variáveis categóricas com três níveis foram convertidas utilizando:

| Valor original | Valor utilizado |
|---|---:|
| Low | 0 |
| Medium | 1 |
| High | 2 |

O atributo `Status de Doença Cardíaca` foi mantido como `No` e `Yes`, pois o `DecisionTreeClassifier` consegue trabalhar diretamente com classes categóricas.

---

## 4. Features e target

As 20 variáveis clínicas foram utilizadas como características de entrada do modelo.

Dessa forma:
- `X` representa as características dos pacientes;
- `y` representa o diagnóstico de doença cardíaca.

O target não foi incluído entre as features, pois ele representa justamente a informação que o modelo deve aprender a prever.

---

## 5. Verificação de colisões

Uma colisão ocorre quando dois registros possuem exatamente os mesmos valores em todas as features, mas apresentam diagnósticos diferentes no target.

Por exemplo:

| Características | Status |
|---|---|
| Mesmo conjunto de atributos | No |
| Mesmo conjunto de atributos | Yes |

Nesse caso, os registros possuem exatamente as mesmas informações de entrada, mas resultados diferentes. Essa situação é importante para a árvore de decisão porque não seria possível criar uma regra baseada somente nas features capaz de separar perfeitamente esses dois registros.

---

## 6. Árvore de decisão sem limite de profundidade

Se a árvore de decisão for criada sem definir um valor para `max_depth`, o algoritmo fica livre para continuar realizando partições recursivas enquanto encontrar divisões capazes de melhorar a separação das classes.

O resultado é uma árvore muito grande. Esse comportamento ocorre porque a árvore continua criando novos nós para tentar aumentar a pureza das folhas.

O índice utilizado para medir essa pureza é o **Gini**. Quanto mais próximo de `0`, mais puro é o nó. Uma folha contendo apenas uma classe pode apresentar `Gini = 0`.

---

## 7. Relação entre Gini e pureza

O índice de Gini indica o grau de mistura entre as classes dentro de um nó.

- Quando `Gini = 0`, o nó é completamente puro (todas as amostras pertencem à mesma classe).
- Quando diferentes classes estão presentes no mesmo nó, o valor de Gini aumenta.

Durante o crescimento da árvore, o algoritmo procura divisões que aumentem a pureza dos nós resultantes.

---

## 8. O modelo com profundidade limitada (`max_depth=6`)

No código desenvolvido, a árvore foi configurada com `max_depth=6` e `random_state=42`, sendo treinada com todo o conjunto de dados processado.

Limitar a profundidade evita que a árvore cresça indefinidamente. Isso ajuda a controlar a complexidade do modelo, gerando folhas mais interpretáveis e impedindo a criação de regras excessivamente específicas para cada detalhe dos dados.

---

## 9. Probabilidades estimadas nas folhas

As folhas de uma árvore de decisão também podem representar probabilidades para cada classe.

Em uma árvore com profundidade limitada (como `max_depth=6`), uma folha pode conter exemplos pertencentes às duas classes com diferentes proporções (por exemplo, 60% de `No` e 40% de `Yes`), o que significa que a folha não é completamente pura e apresenta probabilidades mais distribuídas.

---

## 10. Conclusão

A atividade permitiu observar na prática o funcionamento da partição recursiva em uma árvore de decisão e a relação entre profundidade e pureza dos nós através do índice de Gini.

A utilização do parâmetro `max_depth=6` permitiu estruturar o modelo de forma equilibrada, controlando a complexidade da árvore e gerando visualizações e regras interpretáveis a partir dos dados clínicos de doenças cardíacas.O experimento complementar de treino e teste também mostrou que o modelo mais complexo não necessariamente é o melhor modelo para realizar previsões em novos dados.
