
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib notebook')
import seaborn as sns


# In[2]:

birth_data = pd.read_csv("Natality, 2007-2014-2.txt", sep="\t")
birth_data.head()


# In[3]:

birth_data['State'] = birth_data['County'].str.split(',').str[-1].str.strip()
birth_data.head()


# In[4]:

print birth_data['Delivery Method'].unique()


# In[5]:

states = birth_data[birth_data['State'].isnull() == False]['State'].unique()
state_birth_counts = {}
for state in states:
    state_birth_counts[state] = birth_data[birth_data['State'] == state]['Births'].sum()


# In[13]:

plt.figure(figsize=(10,4))
plt.xlim(-1, len(state_birth_counts))
plt.bar(range(len(state_birth_counts)), state_birth_counts.values(), align='center')
plt.xticks(range(len(state_birth_counts)), state_birth_counts.keys())
plt.xticks(fontsize=8)  
plt.yticks(fontsize=17)  
plt.xlabel("State", fontsize=18)  
plt.ylabel("Births", fontsize=18)  
plt.show()


# In[ ]:



