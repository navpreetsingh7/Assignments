#A6_Q1
r=int(input("enter the radius"))
def rad(r):
    return 22.7*(r*r)
print(rad(r))


#A6_Q2
i=0
sum=0
def perfect():
    for i in range(1,1000):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j

        if sum==i:
            print("%d"%(i))
    return 0
print("perfect num")
perfect()


#A6_Q3

def times_tables(n=12, t=1):
    if t == 11:
        return
    print(str(n) + "x" + str(t) + "=" + str(n*t))
    times_tables(n, t+1)
times_tables()

#A6_Q4
result=1
a=int(input("enter num"))
b=int(input("enter pow"))

def power(a,b):
    if b!=0:
        return (a*power(a,b-1))
    else:
        return 1
result=power(a,b)
print("ans =%d"%(result))

#A6_Q5
n=int(input("enter num"))
def factorial(n):
    if n==1:
       return 1
    else :
        return (n * factorial(n - 1))

dict={'num':n,'factorial':factorial(n)}
print(factorial(n))
print(dict)


