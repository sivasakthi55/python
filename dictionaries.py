#dictionaries

dic={'name':'siva','age':22}
print(dic["age"])

dic['guide']=54
print(dic)

del dic['age']
print(dic)

print(list(dic))

print(sorted(dic))

print("gudio" in dic)     

print("guide" in dic)


a=dict([('bala',656),('siva',565),('aravinth',586)])
print(a)

print(type(a))
print(a["siva"])

dist={x:x**2 for  x in (5,4,7)}
print(dist)

a=dict(a=58,b=78,n=47)
print(a)




studentdetails={}
for x in range(3):
  studentdetails[str(input("enter a name:"))]=int(input("enter a age:"))
print(studentdetails)

del studentdetails['siva']
print(studentdetails)
















