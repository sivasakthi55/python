print("-----------Student details------------")
name=input("Enter the name : ")
age=int(input("Enter your age : "))
total=int(input("Enter your Total Mark : "))

if(age>18):
    f=open("filetxt.txt",'a')
    f.write("\n"+name+"\t"+str(age)+"\t"+str(total))