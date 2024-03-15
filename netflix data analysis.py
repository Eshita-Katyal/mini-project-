#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization
import plotly.graph_objects as go # Plotly graph objects
import warnings # handle warning messages
warnings.filterwarnings('ignore') # Ignore warning messages


# In[2]:


df= pd.read_csv('netflix_titles.csv')
df.head()


# In[3]:


import pandas as pd
     
# making data frame
data = pd.read_csv("netflix_titles.csv")
     
list(data.columns.values)


# In[6]:


df['country'].replace(np.nan, 'USA',inplace  = True)  
df['director'].replace(np.nan, 'No Director',inplace = True)  
df['cast'].replace(np.nan, 'No Cast',inplace = True)  
df['country'].replace(np.nan, 'Not Specify',inplace = True)  
df.isnull().sum()


# In[8]:


df = df.dropna()  
df.isnull().sum()  
df['rating'].value_counts() 


# In[15]:


import seaborn as sns
sns.countplot(data=df,x='type') # looking at kind of Films and TELEVISION shows  


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figsize=(12,8)
sns.countplot(x='rating',data=df)


# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv('netflix_titles.csv')
plt.figure(figsize=(12, 8))
sns.countplot(data=df,x='rating')
plt.show() 


# In[22]:


plt.figure(figsize=(12, 6))  
df[df["type"] == "Movie"]["release_year"].value_counts()[:20].plot(kind="bar", color="red")  
plt.title("Freq of Films which were released in different years and are available on Netflix")
plt.show()


# In[30]:


plt.figure(figsize=(12, 6))  
df[df["type"] == "TV Show"]["release_year"].value_counts()[:20].plot(kind="bar", color="blue")  
plt.title("Frequency of TELEVISION shows which were released in different years and are available on Netflix") 
plt.show()


# In[32]:


plt.figure(figsize=(12, 6))  
df[df["type"] == "Movie"]["listed_in"].value_counts()[:11].plot(kind="bar", color="black")  
plt.title("Top 11 Category of Films", size=18) 
plt.show()


# In[35]:


# Check the number of rows in the DataFrame after filtering
print(df[df["type"] =="TELEVISION Show"].shape[0])

