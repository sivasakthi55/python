#string concatenation
a="hello"
b="world"
c="cup"
d=a+b+c
print(d)
 
age=36
txt="my name is john,and i am {}"
print(txt.format(age))

quantity=3
itemno=587
price=25.23
myorder="i want {} pieces of item {} for {} dollars"
print(myorder)
print(myorder.format(quantity,itemno,price)) 

myorder="i want to pay {2} dollars for {0} \"pieces\" of item {1}"
print(myorder.format(quantity,itemno,price)) 
 
a="hello,world"
print(a.split("o"))



sample_string="Hello,world!"
print(sample_string.capitalize())
print(sample_string.casefold())

print(sample_string.center(50,'-'))

print(sample_string.count('l'))

print(sample_string.encode(encoding='utf-8'))
print(sample_string.endswith('!'))
print("hello\tworld\t!".expandtabs(5))

sample_string="helloworld"
print(sample_string.find('world'))

values={"name":'bob','age':22}
print("myname is {name},i'm {age}years old".format_map(values))


print(sample_string.isalpha())
print(sample_string.index('world'))
print(sample_string.isalnum())
print(sample_string.isascii())
print(sample_string.isdecimal())
print(sample_string.isdigit())
print(sample_string.isidentifier())
print(sample_string.islower())
print(sample_string.isnumeric())
print(sample_string.isprintable())
print(sample_string.isspace())
print(sample_string.istitle())
print(sample_string.isupper())



iterable=['apple','banana','cherry']
print("/".join(iterable))

print(sample_string.ljust(20,'-'))

print(sample_string.lower())
 
a="siva,sakthi,kumar"
print(a.partition(','))
print(a.split('k'))

multiline_string="hello\nworld\n!"
print(multiline_string.splitlines())