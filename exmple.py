c=0
a=b=12
while(a>0):
    r=a%10
    c=c+(r*r*r)
   
    a//=10
print(c)
