import numpy as np
data=np.genfromtxt('SSMA.csv',delimiter=',',dtype=None,skip_header=1,encoding=None)

print(data)

print(data[:10])

print(data.shape)

unique_sales=np.unique('SSMA.csv')
print(len(unique_sales))

all_positive=np.all('SSMA.csv')
print(all_positive)

arg_max=np.argmax('SSMA.csv')
print(arg_max)


