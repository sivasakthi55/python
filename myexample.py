a="personal information"
print(a.center(60,' '))
details=input('enter your name: ')
print('Name : ',details)
num=int(input('enter your age: '))
print("Age : ",num)

print(type(num))
print(type(details))
print("siva" in details)

statement="i'm {0} and age {1}"
print(statement.format(details,num))