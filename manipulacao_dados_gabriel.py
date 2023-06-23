#Importei a função 'ColumnDataSource' do 'bokeh.models'
from bokeh.models import ColumnDataSource

#Chamei a biblioteca pandas de 'pd'
import pandas as pd

#Botei em uma variável o csv usado no trabalho
df_cafe = pd.read_csv('df_arabica_clean.csv')

"""Verifiquei quantos lotes foram produzidos por país, e criei o
CDS com o nome do país e seu respectivo numero de lotes produzidos"""
def ocorrencia_por_pais(df_cafe):
    producao_total = df_cafe['Country of Origin'].value_counts()
    numero_de_lotes = producao_total.values
    nome_do_pais_correspondente = producao_total.index
    novo_cds = ColumnDataSource(data=dict(valores=numero_de_lotes, indices=nome_do_pais_correspondente))
    return novo_cds