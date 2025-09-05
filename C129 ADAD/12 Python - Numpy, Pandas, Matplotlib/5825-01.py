import numpy as np
data=np.genfromtxt('Sales.csv',delimiter=',',dtype=None,skip_header=1,encoding=None)
'''
print(data)

a=np.sum(data[:,10].astype(float))
print(f",{a}")


sales_diff=np.max('Sales.csv')-min('Sales.csv')
print(sales_diff)

sales_index=np.argmax('Sales.csv')
print(sales_index)
                             

ts=np.sum(data[:,11].astype(float))
print(f"Total Sales: {ts}")

#Identify the items with the highest and lowest Item_Outlet_Sales.
max_sales_index = np.argmax(data[:, 11].astype(float))
min_sales_index = np.argmin(data[:, 11].astype(float))
print(f"Item with Max Sales: {data[max_sales_index]}")
print(f"Item with Min Sales: {data[min_sales_index]}")

total_sales = np.sum(data[:, 11].astype(float))
print(f"Total Sales: {total_sales}")
'''
max_sales_index = np.argmax(data)
print(f"Item with Max Sales: {data[max_sales_index]}")
