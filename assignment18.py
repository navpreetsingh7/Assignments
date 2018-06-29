#A18_Q1

import numpy as np
a=np.random.randint(10, size=(10, 1))
print(a)
z=np.mean(a, dtype=np.float64)
print("mean of elements is:"+str(z))

#A18_Q2
import numpy as np
b=np.random.randint(20, size=(20,1))
print(b)
v=b.var()
print("Variance is: "+str(v))
s=b.std()
print("Standard Deviation is: "+str(s))
print(s)

#A18_Q3
import numpy as np
x=10 * np.random.random_sample((10, 20)) +10
print(x)
y=5 * np.random.random_sample((20, 25)) +20
print(y)
c=np.matmul(x,y)
print(c)
d=np.sum(c)
print(c.shape)
print("Sum of elements is: "+str(d))


#A18_Q4

import math
print("QUESTION 4")
print("RANDOM ARRAY->")
x=np.random.random((10,1))
print(x)
i=0
l=[]
for i in range(0,10):
    ans=1/(1+math.exp(-(x[i,0])))
    l.append(ans)
print("f(x)")
print(l)