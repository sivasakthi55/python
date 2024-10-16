import tkinter 
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

win=Tk()
win.geometry("500x500")

frame=Frame(win,width=100,height=100)
frame.pack()
frame.place(relx=0.2,rely=0.38)

img=ImageTk.PhotoImage(Image.open("kitkat.jpg"))
label=Button(frame,image=img,activebackground="skyblue")
label.pack()


a=Label(win,text="first name:")
a.place(relx=0,rely=0.00)

b=Label(win,text="last name:")
b.place(relx=0,rely=0.05)

c=Label(win,text="email id:")
c.place(relx=0,rely=0.10)

d=Label(win,text="contact no:")
d.place(relx=0,rely=0.15)

a1=Entry(win)
a1.place(relx=0.15,rely=0)

b1=Entry(win)
b1.place(relx=0.15,rely=0.05)

c1=Entry(win)
c1.place(relx=0.15,rely=0.10)

d1=Entry(win)
d1.place(relx=0.15,rely=0.15)

r=Label(win,text="gender :")
r.place(relx=0.5,rely=0)

var=IntVar()
r1=Radiobutton(win,text="male",variable=var,value=1)
r1.place(relx=0.6,rely=0)


r2=Radiobutton(win,text="female",variable=var,value=2)
r2.place(relx=0.7,rely=0)

combo1=Label(win,text="country :")
combo1.place(relx=0.5,rely=0.05)

combo=ttk.Combobox(win,values=["india","america","england"])
combo.place(relx=0.61,rely=0.05)

m=Label(win,text="message:")
m.place(relx=0.5,rely=0.1)

text=Text(win,height=3,width=20)
text.place(relx=0.61,rely=0.1)

button=Button(win,text="Done",command=lambda:done(a1.get()))
button.place(relx=0.8,rely=0.25)

def done(name):
    messagebox.showwarning("Excellent work",name)

win.mainloop()


