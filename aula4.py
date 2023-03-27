import pandas as pd
import matplotlib.pyplot as plt
import random

pd.Series(data=5)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

pd.Series(lista_nomes) # Cria uma Series com o valor a lista_nomes

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}

pd.Series(dados) # Cria uma Series com um dicionário)

series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas
print('Tipo de dados: ', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos? ', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)
print('Quantos valores existem? ', series_dados.count()) # Conta quantos valores existem (exclui os nulos)

# Funções matemáticas e estatísticas do pandas
print('Qual o nemor valor? ', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor? ', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética? ', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão? ', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
print('QUal a mediana? ', series_dados.median()) # Extrai a mediana de uma Series numérica
print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series

# recursos de leitura de estrutuas de dados guardando em um DataFrame
url = 'http://en.wikipedia.org/wiki/Minnesota'

dfs = pd.read_html(url)
print(type(dfs))
print(len(dfs))

#filtros
dfs2 = pd.DataFrame(lista_nomes, columns=['nome'])
dfs2['idade'] = 30
dfs2 = dfs2.append({'nome': 'TESTE', 'idade': 25}, ignore_index = True)

#print(dfs) com filtro
print(dfs2.loc[(dfs['idade'] < 30)])

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2) #pyplot gerencia a figura e o eixo