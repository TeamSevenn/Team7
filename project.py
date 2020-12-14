#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as no
import pandas as pd
import matplotlib.pylab as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 10, 6


# In[8]:


pwd


# In[16]:


varibale = pd.read_csv(r"C:\\Users\\Scarvi\Downloads\AirPassengers.csv")


# In[18]:


data=pd.read_csv("C:\\Users\\Scarvi\Downloads\AirPassengers.csv")


# In[19]:


data.head()


# In[23]:


data['Month']=pd.to_datetime(data['Month'], format='%Y-%m')


# In[25]:


from pandas import to_datetime


# In[26]:


data.columns=['ds', 'y']
data['ds']= to_datetime(data['ds'])


# In[27]:


plt.figure(figsize=(12,6))
plt.plot(data.set_index(['ds']))


# In[ ]:




