'''class c1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("this is function")
    def func1(self):
        print(self.name,self.age)
c=c1("kumar",32)
c.func1()
print(c.name)
'''
'''class c2:
    name="prasath"
    def func1(self):
        print(self)
obj=c2()
print(obj.name)
print(obj)
obj.func1()'''

class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print("salary is increase in monthly")
    def read(self):
        print(self.name,self.age,self.salary)
    def __str__(self):
        return str(self.salary) 
obj=employee("viswa",21,10000)
obj.read()
print(obj)




