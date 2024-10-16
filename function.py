'''
#basic function
 
def my_function():
   print("hello from function")
   print("yes this is function")
my_function()
'''
#function passing parameters

def my_function(fname):
   print(fname,"welcome")
my_function("siva")
my_function("harish")

'''
#two parameter passing

def harry(fname,lname):
  print(fname+lname)
a=input("enter the a:")
b=input("enter the b:")
harry(a,b)

def my_function(child3,child2,child1):
  print("the youngest child is "+child1)
my_function(child1="emil",child2="tobias",child3="linus")
my_function("java","python","c++")


#keywords arguments

def my_function(**kids):
  print("his last name is ",kids["fname"],kids["lname"])
my_function(fname="tobias",lname="resfsnes")


def my_function(*kids):
  print("the youngest child is ",kids[1])
my_function("email","tobias","linus")


def my_function(country="norway"):
   print(" i am from "+country)
my_function()
my_function("india")
my_function("brazil")

'''
