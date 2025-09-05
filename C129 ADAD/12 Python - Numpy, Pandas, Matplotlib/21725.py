import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv('Sales.csv')
'''
#print(df.head())
df.rename(columns={'Item_outlet_sales':'sales'}, inplace=True)
#print(df.head())
adv_agg=df.groupby(['Item_Fat_Content','Outlet_Location_Type'])['Sales'].mean()
print(adv_agg)

df=pd.read_csv('Students Social Media Addiction.csv')
#print(a)

df.rename(columns={'Students Social Media Addiction':'Relationship_Status'},inplace=True)
adv_agg=df.groupby(['Country','Gender'])['Students Social Media Addiction'].mean()
print(adv_agg)
'''
advanced_pivot = df.pivot_table(values='Sales', index='Outlet_Type', columns='Item_Type', aggfunc=['mean', 'sum'])
print(advanced_pivot)

