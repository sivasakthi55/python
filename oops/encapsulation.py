"""class student:
    def __init__(self,name,rank,points):
        self.name=name
    def gettername(self):
        print(self.name)
    def settername(self,name):
        self.name=name

st1=student("steve","first",100)
st1.gettername()
st1.settername("siva")
st1.gettername()"""

class employee:
    def __init__(self,name,id,salary,project):
        self.name=name
        self.id=id
        self.salary=salary
        self.project=project
    def show_sal(self):
        print("name: ",self.name,"salary: ",self.salary)
    def proj(self):
        print(self.name,"is working on ",self.project)

emp=employee("siva",112,15000,"python")
emp.show_sal()
emp.proj()
