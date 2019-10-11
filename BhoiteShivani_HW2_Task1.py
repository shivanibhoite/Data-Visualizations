#!/usr/bin/env python
# coding: utf-8

# # Task 1

# In[2]:


import pandas as pd


# In[9]:


#Reading the CSV file
data = pd.read_csv("/Users/shivanibhoite/Desktop/DataScience/Assignment2/dataPreP.csv") 


# In[18]:


print("--------------Printing the first 5 rows from the data given ---------------")
data.head()


# In[11]:


print("--------------Data Description-----------")
print("")
print('---The data provides has rows, columns -->',data.shape)
print("")
print("")
print("---These are the column headers -->")
print(data.columns)
print("")
print("----These are the column type -->")
print(data.dtypes)
print("")
print("----Data Description for the numeric values-->")
data.describe()


# In[13]:


#Making the quantative file
quantative = data[['Attr 4','Attr 5','Attr 6','Attr 7','Attr 8','Attr 9','Attr 10','Attr 11','Attr 12']]

quantative.to_csv(r'/Users/shivanibhoite/Desktop/DataScience/Assignment2/Quantitative.csv')
print("Printing the first 5 rows of the Quantative.csv file")
quantative.head()


# ### The Quantitative.csv has 9 columns

# In[14]:


#Making the quantative file
others = data[['Attr 1','Attr 2','Attr 3','Labels']]

others.to_csv(r'/Users/shivanibhoite/Desktop/DataScience/Assignment2/Others.csv')
print("Printing the first 5 rows of the Others.csv file")

others.head()


# ### The Others.csv has 4 columns

# In[ ]:




