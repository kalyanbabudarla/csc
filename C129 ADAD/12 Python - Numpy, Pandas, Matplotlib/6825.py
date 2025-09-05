import numpy as np

a=np.genfromtxt('Sales.csv',delimiter=',',dtype=None,encoding='utf-8',skip_header=0)

print(a)

print(a.shape)

print(a[: 10])

item_weights = a[:, 1].astype(float)
print("Min:", np.min(item_weights))
print("Max:", np.max(item_weights))
print("Mean:", np.mean(item_weights))
print("Standard Deviation:", np.std(item_weights))

unique_sales=np.unique (Sales.csv)
print(unique_sales)

data = np.genfromtxt('Sales.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
print(data[:10])
print(data.shape)


item_weights = data[:, 1].astype(float)
print("Min:", np.min(item_weights))
print("Max:", np.max(item_weights))
print("Mean:", np.mean(item_weights))
print("Standard Deviation:", np.std(item_weights))

sales=data[:, 10].astype(int)
print("max",np.max(Sales))

unique=np.unique(sales_data[:, 0])
print(\n Unique)

unique_item_types = np.unique(data[:, 4])
print(f"Unique Item Types: {len(unique_item_types)}")

item_mrp_sales = data[:, [5, 11]].astype(float)
print(item_mrp_sales[:5])




