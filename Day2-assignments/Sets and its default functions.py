#!/usr/bin/env python
# coding: utf-8

# In[35]:


lang={"c++","java","javascript","html","css"}
lang


# In[38]:


lang.add("ruby")
lang


# In[40]:


lang1={"c","java","html","perl"}
lang1


# In[42]:


lang.intersection(lang1)


# In[44]:


lang.union(lang1)


# In[46]:


lang.difference(lang1)


# In[49]:


lang.pop()


# In[51]:


lang


# In[54]:


lang2=lang.copy()
lang2

