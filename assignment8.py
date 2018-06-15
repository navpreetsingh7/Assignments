#A8_Q1
class Circle:

    def getArea(self,radius):
        area=3.14*radius*radius
        print("Area = %d"%(area))
    def getCircumference(self,radius):
        circumference=3.14*2*radius
        print("Circumference = %d"%(circumference))
radius=int(input("enter the radius"))
a=Circle()
a.getArea(radius)
a.getCircumference(radius)


#A8_Q2
name=input("enter name")
rn=int(input("enter roll no."))
class Student:
    def Display(self,name,rn):
        print(name)
        print(rn)
x=Student()
x.Display(name,rn)

#A8_Q3
cel=float(input("enter celsius"))
fahren=float(input("enter fahrenheit"))
class Temperature:
    def convertFahrenheit(self,cel):
        fah =(9 / 5) * cel + 32
        print("temperature in fahrenheit %.4f" % (fah))
    def convertCelsius(self,fahren):
        cel = (5 / 9) * (fahren - 32)
        print("temp in celsius %.4f" %(cel))
x=Temperature()
x.convertFahrenheit(cel)
x.convertCelsius(fahren)


#A8_Q4
mn=input("enter movie name")
an=input("enter artist name")
yr=input("enter year of release")
rat=input("enter ratings")

class MovieDetails:
         def displaydetails(self, mn, an, yr, rat):
            print("movie name" + mn)
            print("artist name" + an)
            print("year of release" + yr)
            print("ratings " +rat)


         def updatedetails(self, mn, an, yr, rat):
             mn = input("enter movie name")
             an = input("enter artist name")
             yr = input("enter year of release")
             rat = int(input("enter ratings"))

             print("new movie name " + mn)
             print("new artist name" + an)
             print("new year of release" + yr)
             print("new ratings %d" % (rat))

x=MovieDetails()
x.displaydetails(mn,an,yr,rat)
x.updatedetails(mn,an,yr,rat)

#A8_Q5
exp = int(input("Enter expenditure"))
saving = int(input("Enter savings"))
class Expenditure:
    def displayresult(self,exp,saving):
        print("Expenditure %d" % (exp))
        print("Savings %d" % (saving))
    def calculateresult(self,exp,saving):
        salary = exp + saving
        return salary
    def displaysalary(self,sal):
        print("salary is %d" %(sal))
x = Expenditure()
x.displayresult(exp,saving)
x.calculateresult(exp,saving)
sal=x.calculateresult(exp,saving)
x.displaysalary(sal)

