"""import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

r=Tk()
r.geometry("700x700")



frame=Frame(r,width=100,height=100)
frame.pack()
frame.place(relx=0.9,rely=0.5)

img=ImageTk.PhotoImage(Image.open("siva1.jpg"))
label=Button(image=img)
label.pack()

r.mainloop()
"""

import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk,Image

r=Tk()
r.geometry("500x500")
label=Label(r,text="QRcode_content:")
label.place(relx=0.1,rely=0.05)

label1=Entry(r)
label1.place(relx=0.4,rely=0.05)

b=Button(r,text="click",command=lambda:qr(r))
b.place(relx=0.6,rely=0.15)



def qr(r):

    import qrcode
    img=qrcode.make(label1.get())
    img.save("siva1.jpg")


    #pip install opencv-python
    import cv2
    qr_img=cv2.imread("siva1.jpg")
    qr_det=cv2.QRCodeDetector()
    val,pts,st_code=qr_det.detectAndDecode(qr_img)
    print("information:",val)
    
    
    from PIL import Image
    from PIL import ImageTk,Image
    frame=Frame(r,width=60,height=60)
    frame.pack()
    frame.place(relx=0.5,rely=0.68)

    img=ImageTk.PhotoImage(Image.open("siva1.jpg"))
    label=Button(image=img)
    label.pack()
    

r.mainloop()