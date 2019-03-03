# -*- coding: utf-8 -*-
"""
@author: Sri Manikanth Nunna
"""

import pandas as pd

#Import Data
my_data = pd.read_csv('list_attr_celeba.csv')

#Replace -1 with 0
my_data['Attractive'] = my_data['Attractive'].map({1: 1, -1: 0})

#Export to CSV file
my_data.to_csv('list_attr_celeba.csv', encoding='utf-8', index = False)