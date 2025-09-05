import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Sales.csv')
df.rename(columns={'Item_Outlet_Sales':'Sales'}, inplace=True)
'''
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

sales_pivot = df.pivot_table(values='Sales', index='Item_Type', columns='Outlet_Location_Type', aggfunc='sum')
print(sales_pivot)

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
print(df.head())
'''
print(df.head,df.shape)
grouped_stats = df.groupby(['Outlet_Type', 'Item_Type'])['Sales'].agg(['mean', 'std']).unstack()
grouped_stats.plot(figsize=(10,20))
grouped_stats.plot(kind='bar')
grouped_stats.plot(kind='line')
grouped_stats.plot(kind='bar')
plt.title('Mean and Standard Deviation of Sales by Outlet and Item Type')
plt.xlabel('Outlet and Item Type')
plt.ylabel('Sales')
plt.show()

df.set_index('Date', inplace=True)
df['Sales'].plot(figsize=(12, 6))
plt.title('Sales Over Time')
plt.ylabel('Sales')
plt.show()
























'''import pandas as pd
a=np.genfromtxt('Sales.csv',delimiter=',',skip_header=1,dtype=None, encoding=None)
print(a)
print(a.shape)
print(a.info)


item_weights =a[:,1].astype(float)
print("Min:", np.min(item_weights))
print("Max:", np.max(item_weights))
print("Mean:", np.mean(item_weights))
print("Standard Deviation:", np.std(item_weights))
'''
