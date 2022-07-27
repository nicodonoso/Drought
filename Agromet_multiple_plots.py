#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 18:10:31 2022

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
fechas = df['fecha_hora']

#%% COnstruir 23 + 1 gráficos
indx = 30
ancho = 0.2
x = 15450
x = 15400
y = 1

#fig.set_size_inches(18.5, 10.5)
#fig.set_size_inches(40, 20)

for j in range(1,23+1):
    fig, ax = plt.subplots(indx,1)
    print(j)
    for i in range(indx*j-indx,indx*j):
        print('Indice plot i : '+str(i))
        print('0-29 indx: '+str(abs(i-indx*j)-1))
        if abs(i-indx*j)-1 != indx-1:
            print("sin fecha")
            ax[abs(i-indx*j)-1].plot(fechas,df[str(i)],linewidth=ancho,color='black')
            ax[abs(i-indx*j)-1].set_ylim([0,10])
            ax[abs(i-indx*j)-1].set_yticks([])
            ax[abs(i-indx*j)-1].set_xticks([])
            ax[abs(i-indx*j)-1].set_xlim([fechas[0], fechas[fechas.size-1]])
            #ax[i].text(15500,1,str(i))
            ax[abs(i-indx*j)-1].text(x,y,str(i),fontsize = 'xx-small')
            #ax[i-indx*j].set_xlim([fechas[0], fechas[fechas.size-1]])
        elif abs(i-indx*j)-1 == indx-1:
            print("entramos a las fechas")
            ax[abs(i-indx*j)-1].plot(fechas,df[str(i)],linewidth=ancho,color='black')
            #ax[i].set_ylim([0,10])
            ax[abs(i-indx*j)-1].set_yticks([])
            ax[abs(i-indx*j)-1].set_xlim([fechas[0], fechas[fechas.size-1]])
            ax[abs(i-indx*j)-1].text(x,y,str(i),fontsize = 'xx-small')
    fig.savefig('/home/nico/Documentos/Drought/Mediciones/figures/Validaciones_agromet/test3_2012-2022_'+str(j)+'.png', dpi=400)
    plt.clf()
#%%realizo grádico para los últimas 5 estaciones
indx = 6
ancho = 0.2
x = 15450
x = 15400
y = 1


fig, ax = plt.subplots(indx,1)
for i in range(indx):
    print(i)
    if i != indx-1:
        ax[i].plot(fechas,df[str(i+690)],linewidth=ancho,color='black')
        ax[i].set_ylim([0,10])
        ax[i].set_yticks([])
        ax[i].set_xticks([])
        ax[i].set_xlim([fechas[0], fechas[fechas.size-1]])
        #ax[i].text(15500,1,str(i))
        ax[i].text(x,y,str(i+690),fontsize = 'xx-small')
    else:
        ax[i].plot(fechas,df[str(i+690)],linewidth=ancho,color='black')
        #ax[i].set_ylim([0,10])
        ax[i].set_yticks([])
        ax[i].set_xlim([fechas[0], fechas[fechas.size-1]])
        ax[i].text(x,y,str(i+690),fontsize = 'xx-small')
        
fig.savefig('/home/nico/Documentos/Drought/Mediciones/figures/Validaciones_agromet/test3_2012-2022_24.png', dpi=400)






'''
#%% Funciona para 30 estaciones
indx = 30
ancho = 0.2
x = 15450
y = 1
fig, ax = plt.subplots(indx,1)
#fig.set_size_inches(18.5, 10.5)
#fig.set_size_inches(40, 20)
for i in range(indx):
    print(i)
    if i != indx-1:
        ax[i].plot(fechas,df[str(i)],linewidth=ancho,color='black')
        ax[i].set_ylim([0,10])
        ax[i].set_yticks([])
        ax[i].set_xticks([])
        ax[i].set_xlim([fechas[0], fechas[fechas.size-1]])
        #ax[i].text(15500,1,str(i))
        ax[i].text(x,y,str(i),fontsize = 'xx-small')
    else:
        ax[i].plot(fechas,df[str(i)],linewidth=ancho,color='black')
        #ax[i].set_ylim([0,10])
        ax[i].set_yticks([])
        ax[i].set_xlim([fechas[0], fechas[fechas.size-1]])
        ax[i].text(x,y,str(i),fontsize = 'xx-small')
        
fig.savefig('/home/nico/Documentos/Drought/Mediciones/figures/Validaciones_agromet/test3_2012-2022.png', dpi=100)
#%%
'''    
