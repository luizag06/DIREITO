import pandas as pd
import streamlit as st
import plotly.express as px 

dataset= pd.read_csv('https://www.irdx.com.br/media/uploads/paises.csv')

fig= px.scatter_geo(dataset,
                    lat=dataset['latitude'],
                    lon=dataset['longitude'],
                    hover_name=dataset['nome'])
fig.update_layout(title='Cordenadas dos países no mapa',
                  geo_scope='world')
fig.show()

