#!/usr/bin/env python
# coding: utf-8

# # working on Real Project with python

# ## The weather dataset

# ### here the Weather dataset is atimeseries dataset with per-hour information about the weather conditions at a particular location.it records Temperature Dew point temperature.Relatively humidity,wind speed,visibility,pressure and conditions
# ### This data is available as a CSV file we are going to analyse this data set using pandas Daraframe

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv(r"C:\Users\91824\Downloads\1. Weather Data.csv")


# In[3]:


data


# ## How to analyse the Dataframe?

# ## .head()
# #### it shows the first N rows in the data (by default N=5)

# In[4]:


data.head()


# ## .shape

# ### it shows the total no of rows and no of columns of the dataframe

# In[5]:


data.shape


# # .index
# ### this attribute provides the index of the dataframe

# In[6]:


data.index  


# # .columns
# ### it shows the name of each column

# In[7]:


data.columns


# # .dtypes
# ### it shows data type of each column

# In[8]:


data.dtypes


# # .unique()
# ### in a column,it shows all the uniques values.it can be applied on a single column only,not on whole dataframe

# In[11]:


data['Weather'].unique()


# # .nunique()
# ### it shows total no of unique value in each column.it can be applied in a single column as well as whole dataframe

# In[12]:


data.nunique()


# # .count()
# ### it shows total no of non null in each column.it can be applied in a single column as well as whole dataframe

# In[14]:


data.count()


# # .value_counts()
# ### in a column ,it shows all the unique values with their count.it can be applied in a single column only

# In[17]:


data['Weather'].value_counts()


# # .info()
# ###  provides basic information about the datatframe

# In[18]:


data.info()


# ## Q)1.Find all the unique 'Wind Speed' values in the data

# In[20]:


data.head(2)


# In[21]:


data.nunique()


# In[22]:


data['Wind Speed_km/h'].nunique()


# In[19]:


data['Wind Speed_km/h'].unique()


# ## Q)2.Find the number of times when the 'weather is exactly clear'.

# In[23]:


data.head(2)


# In[24]:


# value_counts()
data.Weather.value_counts()


# In[29]:


# filtering
data[data['Weather']=='Clear']


# In[30]:


# group by
data.groupby('Weather').get_group('Clear')


# ## Q)3.find the number of times when the 'Wind speed was exactly 4km/h'.

# In[32]:


data[data['Wind Speed_km/h'] == 4]


# ## Q4)Find out all the null values in the data

# In[35]:


data.isnull().sum()


# In[36]:


data.notnull().sum()


# ## 5)Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[38]:


data.head(2)


# In[44]:


data.head()


# In[43]:


data.head()


# In[46]:


data.rename(column={'Weather':'Weather condition'})


# In[ ]:




