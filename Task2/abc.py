#!/usr/bin/env python
# coding: utf-8

# In[18]:


from math import *

a = float(input("Enter a number for a: "))
b = float(input("Enter a number for b: "))
c = float(input("Enter a number for c: "))

function = "f = a*x**2 + b*x + c"
D = b**2 - 4*a*c
print("The function is", function, "with the discriminant", D)

#Check the value of the discriminant function
if D > 0:
    x1 = -b + sqrt(D)/(2*a)
    x2 = -b - sqrt(D)/(2*a)
    solution = f"There are two solutions of f: x1 ={x1} and x2 ={x2}."
elif D == 0:
    x = x1 = x2 = -b/(2*a)
    solution = f"There is one solution of f: x ={x}."
else:
    solution = "There is no solution of f."

print(solution)


# In[ ]:




