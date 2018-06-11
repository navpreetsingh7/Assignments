#A4_Q1
a=int(input("enter a year"))
if (a%4==0):
    print("year is leap")
else:
    print("year is not a leap year")

#A4_Q2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("square")
else:
    print("rectangle")


#A4_Q3


a1=int(input("enter first age"))
a2=int(input("enter second age"))
a3=int(input("enter third age"))

if( a1>a2 and a1>a3):
    print("a1 is oldest")

if(a2>a1 and a2>a3):
    print("a2 is oldest")
if(a3>a1 and a3>a2):
    print("a3 is oldest")

elif(a1<a2 and a1<a3):
    print("a1 is youngest")

elif(a2<a1 and a2<a3):
    print("a2 is youngest")

elif(a3<a1 and a3<a2):
    print("a3 is youngest")
else:
    print("all ages are same")





#A4_A4
s=int(input("enter the POINTS"))
if s<200:
    if s>1 and s<50:
        print("NO PRIZE")
    if s>51 and s<150:
        print("WOODEN DOG")

    if s>151 and s<180:
        print("BOOK")

    if s>181 and s<200:
        print("CHOCLATES")

else:
    print("WRONG INPUT")


#A4_Q5
q=int(input("enter quantity"))
if(int(q*100>1000)):
   m= q*100-0.10*q*100
   print(m)

else:
    n=q*100
    print(n)



