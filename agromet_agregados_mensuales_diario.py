#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 01:25:20 2022

Genera los agregados en las series de tiempo de PP

@author: nico
"""


import pandas as pd
#import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import plotly.express as px
#import datetime

#path_and_file = '/home/nico/Documentos/Drought/Mediciones/agrometR/Agromet_hourly_PP_2012-2017.csv'
path_and_file = '/home/nico/Documentos/Drought/Mediciones/agrometR/Agromet_hourly_PP_2012-2022.csv'
df = pd.read_csv (path_and_file, sep =',', parse_dates=['fecha_hora'],index_col=False)
del df["indx"]
# Defino los valores máximos y minimos de PP diaria
max_HH_PP = 50
min_HH_PP = 0
df[df.iloc[:,1:697] >= max_HH_PP] = np.nan
df[df.iloc[:,1:697] <= min_HH_PP] = np.nan
'''
Heavy rain — when the precipitation rate is > 7.6 mm (0.30 in) per hour, or between 10 mm (0.39 in) and 50 mm (2.0 in)
 per hour. Violent rain — when the precipitation rate is > 50 mm (2.0 in) per hour.
''' 
# Defino la cantidad mínima de datos para calcular los agregados
min_daily = 1
min_monthly = 30
#%% Generamos los agregados
df['fecha_hora'] = pd.to_datetime(df['fecha_hora'], format='%Y-%m-%d %H:%M:%S')
# monthly sin nan
#month_df_dropna = df.groupby(pd.Grouper(freq='M', key='fecha_hora'),dropna = False).sum()
# monthly con nan
#month_df0 = df.groupby(pd.Grouper(freq='M', key='fecha_hora')).sum()
month_df = df.groupby(pd.Grouper(freq='M', key='fecha_hora')).sum(min_count=min_monthly)
# daily
daily_df = df.groupby(pd.Grouper(freq='D', key='fecha_hora')).sum(min_count=min_daily)

#%% Genero gráfico de datos mensuales
month_df = month_df.dropna(axis=1, how='all')#borro las columnas que son todos nan
month_df = month_df.to_numpy()

plt.figure(figsize=(40, 60))
    #plt.matshow(T_estanque,aspect='auto')
plt.matshow(month_df[:,1:696],aspect='auto')
    #plt.colorbar()
plt.xlabel("Estaciones")
plt.ylabel("Meses")
plt.clim(0,200)
cbar = plt.colorbar()
cbar.set_label('[mm]',size=11)
#plt.title(nameplot)

#%% Genero gráfico diario
daily_df = daily_df.dropna(axis=1, how='all')#borro las columnas que son todos nan
daily_df = daily_df.to_numpy()

plt.figure(figsize=(40, 60))
    #plt.matshow(T_estanque,aspect='auto')
plt.matshow(daily_df[:,1:696],aspect='auto')
    #plt.colorbar()
plt.xlabel("Estaciones")
plt.ylabel("Días")
plt.clim(0,30)
cbar = plt.colorbar()
cbar.set_label('[mm]',size=11)
#plt.title(nameplot)