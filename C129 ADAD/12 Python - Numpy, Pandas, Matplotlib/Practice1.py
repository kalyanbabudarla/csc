import numpy as np
data=np.genfromtxt('Sales.csv',delimiter=',',names=True,dtype=None,encoding='utf-8')
'''
print(data)

print(data.shape)

num_rows=data.shape[0]
num_cols=len (data.dtype.names)
print(f"No of the rows: {num_rows}, No of the column: {num_cols}")

unique_item_types = np.unique(data['Item_Type'])
print(f"Number of unique Item Types: {len(unique_item_types)}")
print(unique_item_types,end='')

low_fat_rows = data[data['Item_Fat_Content'] == 'Low Fat']
print(low_fat_rows)

print(data[['Item_MRP', 'Item_Outlet_Sales']])

weight_diff = np.nanmax(data['Item_Weight']) - np.nanmin(data['Item_Weight'])
print(f"Difference between max and min Item Weights: {weight_diff}")

unique_outlet_types, counts = np.unique(data['Outlet_Type'], return_counts=True)
for outlet_type, count in zip(unique_outlet_types, counts):
    print(f"{outlet_type}: {count}")

max_sales_item = data[np.argmax(data['Item_Outlet_Sales'])]
min_sales_item = data[np.argmin(data['Item_Outlet_Sales'])]
print(f"Item with highest sales: {max_sales_item}")
print(f"Item with lowest sales: {min_sales_item}")

numerical_columns = ['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales']
for col in numerical_columns:
    print(f"{col} - Min: {np.nanmin(data[col])}, Max: {np.nanmax(data[col])}, Mean: {np.nanmean(data[col])}, Std: {np.nanstd(data[col])}")

mrp_mean = np.nanmean(data['Item_MRP'])
mrp_std = np.nanstd(data['Item_MRP'])
upper_bound = mrp_mean + 3 * mrp_std
lower_bound = mrp_mean - 3 * mrp_std
outliers = data[(data['Item_MRP'] > upper_bound) | (data['Item_MRP'] < lower_bound)]
print("Outliers in Item MRP:")
print(outliers)

unique_item_types = np.unique(data['Item_Type'])
print(f"Number of unique Item Types: {len(unique_item_types)}")
print(unique_item_types,end='')

low_fat_rows=data[data['Item_Fat_Content']=='Low Fat']
print(low_fat_rows)

print(data[['Item_MRP','Item_Outlet_Sales']])

wd=np.nanmax(data['Item_Weight'])-np.nanmin(data['Item_Weight'])
print(f"difference between max and min Item Weight: {wd}")

unique_item_types = np.unique(data['Item_Type'])
total_sales_by_item_type = {item_type: np.nansum(data['Item_Outlet_Sales'][data['Item_Type'] == item_type]) for item_type in unique_item_types}
for item_type, total_sales in total_sales_by_item_type.items():
    print(f"Item Type {item_type} - Total Sales: {total_sales}")

u, counts = np.unique(data['Outlet_Type'], return_counts=True)
for outlet_type, count in zip(u, counts):
    print(f"{outlet_type}: {count}")    

mxs=data[np.argmax(data['Item_Outlet_Sales'])]
mns=data[np.argmin(data['Item_Outlet_Sales'])]
print(f"Item with highest sales: {mxs}")
print(f"Item with lowest sales: {mns}")

mv={col:np.isnan(data[col]).sum() for col in data.dtype.names if data[col].dtype.kind in 'f'}
print(mv)
'''
ts=np.nansum(data['Item_Outlet_Sales'])
ts1=np.nansum(data['Item_MRP'])
ts2=np.nansum(data['Item_Visibility'])
print(f"Total Amount: {ts}")
print(f"Total Amount: {ts1}")
print(f"Total amount: {ts2}")
