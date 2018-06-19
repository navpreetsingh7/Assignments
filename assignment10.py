#A10_Q1
import threading
import time
class myThread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(2)
        print("abc",self.h)

thread1=myThread(1)
thread1.start()

#A10_Q2
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(2)
        print("value of",self.h)

for i in range(10):
    thread1=Mythread(i)
    thread1.start()
    thread1.join()
print("active threads are", threading.activeCount())


#A10_Q3
import threading
import time
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        n=2
        l=(1,2,3,4,5)
        for i in l:
            time.sleep(n)
            print("element is %d"%i)
            n=n+2
thread = mythread("")
thread.start()


#A10_Q4
import threading
import time
import math
class Fact(threading.Thread):
    def __init__ (self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(1)
        print("FACTORIAL IS %d"%math.factorial(self.h))
i=int(input("ENTER NO"))

fact=1
time.sleep(1)
thread1=Fact(i)
thread1.start()
thread1.join()

