import pandas as pd
from sklearn import tree
import  matplotlib.pyplot as plt
df = pd.read_parquet("data/dados_clones.parquet")

print(df.columns)

target = 'Status '

features = ['p2o_master_id', 'Massa(em kilos)',
       'Estatura(cm)', 'Distância Ombro a ombro', 'Tamanho do crânio',
       'Tamanho dos pés', 'Tempo de existência(em meses)']

print(df.select_dtypes(include=['object', 'string']).columns.tolist())

print(df['General Jedi encarregado'].unique())

pd.set_option('display.max_columns', None)

tipos= ['Tamanho do crânio', 'Distância Ombro a ombro', 'Tamanho dos pés']
for i in tipos:
    df[str(i)] = df[str(i)].map({"Tipo 1": 0, "Tipo 2": 1, "Tipo 3": 2, "Tipo 4": 3, "Tipo 5": 4})

jedis = ['General Jedi encarregado']

for i in jedis:
    df[str(i)] = df[str(i)].map({"Yoda": 0, "Shaak Ti": 1, "Obi-wan Kenobi": 2,"Aayla Secura": 3, "Mace Windu": 4})

print(df)

X = df[features]
y = df[target]

model = tree.DecisionTreeClassifier(max_depth=3,
random_state = 42)


model.fit(X, y)


plt.figure(dpi=400)

tree.plot_tree(model,
               feature_names= features,
               class_names= model.classes_,
               filled = True)

plt.show()