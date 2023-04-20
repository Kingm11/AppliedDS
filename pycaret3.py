#!/usr/bin/env python
# coding: utf-8

# Import libraries and load dataset

# In[1]:


from pycaret.datasets import get_data
from pycaret.classification import *
data = get_data('iris')


# 
#  Setup the pipeline
# 

# In[2]:


clf = setup(data, target='species')


# Compare models
# 

# In[3]:


best_model = compare_models()


# Plot the ROC curve

# In[4]:


plot_model(best_model, plot='auc')


# Predict on new data

# In[5]:


new_data = data.drop('species', axis=1).sample(5)
predict_model(best_model, data=new_data)


# In[ ]:




