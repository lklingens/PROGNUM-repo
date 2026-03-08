#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# User inputs

a = int(input("Enter your lower bound:"))
b = int(input("Enter your upper bound:"))
n = int(input("Enter your number of sums:"))
function = input("Enter your function: f(x) =")

x = np.linspace(a,b,n)  # Sets the bounds and the number of sums (n)

def montecarlo(function):
    """ A function that evaluates the integral of you input function"""
    y = eval(function)
    sums = sum(y)
    integral = ((b-a)/n)*sums
    return integral

print(f"The Monte Carlo integral evaluates to: {montecarlo(function)}")


# In[ ]:




