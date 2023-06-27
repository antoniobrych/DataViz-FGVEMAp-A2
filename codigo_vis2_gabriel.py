from manipulacao_dados_gabriel import cds_df_para_vis2

#Import para a visualização em bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.layouts import column
from bokeh.models import Button, Slider, CustomJS
from bokeh.models.sources import ColumnDataSource
from datetime import datetime, timedelta

figure2= figure(x_axis_type = 'datetime', width = 600, height = 400)

figure2.line(x='MesAno', y='Overall', source = cds_df_para_vis2, color="SaddleBrown", line_width = 5)

#Configurações básicas do gráfico
figure2.title.text = 'Evolução da Qualidade do Café'
figure2.title.text_color = "SaddleBrown"
figure2.title.text_font = "Arial"
figure2.title.text_font_size = "30px"
figure2.title.align = "center"
figure2.background_fill_color = "GoldenRod"
figure2.yaxis.axis_label = "Qualidade"
figure2.grid.grid_line_alpha = 0
figure2.yaxis.axis_label_text_color = "#3D2923"
figure2.xaxis.minor_tick_line_color = "#3D2923"
figure2.yaxis.minor_tick_line_color = "#3D2923"
figure2.xaxis.axis_line_width = 3
figure2.yaxis.axis_line_width = 3
figure2.xaxis.axis_line_color = "SaddleBrown"
figure2.yaxis.axis_line_color = "SaddleBrown"
figure2.xaxis[0].ticker.num_minor_ticks = 0
figure2.yaxis[0].ticker.num_minor_ticks = 0