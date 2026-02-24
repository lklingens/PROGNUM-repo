#!/usr/bin/env python
# coding: utf-8

# In[1]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
small_masses = []
print("The length of the masses list is:", len(masses))

for k in masses:
    if k <= masses[-2]:
        small_masses.append(k)

print("The new list with the masses smaller than the mass of the moon is:", small_masses)

m_slice = slice(6,None,1)
mass_slice = masses[m_slice]
print("The list with the 5 last masses of the original list is:", mass_slice)

length = len(mass_slice)
mass_sum = sum(mass_slice)
avg_mass = mass_sum/(length)
print("The average mass of the 5 item mass list is:", avg_mass)


# In[ ]:




