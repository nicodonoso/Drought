#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:51:42 2022

@author: nicod
Unir las mediciones de Agromet en el fomato de CR2
CR2 datos diarios y mensuales (DGA+DMC) -> 816 estaciones para precipitación acumulada diaria, y de 1145 estaciones para precipitación acumulada mensual, entre los años 1930 y 2020. OBS: Para el cálculo de los valores acumulados por mes, para los cuales hay cuatro o más días sin registro, también se asignó el valor  -9999.
Agromet (8 campos) datos horarios con estaciones desde 2013 (algunas, otras son posteriores)

1- Leer ambas
2- Hacer promedios diarios de agromet (en el fomato DMC 12 UTC-12 UTC)
3- Seleccionar solo la PP de agromet y dejarla en una columna con filas de tiempo
4- Ajustar los timestamp entre CR2 y unir Agromet
"""

import pandas as pd
#import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import plotly.express as px
#%% Leer
my_data1 = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=15, usecols = range(1, 880))
name = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=3,skip_footer=1451, usecols = range(1, 880),dtype=None, encoding='utf-8')
my_data1[my_data1==-9999.0] = np.nan
#creo mi dataframe
df = pd.DataFrame(my_data1,columns=[name])

#%%

headers = ['inicio_automatica']
dtypes = {'inicio_automatica':'str'}
parse_dates = ['inicio_automatica']
file = '/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt'
date = pd.read_csv(file, sep=',', header=None, names=headers, dtype=dtypes, parse_dates=parse_dates,usecols=headers,skiprows=14)
#date = pd.to_datetime(date, format='%Y%m.0').dt.strftime('%Y-%m')