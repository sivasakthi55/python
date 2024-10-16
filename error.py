#Error

try:

  print(x)

except:
   print("an error occurred")

    
try:
  print(C)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
    
        
        
try:
    x=4
    print(x)
except:
    print("something went worng")
else:
    print("nothing went worng")



try:
    x=4
    print(x)
except:
    print("something went worng")
finally:
    print("the 'try except' is finished")



#raise Exception("ldgyu")

a="hello"
#assert a=="bala"
assert a=="hello"





