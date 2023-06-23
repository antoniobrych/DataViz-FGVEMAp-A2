#Importei do meu módulo a função 'ocorrencia_por_pais' e o csv 'df_cafe'
from manipulacao_dados_gabriel import ocorrencia_por_pais, df_cafe

#Guardei em uma variável as quantidades de lotes produzidos por país
lotes_produzidos = ocorrencia_por_pais(df_cafe).data['valores']

#Guardei em uma variável o nome dos países correspondentes 
nome_dos_paises = ocorrencia_por_pais(df_cafe).data['indices']
