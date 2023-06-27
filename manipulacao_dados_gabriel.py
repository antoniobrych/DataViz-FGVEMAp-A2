#Importei a função 'ColumnDataSource' do 'bokeh.models'
from bokeh.models import ColumnDataSource

#Chamei a biblioteca pandas de 'pd'
import pandas as pd

#Botei em uma variável o csv usado no trabalho
df_cafe = pd.read_csv('cleaned_coffee_dataset.csv')

"""Verifiquei quantos lotes foram produzidos por país, e criei o
CDS com o nome do país e seu respectivo numero de lotes produzidos"""
def ocorrencia_por_pais(df_cafe):
    producao_total = df_cafe['Country of Origin'].value_counts()
    numero_de_lotes = producao_total.values
    nome_do_pais_correspondente = producao_total.index
    novo_cds = ColumnDataSource(data=dict(valores=numero_de_lotes, indices=nome_do_pais_correspondente))
    return novo_cds


"""VIS 1"""

"""Criei uma função para criar um cds com os paises como index e a sua produção total em kg"""
def peso_total_por_pais(df_cafe):
    df_cafe['Peso da Mochila'] = df_cafe['Bag Weight'].str.replace(' kg', '').astype(int)
    df_cafe['Peso Total Por Produtora'] = df_cafe['Number of Bags'] * df_cafe['Peso da Mochila']
    producao_por_pais_em_kg = df_cafe.groupby('Country of Origin')['Peso Total Por Produtora'].sum().reset_index()
    producao_por_pais_em_kg = producao_por_pais_em_kg.set_index('Country of Origin')
    novo_cds = ColumnDataSource(data=dict(producao=producao_por_pais_em_kg['Peso Total Por Produtora'].tolist(), paises=producao_por_pais_em_kg.index.tolist()))
    return novo_cds

"""Função para criar objetos em cds com a media da qualidade do cafe por pais"""
def media_por_pais(df_cafe):
    media_da_qualidade_do_cafe = df_cafe.groupby('Country of Origin')['Overall'].mean()
    novo_df = pd.DataFrame({'País': media_da_qualidade_do_cafe.index, 'Média das Notas': media_da_qualidade_do_cafe.values})
    novo_cds = ColumnDataSource(data=dict(paises=novo_df['País'], medias=novo_df['Média das Notas']))
    return novo_cds

"""Criei um cds com a produção total por país, e a média da qualidade por país, para fazer o gráfico"""
Producao = peso_total_por_pais(df_cafe).data['producao']
Paises = media_por_pais(df_cafe).data['paises']
Media = media_por_pais(df_cafe).data['medias']
correlacao_quantidade_qualidade = ColumnDataSource(data=dict(media=Media,producao=Producao, paises=Paises))


"""VIS 2"""


def analise_coffee(df_cafe):
    df_cafe['Data de Avaliação'] = pd.to_datetime(df_cafe['Grading Date'], format='mixed', dayfirst=True)
    df_cafe['MesAno'] = df_cafe['Data de Avaliação'].dt.to_period('M')
    return df_cafe

def analise_coffe_limpo(df_cafe):
    df = analise_coffee(df_cafe)
    novo_df = df.loc[:, ['MesAno', 'Overall']]
    return novo_df

novo_df = analise_coffe_limpo(df_cafe)
df_para_vis2 = novo_df.groupby(novo_df['MesAno'])['Overall'].mean().reset_index()
cds_df_para_vis2 = ColumnDataSource(data=df_para_vis2)

