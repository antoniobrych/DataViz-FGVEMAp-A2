from bokeh.io import show,output_file
from codigo_vis1_gabriel import figure1
from codigo_vis2_gabriel import figure2
from bokeh.layouts import row
output_file('vis_gabriel.html')
show(row(figure1,figure2))