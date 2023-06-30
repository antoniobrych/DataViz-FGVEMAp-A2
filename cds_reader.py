# Criando função que transforma data_set em ColunmDataSource
from bokeh.models import ColumnDataSource, HoverTool, Label, Select
def df_to_cds_conv(df):
    source = ColumnDataSource(df)
    return source

"""
conferindo "função cds_generator":
data = cds_generator("df_arabica_clean.csv")
print(data.data['Overall'])
"""