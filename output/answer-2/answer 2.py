#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd


# In[16]:


fd=pd.read_csv("main.csv")


# In[17]:


fd.head()


# In[22]:


fd.groupby('occupation').age.agg(['min', 'max'])


# In[ ]:




