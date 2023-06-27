from manipulacao_dados_gabriel import cds_df_para_vis2

#Import para a visualização em bokeh
from bokeh.plotting import figure
from bokeh.models import Range1d,HoverTool
from bokeh.io import output_file, save, show
import numpy as np

figure2= figure(x_axis_type = 'datetime')

figure2.line(x='MesAno', y='Overall', source = cds_df_para_vis2)