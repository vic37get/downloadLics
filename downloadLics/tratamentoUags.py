import pandas as pd


dados = pd.read_csv('Uags.csv', encoding='utf-8')
dados.dropna(axis=0)
print(dados)
dados.to_csv('Uags.csv', encoding='utf-8', index=False)