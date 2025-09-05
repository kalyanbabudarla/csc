import pandas as pd
df=pd.read_csv('Sales.csv')
print(df.head)

df.set_index('Date', inplace=True) 
df['Sales'].plot(figsize=(12, 6)) 
plt.title('Sales Over Time') 
plt.ylabel('Sales') 
plt.show() 
