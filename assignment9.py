#A9_Q1
class Animal:
    def animal_attribute(self):
        print("IT has 4 legs")

class Tiger(Animal):
    def properties(self):
        print("IT has a tail")


y=Tiger()
y.properties()
y.animal_attribute()

#A9_Q2
#OUTPUT-A,B

#A9_Q3
class Cop:
    def __init__(self, name, age, workexp, desg):
        self.name = name
        self.age = age
        self.workexp = workexp
        self.desg = desg

    @classmethod
    def add(cls):
        cls.name = input("ENTER THE NAME")
        cls.age = int(input("ENTER THE AGE"))
        cls.workexp = int(input("ENTER THE WORK EXPERIENCE"))
        cls.desg = input("ENTER THE DESIGNATION")
        return Cop(cls.name, cls.age, cls.workexp, cls.desg)

    @classmethod
    def display(cls):
        print("")
        print("DETAILS ARE-->")
        print("NAME-> " + cls.name)
        print("AGE-> %d" % cls.age)
        print("WORK EXPERIENCE--> %d" % cls.workexp)
        print("DESIGNATION-->" + cls.desg)

    def update(self):
        print("UPDATE DETAILS-->")
        self.add()
        self.display()


class Mission(Cop):
    def __init__(self, mission_details):
        self.md =mission_details
    def add_mission_details(self):
        self.md=input("ENTER MISSION DETAILS--> ")
        print("")
        self.display()
        print("MISSION DETAILS-->"+self.md)

x = Mission("")
obj1 = Cop("",0,0,"")
obj1.add()
obj1.display()
ch = input("DO YOU WANT TO UPDATE THE DETAILS?(Y/N)")
if ch == 'y' or ch == 'Y':
    obj1.update()
ch = input("DO YOU WANT TO RUN MISSION CLASS?(Y/N)")
if ch == 'y' or ch == 'Y':
    x.add_mission_details()

#A9_Q4
class Shape:
    def __init(self,len,bre):
            self.len=len
            self.bre=bre
class Rectangle(Shape):
    def area(self,len,bre):
        return len*bre

class Square(Shape):
    def area(self,len):
        return len*len
obj=Shape()
obj1=Rectangle()
obj2=Square()
len=int(input("enter length"))
bre=int(input("enter breadth"))
print("area of a rectangle",(obj1.area(len,bre)))
print("area of square",(obj2.area(len)))
