#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
from math import inf

# Given constants

A = float(input("Enter a value for the amplitude:"))
x0 = float(input("Enter a value for the maximum position:"))
sigma = float(input("Enter a value for the maximum width:"))
z0 = float(input("Enter a value for the offset in y:"))
x_l = float(input("Enter a value for the lower bound:"))
x_u = float(input("Enter a value for the upper bound:"))

def gauss(x, A, x0, sigma, z0):
    """A function that calculates the above mentioned function for x"""
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

x = np.linspace(-10, 10, 200)  # Create 200 samples between -10 and 10.
y = gauss(x, A, x0, sigma, z0)  # User defined function with calling environment values for y.

# Calculate the area between x = 0 and x = 2.5.

area, error = integrate.quad(gauss, x_l, x_u, args=(A, x0, sigma, z0))  # quad() calculates the area and the uncertainty, so we assign area to the are and error to the uncertainty.

# Plot the function

plt.plot(x, y, color='mediumpurple', label=r'$f(x)=Ae^{\frac{-(x-x_0)^2}{2\sigma^2}}+z_0$')
plt.fill_between(x, y, 0, where=(x >= x_l)&(x <= x_u), color='skyblue', label=f"Area = {area:.3g}")  # Fills the area under the curve for x values between 0 and 2.5
plt.title("Area under a Gaussian distribution")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()
plt.legend(loc='upper left')  # Place legend in upper left corner.
plt.show()


# In[ ]:




