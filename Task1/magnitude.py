#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Sirius data
apparentMagnitude = input("Give value for the apparent magnitude: ")
absoluteMagnitude = input("Give value for the absolute magnitude: ")

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = float(apparentMagnitude)
M = float(absoluteMagnitude)

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
print(f"The distance to Sirius is {d} ly")


# In[ ]:




