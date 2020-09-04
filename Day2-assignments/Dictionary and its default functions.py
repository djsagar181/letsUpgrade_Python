#!/usr/bin/env python
# coding: utf-8

# In[4]:


dit={"name":"sagar",
    "color":"Blue",
    "languages":"javascript",
    "rank":1}
dit


# In[7]:


dit.get("name") #gets the value of the mentioned key


# In[14]:


dit.values() #gets the all values of the dictionary


# In[18]:


dit.fromkeys("color") #created the sequence of dictionaries from the color key


# In[23]:


dit1=dit.copy() #copies the dit into dit1
dit1


# In[25]:


dit.popitem()#removes last key and value


# In[27]:


dit #shows the dictionary after poping the last element


# In[31]:


dit.pop('color') #removes the mentioned key from the dictionary


# In[32]:


dit

