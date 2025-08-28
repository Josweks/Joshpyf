#!/usr/bin/env python
# coding: utf-8

# In[62]:


# import libraries


# In[1]:


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns


# In[ ]:


# reading data for analysis


# In[2]:


df = pd.read_excel(r'/Users/joshpyf/Downloads/Dataset/Car_Sales_Kaggle_DV0130EN_Lab3_Start.xlsx')


# In[3]:


pd.set_option('display.max_columns',None)


# In[4]:


pd.set_option('display.max.row',None)


# In[5]:


df.head(3)


# In[ ]:


#Renaming the columns for better analysis


# In[6]:


df = df.rename(columns={'Unit Sales':'Unit_Sales','Year Resale Value':'Year_Resale_Value','HP Level':'HP_Level',\
                'Fuel Efficiency':'Fuel_Efficiency','Power Perf Factor':'Power_Perf_Factor','Curb Weight':'Curb_Weight',\
                'Latest Launch':'Latest_Launch','Retention %':'Retention','Fuel Capacity':'Fuel_Capacity','Engine Size':\
                          'Engine_Size','Retention Value':'Retention_Value'})


# In[7]:


df.head(2)


# In[50]:


#dataset summary


# In[8]:


df.shape


# In[9]:


df.info()


# In[21]:


#Checking for duplicate value


# In[10]:


df.duplicated().head()


# In[ ]:


#Checking for null value


# In[11]:


df.isnull().sum()


# In[23]:


#data types summary


# In[12]:


df.dtypes


# In[58]:


#lets the summary of dataset


# In[13]:


df.describe().head()


# In[ ]:


#lets see the number of rows and column.


# In[14]:


df.groupby(['Manufacturer','Model'])['Fuel_Capacity'].mean().to_frame(' avg capacity').reset_index()\
.sort_values(' avg capacity',ascending = False)[:10]


# In[ ]:


#Common calaculations


# In[15]:


df1 = df.groupby('Manufacturer')['Unit_Sales'].count().reset_index()\
.sort_values('Unit_Sales',ascending =False)[:10]


# In[16]:


df1.head()


# In[93]:


#groupby aggregate functions


# In[17]:


df_agg_funct = df.groupby('Manufacturer')['Price']


# In[18]:


df_agg_funct.max().sort_values(ascending = False).reset_index().head()


# In[19]:


df_agg_funct.min().sort_values(ascending = False).reset_index().head()


# In[20]:


df_agg_funct.sum().sort_values(ascending = False).reset_index().head()


# In[21]:


df_agg_funct.std().sort_values(ascending = False).reset_index().head()


# In[22]:


df_agg_funct.mean().sort_values(ascending = False).reset_index().head()


# In[23]:


df2 = df.groupby('Manufacturer')['Price'].agg(['max','mean','min','std'])\
.sort_values('max',ascending = False).reset_index().head()


# In[24]:


df2


# In[ ]:


#Using query function to retrieve certain data


# In[25]:


query_1 = df.query('Manufacturer == "BMW"').head()


# In[26]:


query_1


# In[ ]:


# Exstracting certain info with the filter function


# In[27]:


filter_1=df[df['Retention_Value']=="GOOD"].head(3)


# In[28]:


filter_1


# In[29]:


query_2 = df.query('Retention_Value =="POOR" and Engine_Size < 1.8').head()


# In[30]:


query_2


# In[ ]:


# Exstracting certain info with the filter function.


# In[31]:


filter_2 = df[df['Fuel_Efficiency']<=15][:3]


# In[32]:


filter_2


# In[ ]:


#data manipulation with the "isin" function.


# In[33]:


iteams = ['Audi','Toyota','Volkswagen']

filter_3 = df[df['Manufacturer'].isin(iteams)]


# In[34]:


filter_3.head()


# In[35]:


reg_filter1 = filter_3.filter(regex = '143',axis = 0)


# In[36]:


reg_filter1


# In[37]:


reg_filter2 = df.filter(regex = ('M'),axis = 1 )


# In[38]:


reg_filter2.head(3)


# In[39]:


df_ret = df


# In[76]:


df_ret.head(2)


# In[40]:


#Exstracting various datetime values.


# In[41]:


df_ret['Latest_Launch']=pd.to_datetime(df_ret['Latest_Launch'])


# In[42]:


df_ret['Months']=df_ret['Latest_Launch'].dt.month_name()


# In[43]:


df_ret['Months'].head()


# In[44]:


df_ret['Months'].value_counts().reset_index().rename(columns ={'index':'Months','Months':'Date'}).head()


# In[45]:


df_ret['Day']=df_ret['Latest_Launch'].dt.day_name()


# In[46]:


df_ret.head(3)


# In[190]:


# model count


# In[47]:


model_count1 = df['Model'].value_counts().reset_index()


# In[48]:


model_count1.head(2)


# In[189]:


#rename model columns.


# In[49]:


model_count2 = df['Model'].value_counts().reset_index().rename(columns={'Model':'Count','index':'Model'})


# In[50]:


model_count2.head(2)


# In[52]:


grop_by = df.groupby('Model')['Engine_Size'].sum()\
.sort_values(ascending = False).reset_index().head()


# In[53]:


grop_by


# In[54]:


df_ret['Total'] = df_ret.apply(lambda x:x['Unit_Sales'] + x['Price'],axis = 1)


# In[115]:


df_ret.head(4)


# In[114]:


#Extracting certain info.


# In[55]:


filter_1 = df[df['Latest_Launch']=='2012-02-02']


# In[56]:


filter_1


# In[57]:


filter_2 = df[df['Engine_Size'].isin ([3.5]) & (df['Retention_Value'] =='GOOD')]


# In[58]:


filter_2


# In[59]:


model_query = df[['Model','Vehicle_type','Fuel_Efficiency']].query('Vehicle_type =="Car" & Fuel_Efficiency == 15')


# In[60]:


model_query


# In[61]:


group_bys2 = df.groupby(['Manufacturer','Latest_Launch']).size().reset_index().drop([0],axis = 1)


# In[62]:


group_bys2.head()


# In[63]:


group_bys3 = df.groupby(['Manufacturer','Latest_Launch']).size().to_frame().drop([0],axis = 1)


# In[159]:


group_bys3.head(9)

