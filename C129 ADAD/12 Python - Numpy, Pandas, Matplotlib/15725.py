import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales.csv')
df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)


print(df.head)

print(df.head())

print(df.shape)
'''
df.set_index('Date', inplace=True)
df['Sales'].plot(figsize=(12, 6))
plt.title('Sales Over Time')
plt.ylabel('Sales')
plt.show()
'''

grouped_stats = df.groupby(['Outlet_Type', 'Item_Type'])['Sales'].agg(['mean', 'std']).unstack()
grouped_stats.plot(kind='line')
grouped_stats.plot(kind='bar')
plt.title('Mean and Standard Deviation of Sales by Outlet and Item Type')
plt.xlabel('Outlet and Item Type')
plt.ylabel('Sales')
plt.show()

'''
df['Sales'].head(8000).plot(figsize=(10,20))
df['Sales'].head(8000).plot(kind='bar')
df['Sales'].head(8000).plot(figsize=(1,1))
df['Sales'].head(8000).plot(kind='line')
df['Sales'].head(100).plot(kind='line')
df['Sales'].head(100).plot(kind='line')
df['Sales'].head(100).plot(kind='line')
df['Sales'].head(100).plot(kind='line')
df['Sales'].head(100).plot(kind='line')
df['Sales'].head(100).plot(kind='line')
plt.title('Sales for First 8000 Rows')
plt.xlabel('Index')
plt.ylabel('Sales')
plt.show()
'''

