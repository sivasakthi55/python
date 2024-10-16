#maping and filtering

data=[1,2,3,4,5]

result1=map(lambda x:x*2,data)
print(list(result1))

result=map(lambda x:x/2,data)
print(list(result))

result2=filter(lambda x:x%2==0,data)
print(list(result2))





