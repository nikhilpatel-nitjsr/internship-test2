#!/usr/bin/env python
# coding: utf-8

# In[64]:


import numpy as np
import pandas as pd


# In[65]:


df=pd.read_csv("main.csv")


# In[66]:


df.head()


# In[69]:


c = df.groupby('Team').sum()
c = c.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)
c.iloc[:, -5:-3]


# In[ ]:




