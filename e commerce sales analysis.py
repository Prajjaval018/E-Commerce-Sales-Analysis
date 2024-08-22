#!/usr/bin/env python
# coding: utf-8

# In[25]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[26]:


dataset = pd.read_csv("Superstore_USA1.csv", encoding='latin1')


# In[27]:


dataset.head(2)





# In[28]:


dataset.isnull().sum()


# In[29]:


dataset['Product Base Margin'].fillna(dataset['Product Base Margin'].mean(), inplace=True)


# In[30]:


dataset['Order Priority'].value_counts()


# In[37]:


dataset['Order Priority'].unique()



# In[36]:


dataset['Order Priority']=dataset["Order Priority"].replace("Critical ","Critical")


# In[39]:


plt.figure(figsize=(5,4))
sns.countplot(x="Order Priority",data = dataset)
plt.title("Count of Order Priority")
plt.savefig("Count of order priority.jpg")
plt.show()


# In[42]:


dataset['Ship Mode'].value_counts()



# In[67]:


x=dataset['Ship Mode'].value_counts().index
y=dataset['Ship Mode'].value_counts().values


# In[45]:


plt.figure(figsize=(5,4))
plt.pie(y,labels=x,startangle=60,autopct="%0.2f%%")
plt.legend(loc=2)
plt.show()


# In[47]:


plt.figure(figsize=(5,4))
sns.countplot(x='Ship Mode',data=dataset,hue="Product Category")
plt.show()


# In[49]:


plt.figure(figsize=(6,4))
sns.countplot(x='Customer Segment',data=dataset)
plt.show()


# In[52]:


plt.figure(figsize=(6,4))
sns.countplot(x="Product Category", data=dataset[dataset["Product Category"]=="Office Supplies"], hue="Product Sub-Category")
plt.show()


# In[62]:


plt.figure(figsize=(5,4))
sns.barplot(x="Product Category",y="Profit",data=dataset,estimator='sum')
plt.show()


# In[63]:


dataset['State or Province'].value_counts()[:5]


# # PRODUCT CATEGORY

# In[64]:


plt.figure(figsize=(5,4))
sns.barplot(x="Product Category",y="Product Base Margin",data=dataset,estimator='sum')
plt.show()


# In[ ]:




