#A5_Q1
i=0
emptylist=[]
while i<=4:
    val = int(input("ENTER THE VALUE"))
    emptylist.append(val)
    i=i+1
print(emptylist)


#A5_Q2
while (True):
    print("infinite")

#A5_Q3
a=[]
for i in range(1,5):
    num=int(input("enter the list"))
    a.append(num)
    print(a)

    b=[]
    for i in a:
        val=i*i
        b.append(val)
        print(b)

#A5_Q4
x=['NAV',30,33.4,1,'HELLO','BYE']
i=0
l_1=[]
l_2=[]
s_t=[]
y=[]

l_1 = [y for y in x if type(y) == int]
l_2 = [y for y in x if type(y) == float]
s_t = [y for y in x if type(y) == str]

print(l_1)
print(l_2)
print(s_t)

#A5_Q5

odd=[]
even=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

#A5_Q6
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

#A5_Q7
d={'name':'NAV','age':22,'city':'JAL'}
for i in d:
    print(d[i])
print(dict.keys(d))
print(dict.items(d))

#A5_Q8
a=[]
i=0
while i<=4:
   num=int(input("ENTER THE VALUE"))
   a.append(num)
   i+=1

print(a)
i=0

s=int(input("ENTER THE VALUE YOU WANT TO DELETE"))
if s in a:
    a.remove(s)
    print("ElEMENT REMOVED!")
else:
    print("ELEMENT NOT FOUND")
print(a)