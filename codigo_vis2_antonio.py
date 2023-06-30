from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, Label, Select
from bokeh.palettes import brewer
import pandas as pd
import numpy as np
from bokeh.transform import factor_cmap
from bokeh.palettes import YlOrBr
from bokeh.layouts import row
from cds_reader import df_to_cds_conv

df = pd.read_csv('cleaned_coffee_dataset.csv')
coffee_data = df_to_cds_conv(df)
quakers = coffee_data.data["Quakers"]
quakers = np.float16(quakers)
aroma = coffee_data.data["Aroma"]
nota_geral = coffee_data.data["Overall"]
alpha = (nota_geral - 6.0) / (8.5 - 6.0)

# Adicionar jitter às coordenadas dos pontos
jitter_range = 0.03  
quakers_jitter = np.random.uniform(-jitter_range, jitter_range, len(quakers))
aroma_jitter = np.random.uniform(-jitter_range, jitter_range, len(aroma))
quakers += quakers_jitter
aroma += aroma_jitter
#Usamos o jitter para conseguir ter uma melhor noção da quantidade de amostras

#preparando o gráfico
quakers_aroma = figure(title="Quakers: Grãos imaturos prejudicam o aroma do café",
                     x_axis_label="Quakers",
                     y_axis_label="Nota do Aroma: 1 a 10",
                     width=513, 
                     height=483
                     )
"""
Será um scatter plot, a ideia é verificar a relação entre o quakers e o aroma,
 junto a média nos outros aspectos.
"""
quakers_aroma.circle(quakers, aroma,
                   fill_color="#6F4E37",
                   line_color="#6F4E37",
                   fill_alpha=alpha, 
                   legend_label="Pontuação geral: Maior para menor, mais escuro para mais claro",
                   size = 10
)
#personalizando um pouco o plot, retirando alguns elementos "desnecessários"
quakers_aroma.toolbar.autohide = True 
quakers_aroma.toolbar.logo = None # Não vejo necessidade em aparecer a logo do bokeh
quakers_aroma.grid.visible = False 
# Não vejo necessidade da grade de fundo. A posição e o alpha são suficientes

# Movi a legenda pra esquerda, assim ela sobrepõem os pontos
quakers_aroma.legend.location = "top_left"

#função pra mostrar o gráfico
show(quakers_aroma)

