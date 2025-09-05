import numpy as np


data=np.genfromtxt('SSMA.csv',delimiter=',',skip_header=1,dtype=None,encoding=None)
print(data[:5])
print(data.shape)

num_rows=data.shape[0]
num_cols=len(data.dtype.names)
print(f"No of rows: {num_rows},No of columns:{num_cols}")

df=np.genfromtxt('Sales.csv',delimiter=',',skip_header=1,dtype=None,encoding=None)
missing_values=np.isnun(df.astype(str))
print(f"missing values in each column: {np.sum(missing_values,axis=0)}")



















'''
data=np.genfromtxt('Sales.csv',delimiter=',',skip_header=1,dtype=None,encoding=None)
print(data.shape)

item_weights = data[:, 1].astype(float)
print("Min:", np.min(item_weights))
print("Max:", np.max(item_weights))
print("Mean:", np.mean(item_weights))
print("Standard Deviation:", np.std(item_weights))



data = np.genfromtxt('Sales.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
print(data[:5]) # Preview first 5 rows
#3. Determine the number of rows and columns in the dataset.
print(data.shape)
#4. Calculate the minimum, maximum, mean, and standard deviation for numerical columns.
item_weights = data[:, 1].astype(float)
print("Min:", np.min(item_weights))
print("Max:", np.max(item_weights))
print("Mean:", np.mean(item_weights))
print("Standard Deviation:", np.std(item_weights))
'''
