#list
'''
fruits=['orange','apple','pear']
fruits1=['banana','kiwi','apple','banana']

print(fruits)
print(type(fruits))

fruits.append("apple")
print(fruits)

fruits.extend(fruits1)
print(fruits)

fruits.insert(3,"mango")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.pop()
print(fruits)


print(fruits.index("mango",1))


print(fruits.count("apple"))


fruits.sort()
print(fruits)


fruits.reverse()
print(fruits)

fruits2=fruits.copy()
print("copied list:",fruits2)

fruits2.clear()
print(fruits2)

a=[4,6,4,6]
b=a
b.append(2)
print(a)
print(b)


a=[4,6,4,6]
b=a.copy()
b.append(2)
print(a)
print(b)

'''
'''
name=[str(input("enter a name:"))]
print(name)
i=0
while(i<3):
 name.append(str(input("enter a name:")))
 i+=1
print("name",name)

course=[str(input("enter a course :"))]
print(course)
i=0
while(i<3):
 course.append(str(input("enter a course:")))
 i+=1
print("course",course)

age=[int(input("enter a age:"))]
i=0
while(i<3):
 age.append(int(input("enter a age:")))
 i+=1

print("age",age)

name.append("viswa")
age.append(27)
course.append("bca")

print(name)
print(age)
print(course)

'''
studentdetails=[]

for i in range(3):
  studentdetails.append(str(input("enter a name:")))
  studentdetails.append(int(input("enter aage:")))
  studentdetails.append(str(input("enter a course:")))

print(studentdetails)

