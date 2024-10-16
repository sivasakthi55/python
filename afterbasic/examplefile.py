#open("filename.txt","x")
file=open("filename.txt","w")
file.write("siva\t22")

file=open("filename.txt","a")
file.write("\nsakthi\t23\nkumar\t25")
file=open("filename.txt","r")
info=file.read().split("\n")
print(info)
for data in info:
    d=data.split("\t")
    print("name :"+d[0])
    print("age  :"+d[1])
    print("----------")


