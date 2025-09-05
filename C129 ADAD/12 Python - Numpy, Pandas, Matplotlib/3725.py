import pandas as pd
df = pd.read_csv('sales.csv')
#print(df.head())

'''mean_mrp = df['Item_MRP'].mean()
median_mrp = df['Item_MRP'].median()
std_mrp = df['Item_MRP'].std()
print(f"Mean MRP: {mean_mrp}")
print(f"Median MRP: {median_mrp}")
print(f"Standard Deviation of MRP: {std_mrp}")'''

'''heavy_items = df[df['Item_Weight'] > 10]
print(heavy_items)'''

'''missing_values = df.isnull().sum()
print(missing_values)

fat_content_counts = df['Item_Fat_Content'].value_counts()
print(fat_content_counts)
fat_content_counts = df.groupby(by=['Item_Fat_Content'])['Item_Fat_Content'].count()
print(fat_content_counts)

df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
print(df.head())
df.drop(columns=['Outlet_Establishment_Year'], inplace=True)
print(df.head())
df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
print(df.head())
sorted_df = df.sort_values(by='Sales', ascending=False)
print(sorted_df.head())

unique_outlet_types = df['Outlet_Type'].unique()
print(unique_outlet_types)'''


df.rename(columns={'Item_Outlet_Sales': 'Sales'}, inplace=True)
print(df.head())
subset_df = df[['Item_Type', 'Item_MRP', 'Sales']]
print(subset_df.tail())
