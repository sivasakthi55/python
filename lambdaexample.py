#lambda example

num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))

add=lambda num1,num2:num1+num2
print(add(num1,num2))

sub=lambda a,b:a-b
print(sub(num1,num2))

multiply=lambda a,b:a*b
print(multiply(num1,num2))

div=lambda a,b:a/b
print(div(num1,num2))


data=[2,4,5,7]
data1=[2,2,2,2]

result=map(lambda x,y: x+y, data, data1)
print(list(result))


result1=filter(lambda x: x+x==5, data)
print(list(result1))










