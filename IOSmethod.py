class IOSstring:
    def __init__(self):
        self.str1=""

    def setstring(self):
        self.str1=input("enter string:")

    def printstring(self):
        print  ("result is:",self.str1.upper())
str1= IOSstring()

str1.setstring()
str1.printstring()




