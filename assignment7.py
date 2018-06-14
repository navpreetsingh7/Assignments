#A7_Q1
print("It may be an integer. or a floating point number (to represent fractions of seconds).The Epoch is system-defined; on Unix, it is generally January 1st, 1970. The actual value can be retrieved by calling gmtime(0).The other representation is a tuple of 9 integers giving local time")


#A7_Q2
import time
print(time.asctime(time.localtime()))



#A7_Q3
import datetime
from datetime import date
c="2018-12-6"
d=datetime.datetime.strptime(c,"%Y-%d-%m")
print(d.month)

#Or

d=datetime.date.today()
print(d.month)

#A7_Q4
from datetime import date
import calendar
my_date =date.today()
print(calendar.day_name[my_date.weekday()])


#A7_Q5
a="11-01-2021"
d=d=datetime.datetime.strptime(a,"%d-%m-%Y")
print(d.day)

#A7_Q6
print(time.asctime(time.localtime()))
print("")

#A7_Q7
import math
num=int(input("enter num"))
print(math.factorial(num))

#A7_Q8
a=int(input("enter val1"))
b=int(input("enter val2"))
print(math.gcd(a,b))

#A7_Q9
import os
print(os.getcwd())
print(os.environ)