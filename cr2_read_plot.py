#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:14:37 2022

@author: nico
"""


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import plotly.express as px

saveplot = 0

#my_data0 = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt.data',delimiter=',')
my_data1 = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=15, usecols = range(1, 880))
coord = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=5,skip_footer=1434, usecols = range(1, 880))
#name = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=7,skip_footer=1435, usecols = range(1, 880),dtype=None)
name = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=3,skip_footer=1451, usecols = range(1, 880),dtype=None, encoding='utf-8')
my_data1[my_data1==-9999.0] = np.nan
#creo mi dataframe
df = pd.DataFrame(my_data1,columns=[name])

valores_nan = df.isna().sum()


lat = coord[0,:]
lon = coord[1,:]


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]


plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('% NaN Mon since 1900')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
if saveplot == 1:
    plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since1900.png', bbox_inches='tight', dpi=1000)
plt.show()


#lon = np.genfromtxt('/home/nico/Documentos/Drought/Mediciones/CR2/cr2_prAmon_2019/cr2_prAmon_2019.txt',delimiter=',' , skip_header=6,skip_footer=1433, usecols = range(1, 880))




t = range(1440)
plt.plot(t,my_data1[:,200])


#%% I want select from 1950 
#grep -n "1950-01" cr2_prAmon_2019.dates 
#601:1950-01

df = df.iloc[601:,:]
valores_nan = df.isna().sum()

valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]


plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('%NaN MonPP since 1950')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
if saveplot == 1:
    plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since1950.png', bbox_inches='tight', dpi=1000)
plt.show()

#%% i want select since 1979

#grep -n "1979-01" cr2_prAmon_2019.dates 
#949:1979-01


df = pd.DataFrame(my_data1,columns=[name])


df = df.iloc[949:,:]
valores_nan = df.isna().sum()

valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]

plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('%NaN MonPP since 1979')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
if saveplot == 1:
    plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since1979.png', bbox_inches='tight', dpi=1000)
plt.show()

#%% Select since 1990
#grep -n "1990-01" cr2_prAmon_2019.dates 
#1081:1990-01

df = pd.DataFrame(my_data1,columns=[name])


df = df.iloc[1081:,:]
valores_nan = df.isna().sum()

valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]

plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('%NaN MonPP since 1990')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
if saveplot == 1:
    plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since1990.png', bbox_inches='tight', dpi=1000)
plt.show()


#%% Since 2000
#grep -n "2000-01" cr2_prAmon_2019.dates 
#1201:2000-01

df = pd.DataFrame(my_data1,columns=[name])

df = df.iloc[1201:,:]
valores_nan = df.isna().sum()

valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]

plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('%NaN MonPP since 2000')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
if saveplot == 1:
    plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since2000.png', bbox_inches='tight', dpi=1000)
plt.show()

#%% Since 2010
#grep -n "2010-01" cr2_prAmon_2019.dates 
#1321:2010-01

df = pd.DataFrame(my_data1,columns=[name])


df = df.iloc[1321:,:]
valores_nan = df.isna().sum()

valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]

plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('%NaN MonPP since 2010')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
if saveplot == 1:
    plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since2010.png', bbox_inches='tight', dpi=1000)
plt.show()


#%%
#grep -n "2000-01" cr2_prAmon_2019.dates 
#1201:2000-01


df = pd.DataFrame(my_data1,columns=[name])


df = df.iloc[1201:,:]
valores_nan = df.isna().sum()

valores_nan20 = valores_nan[100*valores_nan/len(df)<20]
valores_nan30 = valores_nan[100*valores_nan/len(df)<30]

plt.figure(figsize=(3.841, 7.195), dpi=100)
cm = plt.cm.get_cmap('RdYlBu')
# We restrict to South America.
#ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
ax = world[world['name'] == 'Chile'].plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
#gdf.plot(lon,lat, color='red')
sc = plt.scatter(lon,lat,2, 100*valores_nan/len(df), cmap=cm)
plt.colorbar(sc)
plt.xlim((-80, -57)) 
plt.ylim((-57, -17)) 
plt.title('%NaN MonPP since 2000')
plt.text(-66,-20, "<20% "+str(len(valores_nan20)), fontsize=7)
plt.text(-66,-23, "<30% "+str(len(valores_nan30)), fontsize=7)
#plt.savefig('/home/nico/Documentos/Drought/Mediciones/figures/CR2PP_month_NaN_since1979.png', bbox_inches='tight', dpi=1000)
plt.show()





'''
world_filepath = gpd.datasets.get_path('naturalearth_lowres')
world = gpd.read_file(world_filepath)
world.head()

chile = world.loc[world['name'] == 'Chile'] # get Singapore row
boundaries = chile['geometry'] # get Singapore geometry
#lat = my_data[5,:]
#lat = str(lat)
'''

'''
        - código estación (el código nacional considerado en la Institución que genera los datos)
        - institución (el nombre de la Institución que genera los datos)
        - fuente (de acuerdo a lo indicado en FUENTES)
        - nombre de estación (nombre considerado en la Institución que genera los datos)
        - altitud (m.s.n.m.)
        - latitud (° decimales S)
        - longitud (° decimales W)
        - código de cuenca
        - nombre de cuenca
        - código de sub-cuenca
        - nombre de sub-cuenca
        - fecha de comienzo de observaciones
        - fecha de fin de observaciones
        - cantidad de observaciones
        - inicio de observaciones en estación automatica
'''




'''
df = px.data.gapminder()
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     animation_frame="year",
                     projection="natural earth")
fig.show()
'''