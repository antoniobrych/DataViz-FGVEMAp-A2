#Import dos dados organizados para o gráfico
from manipulacao_dados_gabriel import cds_df_para_vis2, df_cafe, media_coluna_overall,cds_media

#Import para a visualização em bokeh
from bokeh.plotting import figure,ColumnDataSource
from bokeh.io import output_file, save, show
from bokeh.models import Legend, LegendItem, Line
from bokeh.models.annotations import Span, BoxAnnotation

figure2= figure(x_axis_type = 'datetime', width = 600, height = 400, tools=['pan', 'reset','box_zoom'])

figure2.line(x='MesAno', y='Overall', source = cds_df_para_vis2, color="SaddleBrown", line_width = 5)

#Configurações básicas do gráfico
figure2.title.text = 'Evolução da Qualidade do Café'
figure2.title.text_color = "SaddleBrown"
figure2.title.text_font = "Arial"
figure2.title.text_font_size = "25px"
figure2.title.align = "left"
figure2.background_fill_color = "GoldenRod"
figure2.yaxis.axis_label = "Qualidade"
figure2.xaxis.axis_label = "Data da Avaliação"
figure2.grid.grid_line_alpha = 0
figure2.yaxis.axis_label_text_color = "#3D2923"
figure2.xaxis.minor_tick_line_color = "#3D2923"
figure2.yaxis.minor_tick_line_color = "#3D2923"
figure2.xaxis.major_tick_in = 0
figure2.yaxis.major_tick_in = 0
figure2.xaxis.axis_line_width = 3
figure2.yaxis.axis_line_width = 3
figure2.xaxis.axis_line_color = "SaddleBrown"
figure2.yaxis.axis_line_color = "SaddleBrown"
figure2.xaxis[0].ticker.num_minor_ticks = 0
figure2.yaxis[0].ticker.num_minor_ticks = 0

#Adicionei uma linha pontilhada que representa a média geral da qualidade do café
figure2.line(x='Valores', y='Numero', source=cds_media, color = '#260B01',line_dash = 'dashed', line_width = 2, legend_label = 'Média Geral')
span = Span(location=media_coluna_overall(df_cafe), dimension="width",line_color='#260B01',line_width=2, line_dash = 'dashed')
figure2.add_layout(span)

#Fiz uma box annotation para destacar os picos de perda de qualidade


