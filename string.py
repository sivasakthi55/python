#string

print("hello")
print('hello')

#assign string to variable

a="hello"
print(a)

#multiline string

a="""siva,
kumar,
prasath"""
print(a)

#string are arrays

a="hello,world!"
print(a[1])
print(a[0])

#length function

a="hello,world!"
print(len(a))

#check function

txt="i am siva"
print("siva" in txt) 

#slicing string

b="hello,siva"
print(b[2:])
print(b[1:6])
print(b[:3])
print(b[-5:-2])
print(b[::-1])

#modify the string

print(a.upper())
print(a.lower())
a="    hello,siva   "
print(a)
print(a.strip())

#replace string

print(a.replace("h","j"))

c="sivasakthi"
print(c[4:6].upper())
print(c[:3].lower()+c[3:6].upper()+c[6:].lower())




