import numpy as np
data = np.genfromtxt('Sales.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)

print(data[: 5])

print(data.shape)

unique_item=np.unique(data[:, 4])
print(f"unique item: {len(unique_item)}")





















'''
import numpy as np

data=np.genfromtxt('Sales.csv',delimiter=',',skip_header=1,dtype=None,encoding=None)

print(data)

max_sales=np.argmax(data[:, 11].astype(float))
print(f"{data[max_sales]}")
'''
