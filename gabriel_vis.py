#Import para a visualização em bokeh
from bokeh.plotting import figure
from bokeh.models import Range1d,HoverTool
from bokeh.io import output_file, save, show
import numpy as np

#Importei do meu módulo a função 'ocorrencia_por_pais', o csv 'df_cafe', a função 'peso_total_por_pais' e a 'media_por_pais'
from manipulacao_dados_gabriel import ocorrencia_por_pais, df_cafe, peso_total_por_pais, media_por_pais, correlacao_quantidade_qualidade



output_file('gabriel_vis.html')

# Dados
x = correlacao_quantidade_qualidade.data['media']
y = correlacao_quantidade_qualidade.data['producao']

# Calcular os coeficientes da reta de regressão
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Criar um objeto Figure
figure = figure()

# Plotar os pontos de dispersão
figure.circle(source=correlacao_quantidade_qualidade, x='media', y='producao', fill_color="SaddleBrown", line_color="SaddleBrown", size=10)

# Traçar a reta de regressão
x_regression = np.array([min(x), max(x)])
y_regression = slope * x_regression + intercept
figure.line(x_regression, y_regression, line_color='#3D2923', line_width=3)

# Configurações adicionais do gráfico
figure.width = 1280
figure.height = 720
figure.background_fill_color = "GoldenRod"
figure.title.text = 'Quantidade é Qualidade?'
figure.title.text_color = "SaddleBrown"
figure.title.text_font = "Arial"
figure.title.text_font_size = "42px"
figure.title.align = "center"
figure.x_range.start = 7
figure.x_range.end = 8
figure.y_range.start = -200
figure.y_range.end = 350000
figure.xaxis[0].ticker.desired_num_ticks = 2
figure.yaxis[0].ticker.desired_num_ticks = 3
figure.grid.grid_line_alpha = 0
figure.xaxis.axis_label = "Overall"
figure.yaxis.axis_label = "Produção (kg)"
figure.xaxis.axis_label_text_font_size = "16pt"
figure.yaxis.axis_label_text_font_size = "16pt"
figure.xaxis.axis_label_text_color = "#3D2923"
figure.yaxis.axis_label_text_color = "#3D2923"
figure.xaxis.minor_tick_line_color = "#3D2923"
figure.yaxis.minor_tick_line_color = "#3D2923"
figure.xaxis.minor_tick_in = 2
figure.yaxis.minor_tick_in = 2
figure.axis.major_label_text_color = "#3D2923"
#Adicionei interação para ao passar o mouse por cime da bolinha aparecer informações sobre o país, a produção e a qualidade do café
tooltips = [("País", "@paises"),
            ("Produção em kg", "@producao"),
            ("Qualidade do Café", "@media")]
figure.add_tools(HoverTool(tooltips=tooltips))

#Adicionei um retângulo onde ficará minha anotação
figure.rect(x=7.357, y=200000, width=0.328, height=30000, fill_alpha=0, line_color='#3D2923', line_width=2)

# Adicionar o texto na posição y=110000
figure.text(x=7.21, y=200000, text=['A reta de regressão está muito inclinada por conta'], text_color='#3D2923', text_font_size='12pt')
figure.text(x=7.21, y=190000, text=['da Ethiopia (usar o wheel zoom para ver o outlier)'], text_color='#3D2923', text_font_size='12pt')
# Exibir o gráfico
show(figure)
