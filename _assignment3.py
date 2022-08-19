#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
print(pd.__version__)

#df=pd.read_csv('owid-covid-data.csv')
df=pd.read_csv('C:\pythonData\owid-covid-data.csv')
df.shape


# In[13]:


df.head(10)


# In[14]:


df.tail(5)


# In[17]:


#df.describe(include=object)
df.describe()


# In[30]:


df.drop(columns=['new_deaths_smoothed','new_cases_per_million','total_cases_per_million'],axis=1)


# In[42]:



df.rename(columns={'date': 'Date','location':'Country','continent': 'Continent','iso_code':'ISO_code'},inplace=True)


# In[40]:


df


# In[72]:


for col in df:
    print(df[col].unique())


# In[79]:


l=df['new_cases'].unique().tolist()
l


# In[88]:


df


# In[86]:


imputer = SimpleImputer(strategy='constant')
df2 = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
df2


# In[87]:





# In[100]:


df3 = df2.groupby(['Date','Country'])
df3.first()


# In[106]:


df4=df2.groupby(['Date','Country','total_cases','total_deaths','total_vaccinations']).sum().reset_index()
df4


# In[132]:


#df['total_cases','total_deaths','total_vaccinations'] = df['total_cases','total_deaths','total_vaccinations'].fillna(0)
df2['total_cases'] = df2['total_cases'].replace(['missing_value'],0)
df2['total_deaths'] = df2['total_cases'].replace(['missing_value'],0)
df2['total_vaccinations'] = df2['total_vaccinations'].replace(['missing_value'],0)
df2


# In[145]:


df6=df2[df2['total_deaths']>100000]
num_countries=df6['Country'].unique()
print(num_countries)
#len(num_countries)


# In[147]:


num_Dates=df6['Date'].unique()
len(num_Dates)


# In[ ]:




