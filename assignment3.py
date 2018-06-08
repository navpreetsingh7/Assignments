#A3_Q1

t=('abc','hello',1,2,3)

print(t)
l=len (t)
print(l)

#A3_Q2
c=(1,2,3,4)
print(max(c))
print(min(c))

#A3_Q3
t1=(3*4*5)
print(t1)


#SETS
#A3_Q1
t2= input("enter val 1")
t3= input("enter val 2")
y2=input("enter val 1")
y3=input("enter val 2")
y4=input("enter val 3")

set1= set([t2,t3])
set2=set([y2,y3,y4])

ans1=[set1<=set2]
ans2=[set2<=set1]
print(ans1)
print(ans2)

ans3=set1&set2
print(ans3)

ans4=set1|set2
print(ans4)

ans5=set1-set2
print(ans5)

#dictionary
#A3_Q1
name=input("enter name")
marks=input("enter marks")
d={'name':name,
   'marks':marks}
print(d)
#A3_Q3
l="mississippi"
m=l.count("m")
i=l.count("i")
s=l.count("s")
p=l.count("p")


d={'no of m:':m,
   'no of i':i,
   'no of s':s,
   'no of p':p}
print(d)

