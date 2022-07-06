#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 01:09:58 2022

@author: nico
"""

import pandas as pd
#import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import plotly.express as px
#import datetime

#%% Información de las estaciones

df0 = pd.read_csv ('/home/nico/Documentos/Drought/Mediciones/agrometR/estaciones_agrometRM0.csv', sep=',')
#%%
df = pd.read_csv ('/home/nico/Documentos/Drought/Mediciones/agrometR/R_agromet_script_todoChile_Desde2007.csv', sep =',', parse_dates=['fecha_hora'])
# Así se puede hacer un pre proceso seleccionando a las estaciones por su id
# awk -F, '$2 == 39' data_stations0.csv # selecciona los datos de la estación con id=39

fechas = df['fecha_hora']
#print(fechas.max())
#print(fechas.min())
#print("\nNumber of days")
#print((fechas.max() - fechas.min()).days)
#print("\nNumber of years")
#print((fechas.max() - fechas.min()).days/ 365.25)
    
dti = pd.date_range(fechas.min(),fechas.max(),freq="H")# serie de tiempo horaria creada desde inicio a fin 
#lo convierto en dataframe: serie.to_dataframe
dti = pd.Index(dti,name='fecha_hora')
dti = dti.to_frame(index = False)
# lo mismo con fechas
fechas = pd.Index(fechas,name ='fecha_hora')
fechas = fechas.to_frame(index=False)


for id in range(df['station_id'].max()):
    print(str(id))
    aws   = df[df['station_id']==id]
    awsPP = aws[['fecha_hora','precipitacion_horaria']]
#awsPP.to_csv("/home/nico/Documentos/Drought/Mediciones/agrometR/out_"+str(id)+".csv",na_rep='NaN')
    #acoplado = pd.merge_ordered(dti,awsPP, on = 'fecha_hora', suffixes=('_df1', '_df2'))
    acoplado = pd.merge_ordered(dti,awsPP, on = 'fecha_hora')
    dti[str(id)] = acoplado['precipitacion_horaria']
#acoplado = pd.merge_ordered(awsPP,dti, on = 'fecha_hora', suffixes=('_df1', '_df2'))

#%% Guardamos el CSV
dti.to_csv("/home/nico/Documentos/Drought/Mediciones/agrometR/Agromet_hourly_PP_ALL_2017_onwards.csv",na_rep='NaN')

#df.head()
#df.info()
#%%
