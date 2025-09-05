import numpy as np
data=np.array([585,2655,478,369,796,7854,246,124,493,492,246,846,4663])

print(data)
print(data.shape)
total_data=np.sum(data)
print('Total data :',total_data)
print('Sum of Total :',np.sum(data))
print('Sum of average :',np.mean(data))
print('Lowest data :',np.min(data))
print('Highest data :',np.max(data))

mean=np.mean(data)
std=np.std(data)
outlier_mask=(data>mean+2*std)|(data<mean-2*std)
outliers=data[outlier_mask]
print('Outlier data values :',outliers)

'''
import pandas as pd
df=pd.read_csv('Sales.csv')
print(df.head(5))
'''

#condi=(data>500)&(data<1000)
#selec_data=data[condi]
#print('Sales between 500 and 1000 :',selec_data)
#print('Sales between 500 and 1000 :',data[condi])
print('Data between 500 & 1000 :',(data>500&data<1000))
