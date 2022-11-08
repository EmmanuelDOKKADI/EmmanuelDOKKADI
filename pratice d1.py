##class student:
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##    def __Display(self):
##        print(self.name,self.age)
##    def show(self):
##        self.__Display()
##s1 = student("Abhi",20)
##s1.show()
##s2 = student("Ajay",20)
#s2.show()
class student:
    college = "AEC"
    #those are like varaiable
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def setdata(self,new):
        self.__name = new
    def getdata(self):
        print(self.__name,self.age)
s1=student("Anonymous",20)
s1.age=20
s1.setdata("Don")
s1.getdata()
s2=student("Hemanth",20)
    

