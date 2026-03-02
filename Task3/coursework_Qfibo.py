#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input("Enter your number for N:"))
M = int(input("Enter your number for M:"))

def fibo(N, M):
    """ This function returns the list of Fibonacci numbers lower than N that are able to be divided by M
    This function written by Klingens on 27-02-2026
    
    Parameters
    -----------
    N (int) the input parameter number N
    M (int) the input parameter number M
    
    Return
    -------
    numbers (list) list containing all numbers lower than N that are able to be divided by M
    """
    previous = 0
    new = 1
    numbers = []
    while True:
        if previous < N and previous % M == 0:
            numbers.append(previous)
        elif new >= 100000:  # Statement to break the while loop, otherwise it will run eternally.
            break
        following = previous + new  # Calculates the next Fibonacci number
        previous = new
        new = following
    return numbers

print(f"The Fibonacci numbers that are less than N and can be divided by M are: {fibo(N,M)}")


# In[ ]:




