import numpy as np
data=np.genfromtxt('Sales.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

print(data)

print ("10. Identify the items with the highest and lowest Item_Outlet_Sales.?")
print ()
mxsi=data[np.argmax(data['Item_Outlet_Sales'])]
mnsi=data[np.argmin(data['Item_Outlet_Sales'])]
print(f"Highest sales of the items: {mxsi}")
print()
print(f"Lowest sales of the items: {mnsi}")

print ("15. Calculate the average sales amount for each outlet..?")
print ()
uo= np.unique(data['Outlet_Identifier'])
for outlet in uo:
    avg_sales=np.nanmean(data['Item_Outlet_Sales'][data['Outlet_Identifier']==outlet])
    print(f"Outlet{outlet}-Average Sales : {avg_sales}")
print()

print ("14. Find the items with the highest Item_MRP value...?")
print()
mmi=data[np.argmax(data['Item_MRP'])]
print(f"Item with highest MRP : {mmi}")

print()
def a(x):
    return x*5
print(a(2))

print()
print ("17. Analyze how sales have grown over the years.?")
print()
uy=np.unique(data['Outlet_Establishment_Year'])
for year in uy:
    tsy=np.nansum(data['Item_Outlet_Sales'][data['Outlet_Establishment_Year']==year])
    print(f"Year{year}-Total Sales : {tsy}")
print()


print ("18. Identify outliers in Item_MRP..?")
print()
mrpmean=np.nanmean(data['MRP'])
mrpstd=np.nanstd(data['MRP'])
ub=mrpmean+3*mrpstd
lb=mrpmean-3*mrpstd
outliers=data[(data['MRP']>ub)|(data['MRP']<lb)]
print("Outliers in Item MRP :")
print(outliers)
print()


print ("19. Calculate total sales based on Outlet_Location_Type...?")
print()
unique_locations = np.unique(data['Outlet_Location_Type'])
for location in unique_locations:
    total_sales_location = np.nansum(data['Item_Outlet_Sales'][data['Outlet_Location_Type'] == location])
    print(f"Location {location} - Total Sales: {total_sales_location}")
