def admin_login():
    admin_id=input("enter a admin_id:")
    password=input("enter a password:")
    if(admin_id=="siva123"):
        if(password=="123"):
            print("login successfully")
            file=open("admin.txt","r")
            info=file.read()
            print(info)
        else:
            print("incorrect password")

def customer_login():
    user_name=input("enter a user_name:")
    password1=input("enter a password:")
    if(user_name=="sivasakthi"):
        if(password1=="111"):
            print("login successfully")
            file=open("customer_login.txt","r")
            data=file.read()
            print(data)
        else:
            print("incorrect password")    

def  customer_registation():
    name=input("enter a name:")
    phone_no=input("enter a phone_no:")
    
    file=open("info.txt","r")
    data1=file.read().split("\n")
    a=data1[len(data1)-1].split()[0]
    print(a)
    account_no=int(a)+1
    file=open("info.txt","a")
    file.write("\n"+str(account_no)+"\t"+name+"\t"+phone_no)
    f=open("admin.txt","a")
    f.write("\n"+"\n"+"name:"+name+"\n"+"phone_no:"+str(phone_no)+"\n"+"account_no:"+str(account_no))
    print("registation successfully")


print("1.admin login")
print("2.customer login")
print("3.customer registation")

x=int(input("enter a your choices:"))

if(x==1):
    admin_login()
elif(x==2):
   customer_login()
elif(x==3):
  customer_registation()
        
     





