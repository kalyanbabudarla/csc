import numpy as np

data=np.genfromtxt('Sales.csv',delimiter=',',dtype=None,encoding=None,skip_header=1)

print(data)

print(data.shape)

sales=([5822,45,12,12,52,225,598,5589,5858,698,6352,1233,78522,4662,5462,1769,5621,5586,])

total_sales=np.sum(sales)
print('Total Sales :',total_sales)

print('Total Sales',np.sum(sales))
print('Average of the Sales :',np.mean(sales))
print('Highest of the Sales :',np.max(sales))
print('Lowest of the Sales :',np.min(sales))

print('Madian Sales :',np.median(sales))

print('Variance of Sales :',np.var(sales))

print('Standard Deviation of Sales :',np.std(sales))

#Average_sales=np.mean(sales)
count_below_avg=np.sum(sales<Average_sales)
print('Days with sales below average :',count_below_avg)
