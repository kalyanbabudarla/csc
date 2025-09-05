'''
import numpy as np
a=np.genfromtxt('Sales.csv',delimiter=',',skip_header=1,dtype=None,encoding=None)
print(a)
'''

import pandas as pd
import matplotlib.pyplot as plt

a=pd.read_csv('Sales.csv')
print(a.head())

a.rename(columns={'Item_Outlet_Sales':'Sales'},inplace=True)
print(a.head())

adv_agg=a.groupby(['Item_Fat_Content','Outlet_Location_Type'])['Sales'].mean()
print(adv_agg)

