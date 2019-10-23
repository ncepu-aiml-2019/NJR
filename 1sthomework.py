#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[]
for i in range(2,100):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        a.append(i)     
print(a)


# In[ ]:




