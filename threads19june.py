#import threading
#import time
#class Mythread(threading.Thread):
    #def __init__(self,i):
        #threading.Thread.__init__(self)
        #self.h=i
    #def run(self):
        #time.sleep(5)
        #print("value of",self.h)
#thread1 = Mythread(2)
#thread1.start()
#thread2 = Mythread(2)
#thread2.start()
####

import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(1)
        print("value of", self.h)

for i in range(10):
    thread1=    Mythread(i)
    thread1.start()
    thread1.join()

print("active threads are",threading.activeCount())



import threading
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):

        print("im in a run",self.h)

thread1=Mythread("from thread1")
thread1.start()
thread1.join()
thread2=Mythread("from thread2")
thread2.start()
thread2.join()
print("goodbye")
