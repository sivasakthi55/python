'''
#simple for

for x in range(30):
   print("we're on time",x)

#for and break 

for x in range(30):
  if x==4:
     break
  print(x)

#for else

for x in range(7):
  print(x)
else:
  print("loop ended")

#for using string

string="hello world"
for x in string:
  print(x)

#collections in for loop

collections=['hey',5,'d']
for x in collections:
  print(x)

#nested loops

adj=["red","big","tasty"]
fruits=["apple","banana","cherry",]
for x in adj:
  for y in fruits:
      print(x,y)

#list in for loop
 
list=[[1,2,3],[4,5,6],[7,8,9]]
for y in list:
  print(y)
  for x in y:
    print(x)

#continues statement

fruits=["apple","banana","cherry"]
for x in fruits:
   if x=="apple":
       continue
   print(x)

#increase value 3

for x in range(1,30,3):         
  print(x)

#pass statement

for x in range(7):
  pass


name=input("your name:")
age=int(input("your age:"))
course=input("your course:")
 
print("name :",name)
print("age :",age)
print("course :",course)


mca_subject=["python","java","maths","html"]
bca_subject=["c","c++","java","css","html"]

if(course=="mca"):
   for x in mca_subject:
      print(x)
   else:
      print('this is mca subject')

if(course=="bca"):
   for x in bca_subject:
      print(x)
   else:
       print('this is  bca subject')
'''















