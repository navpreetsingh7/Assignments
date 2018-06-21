#A12_Q1
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("num cannot be divided by zero")
#A12_Q2
try:
    a = [1,2,3]
    print(a[4])

except IndexError:
    print("limit exceed")


#A12_Q3
#output:"AN EXCEPTION"

#A12_Q4
#OUTPUT:-5
#"a/b resut in 0"

#A12_Q5
try:
    import abcff
    print("nnn")
except ImportError:
    print("import error")

try:
    a=int(input("enter no:"))
    print(a)
    b=10/a
    print(b)
except ValueError:
    print("enter only integer")

try:
    a = [1,2,3]
    print(a[4])

except IndexError:
    print("limit exceed")
#A12_Q6
class AgeTooSmallError(Exception):
    pass
try:
    age=int(input("enter age"))
    print(age)
    if age<18:
        raise AgeTooSmallError
except AgeTooSmallError:
    print("age is too small")
