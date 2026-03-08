#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from numpy import sin, cos, exp, pi  # Functions a user can apply.
from scipy import integrate

my_func = input("Enter a function f(x):")

def userfunc(x, my_func):
    """A function that evaluates the user input"""
    function = eval(my_func)  # Evaluates the input (string) as a function in order to be used in the integral.
    return function

# Calculate the integral between 0 and pi for a given function and return any exceptions for the input.

try:
    integral, error = integrate.quad(userfunc, 0, pi, args=my_func)  # quad() calculates the integral and its uncertainty, so we assign inegral to the value and error to the uncertainty.
    print(f"The integral of {my_func} from 0 to pi using quad() gives: {integral:.4g}.")
except NameError as E:
    print(f"NameError: {E}. Enter a function that is defined earlier or known in the NumPy library.")
except TypeError as E:
    print(f"TypeError: {E}. Use the correct mathematical symbols for your function, for example use ** instead of ^.")
except SyntaxError as E:
    print(f"SyntaxError: {E}. The structure of your input is not correct.")
except Exception as E:
    print(f"Error: {E}.")

def MonteCarlo(my_func, a, b, N=100000):
    """A function that applies the Monte Carlo Integration to a given function, for random numbers between a and b. Any errors are returned trough exceptions"""
    try:
        x = np.random.uniform(a, b, N) # N amount of uniformly distributed numbers between a and b 
        y = np.array(userfunc(x, my_func))  # By using the earlier defined function, Monte Carlo can be used for any function that is entered.
        integral= (b-a)*np.mean(y)
    except NameError as E:
        print(f"NameError: {E}. Enter a function that is defined earlier or known in the NumPy library.")
    except TypeError as E:
        print(f"TypeError: {E}. Use the correct mathematical symbols for your function, for example use ** instead of ^.")
    except SyntaxError as E:
        print(f"SyntaxError: {E}. The structure of your input is not correct.")
    except Exception as E:
        print(f"Error: {E}.")
    return integral

print(f"The integral of {my_func} from 0 to pi using Monte Carlo gives: {MonteCarlo(my_func, 0, np.pi):.4g}")  # :.4g formats the number to 4 significant digits


# In[ ]:




