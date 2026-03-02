#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = float(input("Enter a value for a:"))
b = float(input("Enter a value for b:"))
c = float(input("Enter a value for c:"))
triple = False

def istriple(a, b, c):
    if a**2 + b**2 == c**2:
        triple = True
        print(f"The point ({a}, {b}, {c}) is a Pythagorean triple")
    else:
        triple = False
        print(f"The point ({a}, {b}, {c}) is not a Pythagorean triple")
    return triple

print("The statement '(a, b, c) forms a triple' is:", istriple(a, b, c))


# In[ ]:




