import pandas as pd
#data=pd.read_csv("test.csv")
data={'name':['tom','jack','steve','ricky'],'age':[28,22,28,19]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)



import pandas as pd
import numpy as np

d={'name':pd.Series(['tom','jack','steve','ricky']),
    'age':pd.Series([23,24,25,26]),
    'Rating':pd.Series([5,6,7,8])}
df=pd.DataFrame(d)
print("the transpose of data series is")
print (df.T)
print(df.axes)
print(df.head(2))


