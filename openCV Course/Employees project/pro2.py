from tkinter import *
from tkinter .messagebox import *
import os
import cv2
from tkinter import filedialog

window=Tk()
window.title("Employees scanner[AbdalRahman]")
window.geometry("500x470+500+100")
window.iconbitmap("images\Qr-Code2.ico")
window.resizable(False,False)
window.config(background="whitesmoke")

def open():
    file =filedialog.askopenfile(mode='r',filetypes=[("Files" ,' *.jpg' )] )       #     لتحديد نوعية الملفات المراد فتحها وقرا~تها
    if file:
        filepath=os.path.abspath(file.name)
        En1.insert(0,str(filepath))

def scan():
    d=En1.get()
    res=cv2.QRCodeDetector()    #  Qrcode  خاصية تحديد 
    val , points , s_qr=res.detectAndDecode(cv2.imread(d))          #     للتحديد وفك التشفير عن الصورة
    showinfo("Qr-scan-info",val )                     #val:لأستخراج القيم
                                                      #s_qr:الخطوط,points:النقاط
#---------- background-photo and some images---------------

photo1=PhotoImage(file="images\QrCode.png")
phot=photo1.subsample(2,2)
background=Label(window,image=phot,width=495,height=150).place(x=20,y=35)

#------------ Title of page---------------
lb1=Label(window,text='QR_Scanner',fg="whitesmoke",bg="black",font=("Tajawel",16))
lb1.pack(fill=X)

lb2=Label(window, text='QR-Code Scanner',width=70, font=("Tajawel",12),fg="whitesmoke",bg="green").place(x=1,y=250)

En1=Entry(window,width=50,font=("Tajawel",13),cursor="hand2",bg="gray",fg="red")
En1.place(x=10,y=290)

#--------- buttons-------------

btn=Button(window,text="Select Image",fg="white",bg="green",width=50,font=("Tajawel",12),cursor="hand2",command=open)
btn.place(x=10,y=335)

bt=Button(window,text="Read QRCOde",fg="white",bg="red",width=50,font=("Tajawel",12),cursor="hand2",command=scan)
bt.place(x=10,y=383)

window.mainloop()
