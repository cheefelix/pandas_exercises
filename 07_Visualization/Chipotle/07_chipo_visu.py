# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:08:10 2017

@author: felixche
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt 

chipo = pd.read_csv('chipo.txt', sep = '\t')

# check top 5
chipo.head()

# group by quantities
top_5_item = chipo.groupby('item_name').sum()
top_5_item = top_5_item.sort_values('quantity', ascending=False).head(5)

# create the plot
top_5_item.plot(kind='bar')

# Set the title and labels
plt.xlabel('Items')
plt.ylabel('Price')
plt.title('Most ordered Chipotle\'s Items')

# show the plot
plt.show()


# Create a scatterplot with the number of items orderered per order price

chipo.head()

# remove $ from price
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] 

# group
items_ordered = chipo.groupby('order_id').sum()
items_ordered = items_ordered.sort_values('quantity', ascending=False)

# creates the scatterplot
# plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green')
plt.scatter(x = items_ordered.item_price, y = items_ordered.quantity, s = 10, c = 'green')

# Set the title and labels
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)
