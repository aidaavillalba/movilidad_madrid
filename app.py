import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import collections
import numpy as np
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


st.title('Uber pickups in NYC')

"""
df_matriculas = pd.read_excel("./DatosUCM/ucm-matriculas-2020-21-anonimizado.xlsx")
df_matriculas = df_matriculas[(df_matriculas['des_municipio_residencia'].notna() &df_matriculas['lat_municipio_residencia'].notna()&df_matriculas['lon_municipio_residencia'].notna())]
df_matriculas = df_matriculas[(df_matriculas['des_municipio_curso'].notna() &df_matriculas['lat_municipio_curso'].notna()&df_matriculas['lon_municipio_curso'].notna())]


df_matriculas['des_municipio_residencia'].mask(df_matriculas['lon_municipio_residencia'] ==-3.920291 ,'ARROYOMOLINOS MADRID', inplace=True)
df_matriculas['des_municipio_residencia'].mask(df_matriculas['lon_municipio_residencia'] ==-6.161489 ,'ARROYOMOLINOS CACERES', inplace=True)

nodos_residencia = df_matriculas[["des_municipio_residencia", "lon_municipio_residencia","lat_municipio_residencia"]]
nodos_residencia.drop_duplicates(inplace = True)
nodos_residencia.sort_values(by="des_municipio_residencia", inplace=True)

nodos_curso = df_matriculas[["des_municipio_curso", "lon_municipio_curso", "lat_municipio_curso"]]
nodos_curso.drop_duplicates(inplace = True)
nodos_curso.sort_values(by="des_municipio_curso", inplace=True)

nodos_union1 = nodos_residencia.copy()
nodos_union1 = nodos_union1.rename({'des_municipio_residencia': 'MUNICIPIO', 'lon_municipio_residencia': 'LON', 'lat_municipio_residencia': 'LAT'}, axis=1)

nodos_union2 = nodos_curso.copy()
nodos_union2 = nodos_union2.rename({'des_municipio_curso': 'MUNICIPIO', 'lat_municipio_curso': 'LAT', 'lon_municipio_curso': 'LON'}, axis=1)
nodos = nodos_union1.append(nodos_union2).drop_duplicates()

df_edges = df_matriculas[["des_municipio_residencia","des_municipio_curso"]]

municipios = df_edges[["des_municipio_residencia", "des_municipio_curso"]].value_counts().keys().tolist()
recuento = df_edges[["des_municipio_residencia", "des_municipio_curso"]].value_counts().tolist()
value_dict = dict(zip(municipios, recuento))
value_dict = collections.OrderedDict(sorted(value_dict.items()))


df_edges = df_edges.drop_duplicates()
df_edges.sort_values(by=['des_municipio_residencia'], inplace=True)

df_edges["Personas"] = value_dict.values() 

df_edges.drop_duplicates(inplace=True)

#MOVILIDAD
df_edges_movilidad = df_edges.copy()
df_edges_movilidad = df_edges_movilidad[df_edges_movilidad["des_municipio_residencia"]!=df_edges_movilidad["des_municipio_curso"]]


nodos_dic = nodos.set_index('MUNICIPIO').T.to_dict('list')
municipios = nodos_dic.keys()
aristas = list(zip(df_edges_movilidad["des_municipio_residencia"], df_edges_movilidad["des_municipio_curso"]))
pesos = list(df_edges_movilidad["Personas"])

plt.figure(figsize=(60,60))
pos = nodos_dic
nodes = municipios

G = nx.Graph()
G.add_nodes_from(municipios)
G.add_edges_from(aristas, weight= pesos)
nx.draw_networkx(G, nodos_dic, with_labels=False, node_size=20, alpha=0.1, edge_color="red")
fig = nx.draw_networkx_nodes(G, pos, node_color = "gray", node_size=100, alpha=0.5)
#plt.show()


st.pyplot(fig)
"""