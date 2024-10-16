#set

basket={"apple","banana","orange","kiwi","apple"}

print(basket)
print(type(basket))

print("orange" in basket)
print("mango" not in basket)

a={"apple","banana","kiwi"}
b={"apple","banana","orange"}

print(a)

print("letter in a but not in b",b-a,a-b)

print("both a or b",a|b)
      
print("letter in both a and b",a&b)

print("letter in a or b but not both",a^b)

#set checking

a={x for x in 'weajdc' if x in 'abc'}
print(a)

a.update([1,256,3],{13,3})
print(a)

a.discard(256)
print(a)

a.remove(3)
print(a)


x={"a","b","c"}
y={"f","a","m","b","c"}

z=x.issubset(y)
print(z)


x={"f","a","m","b","c"}
y={"a","b","c"}

z=x.issuperset(y)
print(z)

z=x.isdisjoint(y)
print(z)

