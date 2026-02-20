#!/usr/bin/env python
# coding: utf-8

# In[ ]:


D = float(input("Enter the day: "))
M = int(input("Enter the month: "))
Y = int(input("Enter the year: "))

JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5 #The function is altered from the formula in the article to round the final value.
print(JD)

