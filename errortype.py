#Syntax error
'''
x=10
if x==10
print(x)
'''


#Runtime error


#Name Error
#print(x)



#Type Error
x="100"
y=5
#z=y+x
 
#index Error
x=['raja','annamalai','balaji']
#print(x[3])


#Attribute Error
x="Nandhini"
#x.reverse()
             


#Logical Error
def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
print(fact(5))

try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("The result is:", y)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")



#Assertion, attribute,floating poing,import, index,memory ,name,overflow,typeerror






