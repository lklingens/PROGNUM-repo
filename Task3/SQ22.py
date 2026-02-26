#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from math import cos, e

x = list(range(-5, 6))
print(x)
y = []

for i in x:
    result = (e**i+e**-i)/(2)
    y.append(result)

print(y)

# Make a plot

plt.plot(x, y, marker='o', color='b', markersize=8, label="Data points")
title = r"Catenary: $\frac{e^{x}+e^{-x}}{2}$"
plt.title(title, fontsize=18, color ='black')
plt.xlabel("x-values", fontsize=12)
plt.ylabel("y-values", fontsize=12)
plt.legend(fontsize=10)
plt.grid()
plt.show()


# In[ ]:




