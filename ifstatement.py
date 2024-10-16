#if statement
'''
a=70
b=65
c=4
 
#sample if

if(a>b):
    print("a is greater than b")
    print("sss")
    print("ssss")
    a=150
print("a values is: ",a,"\nb values is :",b)

#if else

if(a>b):
   print("a is greater than b")
else:
   print(" b is greater than a")
print(" a values is : ",a,"\nb values is : ",b)


name=input("your name :")
age=int(input("your age : "))
place=str(input("your place :")) 

print("name :",name)
print("age :",age)
print("place:",place)

if(age>=18 and place=="melaiyur"):
   print("your eligible to vote")
else:
   print("you not eligible to vote") 
'''
#else if ladder
a=55
b=222
c=111

if(a>b):
  print("a is greater than b")
elif(c>a):
  print("c is greater than a")
else:
  print("b is lower than a")
print("a value is :",a,"\nb value is :",b)
'''
#nested if
 
if(b>a):
  print("b is greater than a")
  if(c>a):
     print("c is also greater than a")
  else:
     print("!! a is greater than c")
else:
  print("a is greater than b")


name=input("your name:")
age=int(input("your age:"))
place=str(input("your place:"))

print("name :",name)
print("age :",age)
print("place:",place)

if(age>=18):
     print("your age is eligible to vote")
     if(place=="melaiyur"):
        print("your place is eligible to vote")
     else:
        print("your place is  not eligible to vote")
else:
    print("your age is  not eligible to vote")



 '''
