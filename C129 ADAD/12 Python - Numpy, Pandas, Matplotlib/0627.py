import numpy as np

a=np.genfromtxt('Sales.csv',delimiter=',',names=True, dtype=None,encoding=None, skip_header=1)

print('2. ',a[:2])

print('3. ',a.shape)

fat=a[a[:,2]=='Low Fat']
print(fat[:5])
