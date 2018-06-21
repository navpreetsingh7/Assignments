try:
    a=int(input("enter no:"))
    print(a)
    b=10/a

except ValueError:
    print("enter only integer")
except ZeroDivisionError:
    print("number divided by zero")
else:
    print(b)
#or
#except (ValueError,ZeroDivisionError):
finally:
    print("i will execute whether exception occurs or not")
######
try:
    a = [1,2,3]
    print(a[4])

except IndexError:
    print("limit exceed")


try:
    import abcff
    print("nnn")
except ImportError:
    print("abd")

####
class NumError(Exception):
    pass
try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a+b
    if c<10:
        raise NumError
except NumError:
    print("num is less than 10")
else:
    print(c)

