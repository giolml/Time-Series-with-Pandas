#!/usr/bin/env python
# coding: utf-8

# # TimeSeries with Pandas
# ### Author: Giovanni Roncancio
# ### Date: 5/12/2022

# Working with time-series data is an important part of data analysis.
# Starting with v0.8, the pandas library has included a rich API for time-series manipulations.
# 
# The pandas time-series API includes:
# 
# - Creating date ranges
#      - From files
#      - From scratch
#      
# - Manipulations: Shift, resample, filter
# - field accesors (e.g., hour of day)
# - Plotting 
# - Time zones (localization and conversion)
# - Dual representation (point-in-time vs interval)
# 
# 

# In[10]:


from datetime import datetime, date, time
import sys
sys.version


# In[18]:


import pandas as pd
from pandas import Series, DataFrame #Falata importar Panel, averiguar para que sirve
pd.__version__


# ## Example using tick data

# Sample trade ticks from 2011-11-01 to 2011-11-03 for a single security

# In[19]:


with open('data.csv', 'r') as fh:
    print fh.readline() # headers
    print fh.readline() # first row
    
#No compila por que no tengo el csv descargado en el computador.


# Parse_dates: use a list or dict for flexible (possibly multi-column) date parsing

# In[21]:


data = pd.read_csv('data.csv',
                  parse_dates={'Timestamp':['Date'.'Time']},
                  index_col='Timestamp')
data

#Toca descargar el Dataset


# In[23]:


ticks = data.ix[:, ['Price','Volumen']]
ticks.head()
#Volver a ejecutar


# **Resample: regularization and frequency conversion**

# In[26]:


bars = ticks.price.resample('1min', how='ohlc')
bars
#Error por que no esta cargado dataset todavia


# In[27]:


minute_range = bars.high - bars.low
minute_range.describe()


# In[28]:


minute_return = bars.close / bars.open - 1
minute_return.describe()


# Compute a VWAP using resample

# In[29]:


volume = ticks.Volume.resample('1min', how='sum')
vwap = value / volume


# In[ ]:




