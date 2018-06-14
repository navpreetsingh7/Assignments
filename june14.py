import time
print(time.gmtime())
print(time.time())
print(time.gmtime(300000000))
print(time.asctime())
print(time.asctime(time.gmtime()))
print(time.ctime(15000))
print(time.asctime(time.localtime()))


import datetime
from datetime import date
print(datetime.MINYEAR)
print(date.today())
print(date.fromtimestamp(12121212354))



import os
print(os.name)
print(os.environ)
