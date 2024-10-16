"""import tkinter
root=tkinter.Tk()
root.mainloop()"""

"""from tkinter import *
root=Tk()
frame=Frame(root,bg="red",width=400,height=400)
frame.pack()
root.mainloop()
"""

"""import tkinter
from tkinter import messagebox

def helloCallBack():
    tkinter.messagebox.showwarning( "show error","mistake")

top=tkinter.Tk()
b= tkinter.Button(top,text="new",command=lambda:helloCallBack())
b.pack()
top.mainloop()"""

"""
import tkinter 
t=tkinter.Tk()
frame=tkinter.Frame(t,bg="skyblue", width=400, height=500)
b=tkinter.Button(t,text="new",activebackground="green")
b.pack()
frame.pack()
t.mainloop()
"""
"""
from tkinter import*
root=Tk()
for fm in["blue","red","white","black"]:
    Frame(height=20,width=500,bg=fm).pack()
root.mainloop()"""

"""import tkinter
from tkinter import*
import tkinter.messagebox
r=Tk()
r.geometry("400x400")
l1=Label(r,text="enter the first value")
l1.grid(row=0,column=1)
l2=Label(r,text="enter the second value")
l2.grid(row=1,column=1)
l3=Label(r,text="result")
l3.grid(row=2,column=1)
e1=Entry()
e1.grid(row=0,column=2)
e2=Entry()
e2.grid(row=1,column=2)
e3=Entry()
e3.grid(row=2,column=2)

def callback(c):
    tkinter.messagebox.showwarning("result",c)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    e3.delete(0,53)
    callback(c)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    e3.delete(0,55)
    e3.insert(0,c)
    callback(c)


def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    e3.delete(0,55)
    e3.insert(0,c)
    callback(c)


def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    e3.delete(0,55)
    e3.insert(0,c)
    e3.insert(0,c) 
    callback(c)


b=Button(r,text="add",activebackground="red",command=lambda:add())
b.grid(row=0,column=4)
b=Button(r,text="sub",activebackground="green",command=lambda:sub())
b.grid(row=1,column=4)
b=Button(r,text="multiple",activebackground="skyblue",command=lambda:mul())
b.grid(row=2,column=4)
b=Button(r,text="div",activebackground="black",command=lambda:div())
b.grid(row=3,column=4)
r.mainloop()"""



from tkinter import*
from tkinter import ttk


root=Tk()
text=Text(root,height=2,width=30)
text.pack()

var=IntVar()
r1=Radiobutton(root,text="option 1",variable=var,value=1)
r1.pack(anchor=W)
r2=Radiobutton(root,text="option 2",variable=var,value=2)
r2.pack(anchor=W)
r3=Radiobutton(root,text="Option 3",variable=var,value=3)
r3.pack(anchor=W)
r4=Radiobutton(root,text="option 4",variable=var,value=4)
r4.pack(anchor=W)


combo=ttk.Combobox(root,values=["option 1","option 2","option 3","option 4"])
combo.pack()


Checkbutton(root,text="new").pack()
Checkbutton(root,text="new1").pack()

root.mainloop()



