class Car:
    def __init__(self):
        self.__updatesoft()
    def drive (self):
        print ("driving")
    def __updatesoft(self):
        print ("updating")

red = Car()
red.drive()
#red.__updatesoft()
#red.__init__()