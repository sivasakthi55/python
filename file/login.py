name="nandi"
total="345"
f=open("filetxt.txt","r")
info=f.read().split("\n")
for x in info:
    x=x.split("\t")
    if(x[0]==name and x[2]==total):
        print("login successfully")
        break
else:
        print("not")