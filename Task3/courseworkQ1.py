#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from math import sqrt

data = [2.3, 3.5, 5.6, 12.8, 10.3, 7.2, 5.0, 2.1, -2.0]

# Starting conditions

N = 0
sum_mu = 0
sum_sigma = 0

# Checks if a value in data is negative, if so it's removed from the list.
# For every iteration: the sum_mu gets higher by k, N by is upped by 1 and sum_sigma gets larger by (k-mu)**2. Mu is defined later in the code.

for k in data:
    if k < 0:
        data.remove(k)
    else:
        sum_mu += k
        N += 1
        sum_sigma += (k-mu)**2

mu = sum_mu/(N)  # Calculates the mean of the list, using the earlier calculated sum_mu.
sigma = sqrt(sum_sigma/(N))  # Calculates the standard deviation of the list, using the earlier calculated sum_sigma.

print(f"The average intensity of the data is: {mu}")
print(f"The standard deviation of the intensities is: {sigma}")
print()

# Below are the same calculations of the mean and standard deviation, but now done by NumPy using functions on the data. The data list is first converted to an array.

data_array = np.array(data)
mean = np.mean(data_array)
stdev = np.std(data_array)

print(f"The average intensity of the data calculated by NumPy is: {mean}")
print(f"The standard deviation of the intensities by NumPy is: {stdev}")

