#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
ecommerce_data = pd.read_csv('Amazon Sale Report.csv')

# Display the first few rows of the dataset
print(ecommerce_data.head())


# In[11]:


print(ecommerce_data.info())  # Summary information about the dataset
print(ecommerce_data.describe()) 


# In[13]:


#Check for missing values
print(ecommerce_data.isnull().sum())


# In[14]:


# Example 1: Sales analysis
sales_by_category = ecommerce_data.groupby('Category')['Amount'].sum()
print("\nSales by Category:")
print(sales_by_category)


# In[15]:


# Visualize sales by category
sales_by_category.plot(kind='bar', xlabel='Category', ylabel='Total Sales', title='Sales by Category')
plt.show()


# In[8]:


# Example 2: Market basket analysis (dummy example, replace with actual analysis)
# For demonstration purposes, let's create a histogram showing the distribution of purchase amounts
plt.hist(ecommerce_data['Amount'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Purchase Amounts')
plt.show()


# In[9]:


# Example 4: Sales forecasting (dummy example, replace with actual analysis)
# For demonstration purposes, let's create a line plot showing sales trend over time
ecommerce_data['Date'] = pd.to_datetime(ecommerce_data['Date'])
sales_over_time = ecommerce_data.groupby('Date')['Amount'].sum()
print("\nSales Trend over Time:")
print(sales_over_time)

# Visualize sales trend over time
sales_over_time.plot(kind='line', xlabel='Date', ylabel='Total Sales', title='Sales Trend over Time')
plt.show()

