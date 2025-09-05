import numpy as np
a=np.genfromtxt('Z:\\STUDENT NOTES\\12 Python - Numpy, Pandas, Matplotlib\\Practice\\Students Social Media Addiction\\Students Social Media Addiction.csv',delimiter=',',dtype=None,names=True,encoding='utf-8')
b=['Age','Avg_Daily_Usage_Hours','Sleep_Hours_Per_Night','Mental_Health_Score','Conflicts_Over_Social_Media','Addicted_Score']
for i in b :
    print(f"{b}:{np.unique(a[i])}")

