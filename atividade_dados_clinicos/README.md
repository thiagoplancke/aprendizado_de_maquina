# Modelagem Experimental — Árvore de Decisão

## Alunos:

Thiago Plancke 
Kauê Lima
Vladimir Queiroz 

## 1. Objetivo

Nesta atividade foi realizada uma primeira modelagem experimental utilizando uma árvore de decisão aplicada a um conjunto de dados clínicos relacionados a doenças cardíacas.

Foram utilizados os conceitos de **partição recursiva** e **pureza dos nós**, analisando inicialmente uma árvore de decisão sem limite de profundidade e, posteriormente, uma árvore com profundidade máxima limitada.

O objetivo foi observar o comportamento das folhas, do índice de Gini e das probabilidades estimadas nas folhas, além de analisar o efeito do sobreajuste (*overfitting*).

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

O target utilizado foi:
`Status de Doença Cardíaca`

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

Nesse caso, os registros possuem exatamente as mesmas informações de entrada, mas resultados diferentes.

Essa situação é importante para a árvore de decisão porque não seria possível criar uma regra baseada somente nas features capaz de separar perfeitamente esses dois registros.


---

## 6. Árvore de decisão sem limite de profundidade

Inicialmente, foi criada uma árvore de decisão sem definir um valor para `max_depth`.

Dessa forma, o algoritmo ficou livre para continuar realizando partições recursivas enquanto encontrasse divisões capazes de melhorar a separação das classes.

O resultado foi uma árvore de decisão muito grande. Esse comportamento ocorre porque a árvore continua criando novos nós para tentar aumentar a pureza das folhas.

O índice utilizado para medir essa pureza foi o **Gini**. Quanto mais próximo de `0`, mais puro é o nó.

Uma folha contendo apenas uma classe pode apresentar `Gini = 0`. Por exemplo, uma folha contendo somente pacientes classificados como `Yes` seria completamente pura. Essa árvore sem limite de profundidade pode criar diversas folhas extremamente específicas, algumas delas chegando a uma pureza máxima.

---

## 7. Relação entre Gini e pureza

O índice de Gini indica o grau de mistura entre as classes dentro de um nó.

Quando `Gini = 0`, o nó é completamente puro. Isso significa que todas as amostras daquele nó pertencem à mesma classe.

Por outro lado, quando diferentes classes estão presentes no mesmo nó, o valor de Gini aumenta. Durante o crescimento da árvore, o algoritmo procura divisões que aumentem a pureza dos nós resultantes. Assim, a árvore sem limite de profundidade pode continuar criando divisões até produzir folhas extremamente puras.

---

## 8. Problema do sobreajuste

Apesar de uma árvore muito profunda conseguir produzir folhas muito puras, isso não significa necessariamente que ela seja um modelo melhor.

Uma árvore sem limite de profundidade pode aprender características muito específicas dos dados utilizados no treinamento. Esse comportamento é conhecido como *overfitting*, ou sobreajuste.

Nesse caso, o modelo apresenta um desempenho muito alto nos dados utilizados durante o treinamento, mas pode apresentar desempenho inferior quando recebe dados que não foram utilizados para seu aprendizado.

Portanto, uma folha com Gini igual a zero indica pureza em relação aos dados que chegaram àquela folha, mas não garante uma boa capacidade de generalização.

---

## 9. Separação entre treino e teste

Como análise complementar à atividade, os dados foram divididos em dois conjuntos:

- **80%** para treinamento
- **20%** para teste

O conjunto de treinamento foi utilizado para ajustar a árvore. O conjunto de teste foi utilizado posteriormente para verificar como o modelo se comportava diante de dados que não haviam sido utilizados durante o treinamento.

Essa etapa permitiu analisar não apenas a capacidade da árvore de aprender os dados, mas também sua capacidade de generalização.

---

## 10. Testes com diferentes profundidades

Além da comparação solicitada na atividade, foram realizados testes utilizando diferentes valores de `max_depth`.

Foi observado que aumentar a profundidade inicialmente melhorou o desempenho do modelo no conjunto de teste. Porém, depois de determinado ponto, aumentar ainda mais a profundidade passou a reduzir a acurácia no conjunto de teste.

Nos experimentos realizados, a profundidade **6** apresentou o melhor resultado observado, com uma acurácia próxima de **80%**. A partir desse ponto, valores maiores de profundidade apresentaram desempenho inferior.

Esse resultado mostra que aumentar a complexidade da árvore não significa necessariamente aumentar sua capacidade de generalização.

---

## 11. Comparação entre árvores de diferentes profundidades

O comportamento observado pode ser resumido da seguinte maneira:

| Profundidade | Comportamento observado |
|---|---|
| Menor profundidade | Modelo mais simples e com menor capacidade de realizar divisões |
| 5 | Desempenho próximo de 80% |
| 6 | Melhor desempenho observado, próximo de 80% |
| 7 | Pequena redução no desempenho |
| 10 ou maior | Redução mais evidente no desempenho de teste |

Os valores exatos dependem da divisão utilizada entre treinamento e teste. O resultado indica a existência de um ponto em que a complexidade da árvore deixa de trazer benefícios para a generalização.

---

## 12. Probabilidades estimadas nas folhas

As folhas de uma árvore de decisão também podem representar probabilidades para cada classe.

Quando uma folha contém apenas uma classe, a probabilidade estimada pode chegar a 100% para essa classe. Por exemplo:
- `No` = 0%
- `Yes` = 100%

Nesse caso, a folha é completamente pura.

Entretanto, em uma árvore com profundidade limitada, uma folha pode conter exemplos pertencentes às duas classes. Por exemplo:
- `No` = 60%
- `Yes` = 40%

Nesse caso, a folha não é completamente pura.

Ao limitar a árvore com `max_depth=3`, espera-se que as folhas representem grupos maiores de observações e, consequentemente, apresentem probabilidades menos extremas do que algumas folhas da árvore sem limite de profundidade.

Essa comparação permite observar na prática como a limitação da profundidade reduz a capacidade da árvore de criar regiões extremamente específicas dos dados.

---

## 13. Comparação entre o modelo sem limite e o modelo com `max_depth=3`

A comparação solicitada na atividade pode ser entendida da seguinte forma:

### Árvore sem limite de profundidade
- Possui maior complexidade.
- Pode criar uma grande quantidade de nós.
- Pode produzir folhas extremamente puras.
- Pode apresentar Gini igual a 0 em diversas folhas.
- Pode produzir probabilidades próximas de 0% ou 100%.
- Possui maior risco de sobreajuste.

### Árvore com `max_depth=3`
- Possui menor complexidade.
- Possui menos níveis de decisão.
- Não consegue realizar tantas divisões.
- Algumas folhas permanecem com as duas classes.
- O Gini de algumas folhas permanece maior que 0.
- As probabilidades tendem a ser menos extremas.
- A árvore se torna mais simples de interpretar.

---

## 14. Conclusão

A atividade permitiu observar na prática o funcionamento da partição recursiva em uma árvore de decisão e a relação entre profundidade e pureza dos nós.

Quando a árvore foi treinada sem limite de profundidade, ela cresceu consideravelmente e conseguiu criar folhas muito puras. Em algumas folhas, o índice de Gini pode chegar a 0, indicando que todos os exemplos daquela folha pertencem à mesma classe.

Entretanto, uma árvore extremamente profunda pode apresentar sobreajuste, pois possui liberdade para criar regras muito específicas para os dados de treinamento.

A limitação da profundidade reduz essa complexidade. Com `max_depth=6`, a árvore possui menos possibilidades de realizar divisões sucessivas, fazendo com que algumas folhas mantenham exemplos das duas classes e apresentem probabilidades mais distribuídas.

Como análise complementar, também foi realizada uma separação entre dados de treinamento e teste. Os experimentos com diferentes valores de profundidade mostraram que o aumento da complexidade inicialmente pode melhorar o desempenho, mas, após determinado ponto, pode começar a prejudicar a capacidade de generalização.

Nos testes realizados, a profundidade **6** apresentou o melhor desempenho observado, com uma acurácia próxima de **80%**.

Dessa forma, o experimento mostrou que:
- A redução do Gini representa aumento da pureza do nó;
- Árvores mais profundas conseguem criar folhas mais específicas;
- Folhas perfeitamente puras não garantem necessariamente melhor generalização;
- Aumentar a profundidade indefinidamente pode causar *overfitting*;
- Limitar a profundidade reduz a complexidade do modelo;
- A avaliação em dados não utilizados durante o treinamento permite observar a capacidade de generalização da árvore.

O experimento complementar de treino e teste também mostrou que o modelo mais complexo não necessariamente é o melhor modelo para realizar previsões em novos dados.