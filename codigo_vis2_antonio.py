from bokeh.plotting import figure, show
from bokeh.models import HoverTool, Select
from bokeh.transform import linear_cmap
from bokeh.palettes import Spectral6
import pandas as pd
import numpy as np
from cds_reader import df_to_cds_conv

# Leitura dos dados
df = pd.read_csv('cleaned_coffee_dataset.csv')
coffee_data = df_to_cds_conv(df)
quakers = coffee_data.data["Quakers"]
quakers = np.float16(quakers)
aroma = coffee_data.data["Aroma"]
nota_geral = coffee_data.data["Overall"]
alpha = (nota_geral - 6.0) / (8.5 - 6.0)

# Jitter
jitter_range = 0.03  
quakers_jitter = np.random.uniform(-jitter_range, jitter_range, len(quakers))
aroma_jitter = np.random.uniform(-jitter_range, jitter_range, len(aroma))
quakers += quakers_jitter
aroma += aroma_jitter

# Criação do gráfico quakers_aroma
quakers_aroma = figure(title="Quakers: Grãos imaturos prejudicam o aroma do café",
                       x_axis_label="Quakers",
                       y_axis_label="Nota do Aroma: 1 a 10",
                       width=513,
                       height=483
                       )

# Alterar a paleta de cores

# Adicionar interatividade - HoverTool
hover = HoverTool(tooltips=[("Quakers", "@quakers"), ("Aroma", "@aroma"), ("Pontuação Geral", "@Overall")])
quakers_aroma.add_tools(hover)

quakers_aroma.circle(quakers, aroma,
                     fill_color='Blue',
                     line_color='Black',
                     fill_alpha=alpha,
                     legend_label="Pontuação geral: Maior para menor, mais escuro para mais claro",
                     size=10
                     )

# Retirando logo do Bokeh
quakers_aroma.toolbar.logo = None

quakers_aroma.legend.location = "top_left"

# Renderizando o gráfico
show(quakers_aroma)
