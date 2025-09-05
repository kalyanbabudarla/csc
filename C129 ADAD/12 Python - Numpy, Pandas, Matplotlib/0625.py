import numpy as np
a=np.genfromtxt('students social media addiction.csv', delimiter=',',names=True,dtype=None, encoding='utf-8')
'''
print(a)
print(a.shape)
print(a[:5])
'''
b=[a]
for col in b:
    print(f"{col}-Min: {nunmin(data[col])}")
