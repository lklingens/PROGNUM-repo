#!/usr/bin/env python
# coding: utf-8

# In[1]:


previous = 1
new = 2

for k in range(98): #the first two numbers are known, so we need to go 98 steps further for the 100th number
    following = previous + new 
    previous = new
    new = following

print(f"The 100th number in the Fibonacci sequence is {new}")
    


# In[ ]:




