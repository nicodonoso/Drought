#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 01:25:20 2022

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

df = pd.read_csv (path_and_file, sep =',', parse_dates=['fecha_hora'])

#%%

dc = df.describe()

count = dc.iloc[[0]].transpose()
minim = dc.iloc[[3]].transpose()
maxm = dc.iloc[[7]].transpose()

tabla0 = count.join(minim)
tabla0 = tabla0.join(maxm)

acum = df.sum()
s = pd.Series(acum,name="Acumulado")
s = s.to_frame()

tabla0 = tabla0.join(s)
tabla0 = tabla0.drop('indx')

with open('/home/nico/Documentos/Drought/python/mytable.tex', 'w') as tf:
     #tf.write(tabla0.to_latex(index=False))
     tf.write(tabla0.to_latex())

nann = df.isna().sum()

