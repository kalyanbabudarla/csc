'''
import numpy as np
data=np.genfromtxt('sales.csv',delimiter=',',skip_header=1,dtype=None,encoding=None)
print(data)
print(data.shape)
'''
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('D:\\Sales.csv')
#b=pd.read_csv('Students Social Media Addiction.csv')
#print(a.head,b.head,a.shape,b.shape)
#a.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True) 
'''b['Students Social Media Addiction.csv'].head(50).plot(kind='line')
plt.title('sales for First 50 Row')
plt.xlabel('Index')
plt.ylabel('Students Social Media Addiction.csv')
plt.show()'''

'''df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

filtered_df = df[(df['Fat'] == 'Low Fat') & (df['Sales'] > 1000)]
print(filtered_df)

df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
multi_index_df = df.set_index(['Outlet_Type', 'Item_Type'])
sales_multi_index = multi_index_df['Sales'].groupby(level=[0, 1]).sum()
print(sales_multi_index)'''

'''df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
df['Cumulative_Sales'] = df.groupby('Outlet_Type')['Sales'].cumsum() 
df.pivot_table(values='Cumulative_Sales', index='Item_Type', columns='Outlet_Type').plot() 
plt.title('Cumulative Sales by Outlet Type') 
plt.xlabel('Index') 
plt.ylabel('Cumulative Sales')
plt.show()'''

'''median_visibility = df['Item_Visibility'].median()
filtered_df = df[(df['Item_Visibility'] > median_visibility) & (df['Item_Fat_Content'] == 'Low Fat')]
print(filtered_df)
plt.show() 

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
print(df.head())

df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
df.set_index('Date', inplace=True)
df['Sales'].plot(figsize=(12, 6))
plt.title('Sales Over Time')
plt.ylabel('Sales')
plt.show()

df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
advanced_pivot = df.pivot_table(values='Sales', index='Outlet_Type', columns='Item_Type', aggfunc=['mean', 'sum'])
print(advanced_pivot)'''

df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
grouped_df = df.groupby(['Outlet_Type', 'Item_Type'])['Sales'].sum()
print(grouped_df)
