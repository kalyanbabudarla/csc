import pandas as pd
#1. Load the dataset and display the first 5 rows.
df=pd.read_csv('Sales.csv')


print(df.head())

#2. Check for missing values in the dataset.
print(df.isnull().sum())

#3. Rename the Item_Outlet_Sales column to Sales.
df.rename(columns={'Item_Outlet_Sales','Sales'}, inplace=True)
print(df.head())

#4. Drop the Outlet_Establishment_Year column from the dataset.
df=df.drop('Outlet_Establishment_Year',axis=1)
print(df)

#5. Filter the dataset to include only rows where Item_Type contains the word "Snack."
snack_df=df[df['Item_Type'].str.contains('snack', na=False)]
print(snack_df)

#6. 14. Print the shape (rows and columns) and size (total elements) of the dataset.
print(df.shape)

#7. Display the unique values in the Outlet_Type column.
unique_val=df.unique('Outlet_Type',axis=1)
print(unique_val)

#8. Filter the dataset to display only Low Fat items with Sales greater than 1000.
low_fat=df[(df['Item_Fat_Content']=='Low_Fat') & (df['Sales']>1000)]
print(low_fat)

#9. Create a stacked bar plot showing the distribution of Sales across Item_Type for each Outlet_Type.
import matplotlib.pyplot as plt
df.rename(columns={'Item_Outlet_Sales','Sales'}, inplace=True)
grouped_stats=df.groupby(['Item_Type','Outlet_Type'])['Sales'].agg(['maen','std']).unstack()
grouped_stats.plot(kind='bar')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
'''
#10. Group the dataset by Outlet_Type and Item_Type, and calculate the sum of Sales.
grouped_df=df.groupby(['Outlet_Type','Item_Type'])['Sales'].sum()
print(grouped_df)
'''
