import pandas
import matplotlib.pyplot as plt
from sklearn import tree

df = pandas.read_csv("data/heart_disease.csv")
df_limpo = df.dropna()

traducao_colunas = {
    'Age': 'Idade',
    'Gender': 'Gênero',
    'Blood Pressure': 'Pressão Arterial',
    'Cholesterol Level': 'Nível de Colesterol',
    'Exercise Habits': 'Hábitos de Exercício',
    'Smoking': 'Tabagismo',
    'Family Heart Disease': 'Histórico Familiar de Doença Cardíaca',
    'Diabetes': 'Diabetes',
    'BMI': 'IMC',
    'High Blood Pressure': 'Pressão Arterial Alta',
    'Low HDL Cholesterol': 'Colesterol HDL Baixo',
    'High LDL Cholesterol': 'Colesterol LDL Alto',
    'Alcohol Consumption': 'Consumo de Álcool',
    'Stress Level': 'Nível de Estresse',
    'Sleep Hours': 'Horas de Sono',
    'Sugar Consumption': 'Consumo de Açúcar',
    'Triglyceride Level': 'Nível de Triglicerídeos',
    'Fasting Blood Sugar': 'Glicemia em Jejum',
    'CRP Level': 'Nível de PCR',
    'Homocysteine Level': 'Nível de Homocisteína',
    'Heart Disease Status': 'Status de Doença Cardíaca'
}

df_limpo = df_limpo.rename(columns=traducao_colunas)





print(df.shape)
print(df_limpo.shape)

binary_colum = ['Tabagismo',
'Histórico Familiar de Doença Cardíaca',
'Diabetes',
'Pressão Arterial Alta',
'Colesterol HDL Baixo',
'Colesterol LDL Alto'
]

genero_colum = ['Gênero']

level_colum = ['Hábitos de Exercício',
'Consumo de Álcool',
'Nível de Estresse',
'Consumo de Açúcar']

for i in binary_colum:
    df_limpo[str(i)] = df_limpo[str(i)].map({"No": 0, "Yes": 1})


for i in level_colum:
    df_limpo[str(i)] = df_limpo[str(i)].map({"Low": 0, "Medium": 1, "High": 2})

for i in genero_colum:
    df_limpo[str(i)] = df_limpo[str(i)].map({"Female": 0, "Male": 1})


for coluna in df_limpo.columns:
    print(f"\n--- {coluna} ---")
    print(df_limpo[coluna].dtype)
    print(df_limpo[coluna].unique())





target = 'Status de Doença Cardíaca'

features = ['Idade', 'Gênero', 'Pressão Arterial', 'Nível de Colesterol', 'Hábitos de Exercício', 'Tabagismo', 'Histórico Familiar de Doença Cardíaca', 'Diabetes', 'IMC', 'Pressão Arterial Alta', 'Colesterol HDL Baixo', 'Colesterol LDL Alto', 'Consumo de Álcool', 'Nível de Estresse', 'Horas de Sono', 'Consumo de Açúcar', 'Nível de Triglicerídeos', 'Glicemia em Jejum', 'Nível de PCR', 'Nível de Homocisteína']


y = df_limpo[target]

X = df_limpo[features]




model = tree.DecisionTreeClassifier(max_depth=6,
random_state = 42)


model.fit(X,y)



plt.figure(dpi=400)

tree.plot_tree(model,
               feature_names= features,
               class_names= model.classes_,
               filled = True)

plt.show()
