#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import pandas as pd


# In[56]:


df=pd.read_csv("main.csv")


# In[57]:


df.head()


# In[58]:


df.dtypes


# In[59]:


df.set_index('Year')


# In[60]:


df.Population.isnull().sum()


# In[61]:


df=df.drop(columns="Total")


# In[62]:


df_decade = df.groupby(np.floor(df['Year']/10) * 10)[['Population','Violent', 'Property', 'Murder',
       'Forcible_Rape', 'Robbery', 'Aggravated_assault', 'Burglary',
       'Larceny_Theft', 'Vehicle_Theft']].sum()


# In[63]:


df_decade


# In[ ]:




