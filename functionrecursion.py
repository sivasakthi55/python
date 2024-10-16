#function recursion

def factorial(x):
  if x==1:
      return 1
  else:
     return(x*factorial(x-1))     
num=int(input("enter a num :"))
print("the factorial of",num,"is",factorial(num))

'''
def factorial(x):
     while(x==1):
         return 1
     else:
        return(x*factorial(x-1))
num=4
print("the factorial of",num,"is",factorial(num))

'''
'''
# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))
'''