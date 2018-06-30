#A19_Q1
import pandas as pd
import numpy as np
data={'NAME':['NAVPREET'],'age':[22],'mail id':['navbajwa7@gmail.com'],'phone no.':[8437904647]}
df=pd.DataFrame(data)
print(df)
df.loc[1]=['mno',22,'abc@gmail.com',9876543210]
print(df)
#A19_Q2

data=pd.read_csv("text.csv")
df=pd.DataFrame(data)
print("FIRST FIVE ROWS")
print(df.head(5))
print("\n")
print("FIRST TEN ROWS->")
print(df.head(10))
print("BASIC statistics")
print(df.axes)
print("DATATYPES")
print(df.dtypes)
print("DIMENSIONS")
print(df.ndim)
print("SHAPE")
print(df.shape)
print("SIZE")
print(df.size)
print("LAST FIVE ROWS->")
print(df.tail(5))
