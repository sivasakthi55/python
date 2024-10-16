name=input("your name:")
age=int(input("your age:"))
email=input("email id:")

if(age>=18):
   tamil_mark=int(input("enter a tamil mark:"))
   english_mark=int(input("enter a english mark:"))
   maths_mark=int(input("enter a maths mark:"))
   physics_mark=int(input("enter a physics mark:"))
   chemistry_mark=int(input("enter a chemistry mark:"))
   Biology_mark=int(input("enter a biology mark:"))

   print("name :",name)
   print("age :",age)
   print("email id :",email)


   print("tamil : ",tamil_mark)
   print("english : ",english_mark)
   print("maths : ",maths_mark)
   print("physics : ",physics_mark)
   print("chemistry : ",chemistry_mark)
   print("biology : ",Biology_mark)

   total_mark=tamil_mark+english_mark+maths_mark+physics_mark+chemistry_mark+Biology_mark

   print("total_mark=",total_mark)

   average=total_mark/600*100
   print("average=",average)


   if(average>=90):
      print("you eligible medical college")
   elif(average>=80):
      print("you eligible engineering college")
   elif(average>=35): 
     print("you eligible arts and science college")
   else:
    print("you not eligible college")
else:
  print("your age not eligiblle ")


open("student_details.txt")
file=open("student_details.txt","a")
file.write("\n"+"\n"+"name:  "+name)
file.write("\n")
file.write("age:   "+str(age))
file.write("\n")
file.write("email: "+email)
file.write("\n")
file.write("tamil: "+str(tamil_mark))
file.write("\n")
file.write("english: "+str(english_mark))
file.write("\n")
file.write("maths: "+str(maths_mark))
file.write("\n")
file.write("physics:"+str(physics_mark))
file.write("\n")
file.write("chemistry: "+str(chemistry_mark))
file.write("\n")
file.write("biology: "+str(Biology_mark))
file.write("\n")
file.write("total: "+str(total_mark))
file.write("\n")
file.write("average: "+str(average))




