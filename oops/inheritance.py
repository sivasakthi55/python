"""class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname)
        print(self.lastname)
class student(person):
    pass
x=student("mike","olren")
x.printname()
"""
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname)
        print(self.lastname)

class student(person):
    def __init__(self,fname,lname):
        super(). __init__(fname,lname)
        person.__init__(self,fname,lname)
        self.gradutionyear=2022
x=student("mike","olren")
print(x.gradutionyear)
x.printname()


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname)
        print(self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        super(). __init__(fname,lname)
        person.__init__(self,fname,lname)
        self.gradutionyear=year
x=student("mike","olren",2023)
print(x.gradutionyear)
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class College(Person):
  def __init__(self, fname, lname, college):
     super().__init__(fname, lname)
     self.college = college
  def printn(self):
    print(self.firstname,self.lastname,self.college)
  
class Student(College):
  def __init__(self,fname,lname,class1,degree):
    super().__init__(fname,lname,class1)
    self.Degree=degree

mani=Student("prem","kumar","a.v.c","bca")
mani.printname()
mani.printn()
print(mani.Degree)

"""class base1:
    def __init__(self):
        self.str1="a"
        print("base1")

class base2:
    def __init__(self):
        self.str2="b"
        print("base2")

class derived(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("dervied")
    def printstrs(self):
        print(self.str1,self.str2)
        
ob=derived()
ob.printstrs()
"""
