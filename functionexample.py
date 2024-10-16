#function

def add_function(num1,num2):
   print("add a and b :",num1+num2)
def sub_function(num1,num2):
   print("sub a and b :",num1-num2)
def multi_function(num1,num2):
   print("multiple a and b:",num1*num2)
def div_function(num1,num2):
   print("div a and b :",num1/num2)
def function(a):
          c=0
          a=a
          while(a>0):
               r=a%10
               c=(c*10)+r
               a//=10
          print(c)


def adam_function(num):
       c=0
       a=b=num
       while(a>0):
          r=a%10
          c=(c*10)+r
          a//=10
          d=c*c
       print(d)
       c=0
       a=b*b
       while(a>0):
          r=a%10
          c=(c*10)+r
          a//=10
       print(c)




a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))
d=int(input("enter the d:"))

while(d==0):
   if(c==1):
    add_function(a,b)
   elif(c==2):
    sub_function(a,b)
   elif(c==3):
    multi_function(a,b) 
   elif(c==4):
     div_function(a,b)
   elif(c==5):
      function(a)
   elif(c==6):
      adam_function(a)
   else:
     print("c is not calculator function")

   d=int(input("enter the d:"))



pyinstaller --clean --onefile --windowed --icon=bd.ico birthdaywishes.py
