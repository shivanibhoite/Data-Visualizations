#!/usr/bin/env python
# coding: utf-8

# # Task 2 

# ### Importing the libraries

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

import seaborn as sns
from pandas.plotting import scatter_matrix


# In[2]:


qdata = pd.read_csv("/Users/shivanibhoite/Desktop/DataScience/Assignment2/Quantitative.csv", sep=',') 


qdata = qdata.loc[:, ~qdata.columns.str.contains('^Unnamed')] #removing the unamed column

print("")
qdata.head()


# ## Generating the Data for Summary Table Report

# In[3]:


print("---Data for Summary Table report is as follows for a continuous features:---")


reportdf = pd.DataFrame(columns=['Count', '%Miss', 'Card','Min','1st Quartile','Mean',
                                 'Median','3rd Quartile','Max','Std Dev'])


for(name,series) in qdata.iteritems():

    reportdf = reportdf.append({'Count':qdata[name].size, 
                                '%Miss':sum(qdata[name].isnull().values.ravel()), 
                                'Card':qdata[name].unique().size,
                                'Min':qdata[name].min(),
                                '1st Quartile':qdata[name].quantile(0.25),
                                'Mean':qdata[name].mean(),
                                'Median':qdata[name].mean(),
                                '3rd Quartile':qdata[name].quantile(0.75),
                                'Max':qdata[name].max(),
                                'Std Dev':qdata[name].std()
                                
                               }, ignore_index=True)


reportdf.head()


# ## Making Equal Width Historgrams

# In[4]:


#Plotting the historgrams
print("----Equal Width Historgrams---------")    
qdata.diff().hist(color='blue', figsize=(10,10), alpha=0.5, bins=30)


# ## Making Violin Plots

# In[7]:




print("----Horizontal Violin Plots---------")    

ax = sns.violinplot(data=qdata,scale="width", palette="Set3",orient="h")


# ## Generating Scatter Plot Matrix

# In[8]:


sns.set(style="ticks")

sns.pairplot(qdata)

print("Using seaboran")


# ## Generating the Covariance table of the data

# In[12]:


print("---------Covariance table of the data---------")

qdata.cov()


# 
# ## HeatMap for the Covariance Table

# In[11]:


print("--------Heat Map for Covariance----------")

cov=qdata.cov()
sns.heatmap(cov, xticklabels=cov.columns, yticklabels=cov.columns, center=0,linewidths=.5)


# ## Generating the Correlation  Table from the data

# In[10]:


print("---------Correlation table of the data---------")

qdata.corr()


# ## HeatMap for Correlation Table

# In[14]:


print("--------Heat Map for Correlation----------")

corr=qdata.corr()
sns.heatmap( qdata.corr(), xticklabels=corr.columns, yticklabels=corr.columns, center=0,linewidths=.5)


# In[ ]:




