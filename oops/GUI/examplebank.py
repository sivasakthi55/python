import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import Image
from PIL.ImageTk import PhotoImage
r=Tk()
r.geometry("1500x800")
r.title("IOB BANK")
frame=Frame(r,bg="skyblue",width=1500,height=60)
frame.pack()

img1=PhotoImage(Image.open("bank.jpg"))
label=Label(frame,image=img1,bg="skyblue")
label.pack()
label.place(relx=0.35,rely=0.1)

label_font=font.Font(weight="bold",family="Courier New",size=30)
x=Label(frame,text="IOB BANK",font=label_font)
x.config(bg="skyblue",fg="white")
x.place(relx=0.4,rely=0.01)

frame=Frame(r,height=450,width=450,bg="orange")
frame.pack()
frame.place(relx=0.33,rely=0.19)

label_font=font.Font(weight="bold",family="Times New Romen",size=20)
label=Label(frame,text="CUSTOMER REGISTRATION",font=label_font,bg="skyblue")
label.place(relx=0.1,rely=0.04)

frame1=Frame(frame,height=40,width=160,bg="pink")
frame1.pack()
frame1.place(relx=0.04,rely=0.18)

label_font=font.Font(weight="bold",family="Times New Romen",size=16)
label=Label(frame1,text="Name  \t  :",font=label_font,bg="pink")
label.place(relx=0.1,rely=0.09)



frame2=Frame(frame,height=40,width=160,bg="pink")
frame2.pack()
frame2.place(relx=0.04,rely=0.32)

label_font=font.Font(weight="bold",family="Times New Romen",size=17)
label=Label(frame2,text="Phone No  :",font=label_font,bg="pink")
label.place(relx=0.07,rely=0.08)

frame2=Frame(frame,height=40,width=160,bg="pink")
frame2.pack()
frame2.place(relx=0.04,rely=0.48)

label_font=font.Font(weight="bold",family="Times New Romen",size=17)
label=Label(frame2,text="Email id\t   :",font=label_font,bg="pink")
label.place(relx=0.07,rely=0.08)

frame2=Frame(frame,height=40,width=160,bg="pink")
frame2.pack()
frame2.place(relx=0.04,rely=0.63)

label_font=font.Font(weight="bold",family="Times New Romen",size=17)
label=Label(frame2,text="Place\t   :",font=label_font,bg="pink")
label.place(relx=0.07,rely=0.08)

e1=Entry(frame)
e1.place(relx=0.5,rely=0.19,height=35,width=200) 

e2=Entry(frame)
e2.place(relx=0.5,rely=0.33,height=35,width=200)

e3=Entry(frame)
e3.place(relx=0.5,rely=0.49,height=35,width=200)

e4=Entry(frame)
e4.place(relx=0.5,rely=0.63,height=35,width=200)

label_font=font.Font(weight="bold",family="Times New Romen",size=17)
button_adminlogin=Button(frame,text="Register",font=label_font,bg="pink")
button_adminlogin.place(relx=0.6,rely=0.79)
r.mainloop()
