#!/usr/bin/env python
# coding: utf-8

# # Project Overview
# In this project i will take you through an interesting looking to a data of the financial side of Cinema industry to get some useful output that help the directors in the future​.

# ## Introduction
# 

# This data set contains information about 10,000 movies collected from The Movie Database (TMDb) including user ratings and revenue,we will investigate this data trying to answer following questions:
# Q1:Does revenue related to the budget of the production?
# Q2:Does the revenue affected by the voting?
# Q3:Does the production of movies increase with time,and whats the most years of production?
# Q4:What is the most popular movies kinds?

# *let import the modules that we will used.*

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import ast
get_ipython().run_line_magic('', 'matplotlib inline')


# *then read our files*

# In[2]:


df_1=pd.read_csv('movies.csv')


# **Let assessing and clean data**

# In[3]:


df_1.head()


# In[4]:


df_1.shape


# In[5]:


df_1.info()


# In[6]:


df_1.describe()


# In[22]:


df_1.columns


# *drop unused columns*
# 

# In[23]:


df_1.drop(['homepage','overview','keywords','title','tagline','status','id','original_language','spoken_languages','production_countries','production_companies'],inplace=True,axis=1)


# In[24]:


df_1.head()


# In[25]:


df_1.shape


# *change units of revenue and budgets to million*

# In[26]:


df_1.revenue=df_1.revenue/10**6
df_1.budget=df_1.budget/10**6


# In[27]:


df_1.head()


# In[28]:


df_1.dtypes


# *convert release_date data types into datetime*

# In[29]:


df_1['release_date']=pd.to_datetime(df_1['release_date'])


# In[30]:


df_1.dtypes


# In[31]:


df_1.duplicated().sum()


# In[32]:


df_1.isnull().sum()


# *Drop null values*

# In[33]:


df_1.dropna(inplace=True)


# In[34]:


df_1.isnull().sum().sum()


# ### Visualize Data

# In[35]:


df_1.hist(figsize=(10,10));


# In[ ]:


df_1.groupby([''])


# ### Answer questions and conclusions:

# #### Q1:Does revenue related to the budget of the production?

# In[103]:


def plot(x, y, x_label, y_label, title):
    plt.scatter(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True) 
    ax = plt.gca() 
    plt.draw()
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)       
    
plt.figure(figsize=(20,10)) 
plt.subplot(2, 2, 1) 
plot(df_1['budget'],df_1['revenue'], 'budget', 'revenue', 'Relation Between Budget and revenue' )
   


#                      *There is on certian corelation between budget and revenue in most cases*

# #### Q2:Does the revenue affected by voting

# In[107]:


def plot(x, y, x_label, y_label, title):
    plt.scatter(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True) 
    ax = plt.gca() 
    plt.draw()
    for tick in ax.get_xticklabels():
        tick.set_rotation(0)       
    
plt.figure(figsize=(20,10)) 
plt.subplot(2, 2, 1) 
plot(df_1['vote_average'],df_1['revenue'], 'vote_average', 'revenue_', 'Affecting of votting in revenue' )


#                                     * The votes between 6-8 have the most revenues*

# #### Q3:Does the production of movies increase with time,and whats the most years of production,does the revenues also increase with time?

# In[108]:


df_1.release_date.hist()
plt.xlabel('years of production')
plt.ylabel('No.of released moeies')
plt.title('No.of released movies with time')


#      *we can notice that production of movies increase by time ,and the most years of ptoduction is between 1998-2018*

# In[109]:


df_1.groupby("revenue").release_date.hist()
plt.xlabel('Years')
plt.ylabel('revenues in M')
plt.title('Revenues with time')


#                  *we can notice here that investment in cinema is a good investment by time*

# ### Q4:What is the most popular movies kinds?

# *note:I get the idea of this function from stackoverflow and this is its link
# https://stackoverflow.com/questions/57604212/how-to-split-a-list-of-dictionaries-into-multiple-columns-keeping-the-same-index*

# In[110]:


out={}

for i ,(k,v) in enumerate(df_1['genres'].items()):
    df_2=pd.DataFrame(eval(v))
    if df_2.empty:
        out[(i,k)]=pd.DataFrame(index=[0],columns=['id'])
    else:
        out[(i,k)]=df_2

df_2 = pd.concat(out, sort=True).reset_index(level=[0,2], drop=True)
print (df_2)
   


# In[111]:


df_2.value_counts()


# In[112]:


df_2.value_counts().plot(x='id',y='name',kind='bar')
plt.xlabel('Type name')
plt.ylabel('No.of repetation of each kind')
plt.title('The most populars movies kinds')


#                             *  we can notice here the most popular movies kinds *

# ## Conculsion:

# After we exploring our data and answering our quation we can get that:
# *1-There is no certain corelation between budget and revenus in most case,but in few movies there are a postive corelation between them,but the over 1000 M revenus can be get with budget over 150 M  .
# *2-People voting affect the revenues, so if we get average voting of (6-8/10) we can expect a good revenues.
# *3-The 5th most popular movies types are (Drama,Comedy,Thriller,Action).
# *4-The last 20 years have noticed increase in released movies and there are increase in revenues.

# ## Limitation

# Here, the column popularity is confusing.. Jurassic World recives popularity of 32.98, whereas Avatar, Dark Knight have a popularity of <10...
# Similarly, the dataset does not include movies from other regions.. more recently movie called baahubali by director SS Rajamouli has been well received world wide and he is in the league of Nolan, Cameron.. but his movies are absent from this list

#                             **Thanks for your time spent in reviewing my work**

# In[ ]:




