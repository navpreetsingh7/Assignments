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
#A,B

#A9_Q3
class Cop:
    def __init__(self,nm,age,we,des):
        self.nm=nm
        self.age=age
        self.we=we
        self.des=des

    def add(cls):
        cls.name = input("ENTER THE NAME=")
        cls.age = int(input("ENTER THE AGE="))
        cls.workexp = int(input("ENTER THE WORK EXPERIENCE="))
        cls.desg = input("ENTER THE DESIGNATION=")
        return Cop(cls.name, cls.age, cls.workexp, cls.desg)

    def display(self,nm,age,we,des):
        print("name of a cop=" +nm)
        print("age of a cop=" +age)
        print("work experience of a cop="+we)
        print("designation of a cop="+des)
    def update(self):
        print("for updation enter details")
        nm = input("enter name=")
        age = input("enter age=")
        we = input("enter work experience=")
        des = input("enter designation=")
        print("new name =" + nm)
        print("new age=" + age)
        print("new work experience=" + we)
        print("new designation=" +des)


class Mission(Cop):
    def __init__(self,missionname):
        self.missionname = missionname
    def add_mission_details(self,missionname):
        #self.missionname=missionname
        print("MISSION NAME-->"+missionname)



x=Cop('NAV','22','5','DC')
y=Mission('HELLO')
y.display('NAV','22','5','DC')
y.add()
y.update()
y.add_mission_details('kapurthala')



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
