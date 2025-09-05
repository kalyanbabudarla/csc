import numpy as np

sales=np.array([55,69,33,458,789,12000,555,100000,373,2839,7392,737,4529,564,78,4593,567,258,645,198])

print('Total Data :', sales)

print('Shape of Data :', sales.shape)

total_sum=np.sum(sales)
print('Sum of the Total :', total_sum)

arg_max=np.max(sales)
print('Arg of the Maximum :', arg_max)

average_sales=np.mean(sales)
print('Average of Sales :', average_sales)

#Sales of the data (high & low)
max_sales=np.max(sales)
min_sales=np.min(sales)
print('Maximum of Sales :', max_sales)
print('Minimum of Sales :', min_sales)

cumulative_sales=np.cumsum(sales)
print('Cumulative of the Sales :', cumulative_sales)

mean_sales=np.mean(sales)
std_sales=np.std(sales)
print('Mean of the Sales :', mean_sales)
print('Standed Deviation of the Sales :', std_sales)
outlier_mask=(sales>mean_sales+2*std_sales) | (sales<mean_sales-2*std_sales)
outliers=sales[outlier_mask]
print('Outliers sales values :', outliers)

diff_sales=np.diff(sales)
print('Diff of the Sales :', diff_sales)
pct_sales=diff_sales / sales[:-1]*100
print('Day-Over-Day Sales Changes :',diff_sales)
print('Day-Over-Day % Change :', pct_sales)

condition=(sales>300)&(sales<10000)
selected_sales=sales[condition]
print('Sales between 300 and 10000 :', selected_sales)

print('Total sales :', np.sum(sales))
print('Average sales :', np.mean(sales))
print('Highest sales :', np.max(sales))
print('Lowest sales :', np.min(sales))

low,high=200,10000
filtered_sales =sales[(sales>=low)&(sales<=high)]
print(f'Sales between {low} and {high} :', filtered_sales)

high_sales_day=np.where(sales)[0]
print('Days with sales < 10000 :', high_sales_day)












'''
sorted_indices=np.argsort(sales[:: -1])
top_3_indices=sorted_indices[:3]
top_3_sales=sales[top_3_iddices]
print('Top 3 Sales Days (indices) :',top_3_indices)
print('Top 3 Sales Values :',top_3_sales)
'''
