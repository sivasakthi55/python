
name=input("enter a name: ")
employee_id=input("enter a id: ")
password=input("enter a password: ")
email=input("enter a email: ")


file=open("s.txt","a")

file.write(name+"\t"+employee_id+"\t"+password+"\t"+email)

file=open("s.txt","r")
data=file.read().split("\t")
print(data)



id=input("enter a id:")
password1=input("enter a password:")

if(id==data[1]):
    if(password1==data[2]):
        print("login successfilly")
    else:
        print("incorrect password")
else:
    print("employee_id not match")        
    



