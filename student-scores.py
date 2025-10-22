#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
df = pd.read_csv("Week-5-Student-Scores 1.csv") 


# In[3]:


df.shape


# In[4]:


df.dtypes


# In[5]:


df.isnull().sum()


# In[6]:


df.duplicated().sum()


# In[7]:


diagnostics = pd.DataFrame({
    'Data Type': df.dtypes,
    'Missing Values': df.isnull().sum(),
    'Missing %': round((df.isnull().sum()/ len(df)) *100, 2) ,
    'Unique Values': df.nunique(),
    'Duplicates':[df.duplicated().sum()] + [''] * (len (df.columns) -1)
})

print(f"Shape of dataset: {df.shape}") 
diagnostics 


# In[8]:


# Get descriptive statistics for numeric columns
descriptive_stats = df.describe()


# In[10]:


# 3. Select Required Statistics and Rename (Corrected)
required_stats = ['mean', '50%', 'std', 'min', 'max', '25%', '75%']
descriptive_stats = descriptive_stats.loc[required_stats]
descriptive_stats = descriptive_stats.rename(index={'50%': 'median'})


# In[11]:


descriptive_stats = descriptive_stats.T


# In[12]:


print(descriptive_stats)


# In[ ]:




