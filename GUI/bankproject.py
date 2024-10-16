import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import Image
from PIL.ImageTk import PhotoImage


#home_page
r=Tk()
r.title("IOB BANK")
r.geometry("1500x800")
r.attributes('-fullscreen', True)

frame=Frame(r,bg="skyblue",width=1500,height=60)
frame.pack()

img=PhotoImage(Image.open("bank.jpg"))
label=Label(frame,image=img)
label.pack()
label.place(relx=0.35,rely=0.1)

label_font=font.Font(weight="bold",family="Courier New",size=30)
x=Label(frame,text="IOB BANK",font=label_font)
x.config(bg="skyblue",fg="white")
x.place(relx=0.4,rely=0.01)

label_font1=font.Font(weight="bold",family="Domine",size=20)
s="""A bank is a financial institution that accepts deposits from the public
and creates a demand deposit while simultaneously making loans."""
y=Label(r,text=s,font=label_font1)
y.place(relx=0.15,rely=0.12)

label_font2=font.Font(weight="bold",family="Times New Roman",size=15)
b=Button(r,text="Admin Login",font=label_font2,background="skyblue",command=lambda:admin_login(r))
b.place(relx=0.45,rely=0.25)

label_font3=font.Font(weight="bold",family="Domine",size=20)
a="""A person or entity that maintains an account and/or has business relationships with the bank.
One on whose behalf the account is maintained.
The beneficiary of the transaction carried professional intermediaries."""
y1=Label(r,text=a,font=label_font3)
y1.place(relx=0.08,rely=0.35)

label_font2=font.Font(weight="bold",family="Times New Roman",size=15)
b1=Button(r,text="Customer Login",font=label_font2,background="skyblue",command=lambda:customer_login(r))
b1.place(relx=0.18,rely=0.55)

label_font2=font.Font(weight="bold",family="Times New Roman",size=15)
b3=Button(r,text="customer Registration",font=label_font2,background="skyblue",command=lambda:customer_registration(r))
b3.place(relx=0.68,rely=0.55)

frame=Frame(r,bg="skyblue",width=1500,height=60)
frame.pack()
frame.place(relx=0,rely=0.9)


label_font=font.Font(weight="bold",family="Courier New",size=19)
x=Label(frame,text="Copyright © 2024 IOB",font=label_font)
x.config(bg="skyblue",fg="white")
x.place(relx=0.1,rely=0.15)

label_font=font.Font(weight="bold",family="Courier New",size=19)
x=Button(frame,text="service",font=label_font)
x.config(bg="skyblue")
x.place(relx=0.5,rely=0.1)



#Admin login
def admin_login(r):
    r.destroy()
    r=Tk()
    r.geometry("1500x800")
    r.attributes('-fullscreen', True)
    r.title("IOB BANK")
    frame=Frame(r,bg="skyblue",width=1500,height=60)
    frame.pack()

    img1=PhotoImage(Image.open("bank.jpg"))
    label=Label(frame,image=img1)
    label.pack()
    label.place(relx=0.35,rely=0.1)

    label_font=font.Font(weight="bold",family="Courier New",size=30)
    x=Label(frame,text="IOB BANK",font=label_font)
    x.config(bg="skyblue",fg="white")
    x.place(relx=0.4,rely=0.01)

    frame=Frame(r,height=350,width=400,bg="skyblue")
    frame.pack()
    frame.place(relx=0.33,rely=0.26)

    label_font=font.Font(weight="bold",family="Times New Romen",size=20)
    label=Label(frame,text="ADMIN LOGIN",font=label_font,bg="skyblue")
    label.place(relx=0.26,rely=0.06)

    frame1=Frame(frame,height=40,width=160,bg="pink")
    frame1.pack()
    frame1.place(relx=0.04,rely=0.25)

    label_font=font.Font(weight="bold",family="Times New Romen",size=15)
    label=Label(frame1,text="Admin Number:",font=label_font,bg="pink")
    label.place(relx=0.05,rely=0.08)



    frame2=Frame(frame,height=40,width=160,bg="pink")
    frame2.pack()
    frame2.place(relx=0.04,rely=0.45)

    label_font=font.Font(weight="bold",family="Times New Romen",size=17)
    label=Label(frame2,text="Password  :",font=label_font,bg="pink")
    label.place(relx=0.07,rely=0.08)

    e=Entry(frame)
    e.place(relx=0.5,rely=0.26,height=35,width=185)

    e=Entry(frame)
    e.place(relx=0.5,rely=0.46,height=35,width=185)

    label_font=font.Font(weight="bold",family="Times New Romen",size=17)
    button_adminlogin=Button(frame,text="login",font=label_font,bg="pink")
    button_adminlogin.place(relx=0.6,rely=0.69)
    r.mainloop()


def customer_login(r):
    
    r.destroy()
    r=Tk()
    r.geometry("1500x800")
    r.attributes('-fullscreen', True)
    r.title("IOB BANK")
    frame=Frame(r,bg="skyblue",width=1500,height=60)
    frame.pack()

    img=PhotoImage(Image.open("bank.jpg"))
    label=Label(frame,image=img)
    label.pack()
    label.place(relx=0.35,rely=0.1)

    label_font=font.Font(weight="bold",family="Courier New",size=30)
    x=Label(frame,text="IOB BANK",font=label_font)
    x.config(bg="skyblue",fg="white")
    x.place(relx=0.4,rely=0.01)

    frame=Frame(r,height=350,width=400,bg="pink")
    frame.pack()
    frame.place(relx=0.33,rely=0.26)

    label_font=font.Font(weight="bold",family="Times New Romen",size=20)
    label=Label(frame,text="CUSTOMER LOGIN",font=label_font,bg="pink")
    label.place(relx=0.2,rely=0.06)

    frame1=Frame(frame,height=40,width=160,bg="skyblue")
    frame1.pack()
    frame1.place(relx=0.04,rely=0.25)

    label_font=font.Font(weight="bold",family="Times New Romen",size=18)
    label=Label(frame1,text="User Name :",font=label_font,bg="skyblue")
    label.place(relx=0.05,rely=0.08)



    frame2=Frame(frame,height=40,width=160,bg="skyblue")
    frame2.pack()
    frame2.place(relx=0.04,rely=0.45)

    label_font=font.Font(weight="bold",family="Times New Romen",size=17)
    label=Label(frame2,text="Password  :",font=label_font,bg="skyblue")
    label.place(relx=0.07,rely=0.08)

    e=Entry(frame)
    e.place(relx=0.5,rely=0.26,height=35,width=185)

    e=Entry(frame)
    e.place(relx=0.5,rely=0.46,height=35,width=185)

    label_font=font.Font(weight="bold",family="Times New Romen",size=17)
    button_adminlogin=Button(frame,text="login",font=label_font,bg="skyblue")
    button_adminlogin.place(relx=0.6,rely=0.69)
    r.mainloop()


def customer_registration(r):
    
    r.destroy()
    r=Tk()
    r.geometry("1500x800")
    r.title("IOB BANK")
    frame=Frame(r,bg="skyblue",width=1500,height=60)
    frame.pack()
    r.attributes('-fullscreen', True)
    img1=PhotoImage(Image.open("bank.jpg"))
    label=Label(frame,image=img1)
    label.pack()
    label.place(relx=0.35,rely=0.1)

    label_font=font.Font(weight="bold",family="Courier New",size=30)
    x=Label(frame,text="IOB BANK",font=label_font)
    x.config(bg="skyblue",fg="white")
    x.place(relx=0.4,rely=0.01)

    frame=Frame(r,height=450,width=450,bg="skyblue")
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


r.mainloop()