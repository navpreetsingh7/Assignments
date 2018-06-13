#function's lecture
def hello():
    print("hey")
hello()

def add(a,b):
    return a+b
print(add(2,3))


def add(a,b):
    return a+b
print(add(b=2,a=3))

def add(a,b=4):
    return a+b
print(add(3))

a=2
def add(a):
    a=3
    print(a)
add(a)



a=int(input("enter the val of a"))
b=int(input("enter the val of b"))
def add(a,b=5):
    return a+b
print(add(a,b))

def sub(a,b):
    return a-b
print(sub(a,b))



