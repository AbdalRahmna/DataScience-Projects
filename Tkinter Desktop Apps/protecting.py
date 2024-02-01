from tkinter import*
import cv2 # this pkg dealing with camera to take photo :
from tkinter.messagebox import*


root1=Tk()
root1.title("[Protecting SYstem]")
root1.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\c2.ico")
root1.geometry("290x500+50+20")
root1.config(background="whitesmoke")
root1.resizable(False,False)
root1.attributes('-alpha',0.9) #لجعل النافذة شفافة

#--------- images-----------
right=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\صح.png")
r=right.subsample(6,4)

false=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\غلط.png")
f=false.subsample(6,4)

#--------- Duflts:----------------
def clear(event=None):
  En1.delete("0",END)

def one(event=None) :
  En1.insert(END,"1") 

def two(event=None) :
  En1.insert(END,"2") 

def three(event=None) :
  En1.insert(END,"3") 

def four(event=None) :
  En1.insert(END,"4") 

def five(event=None) :
  En1.insert(END,"5") 

def six(event=None) :
  En1.insert(END,"6") 

def seven(event=None) :
  En1.insert(END,"7") 

def eight(event=None) :
  En1.insert(END,"8") 

def nine(event=None) :
  En1.insert(END,"9") 

def ten(event=None) :
  En1.insert(END,"10") 

def zero(event=None) :
  En1.insert(END,"0") 

def enter(evebt=None):
  password=En1.get()
  if password=="2022":
    showinfo("التسجيل","بياناتك صحيحة تفضل بالدخول")
  else:
     s=cv2.VideoCapture(0) #  لأخذ لقطة شاشة
     ret,image=s.read() #لقراءة الصورة بشكل خفلى
     cv2.imwrite('lock.png',image)     #lock لحفظ الصورة باسم 
     del(s) #لخفاء الألتقاط
     showerror("التسجيل","عذرا بياناتك خاطئة")  

#----------- title ------------
title=Label(root1,text="SCreen Lock",fg="whitesmoke",bg="#D82148",font=("Stencil",21,"bold")).pack(fill=X)

#------------- frame tools -------------------

fr1=Frame(root1,width=298,height=460,bg='white',bd=1,relief=GROOVE)
fr1.place(x=0,y=38)

title1=Label(fr1,text="Enter the Password:",fg="whitesmoke",bg="#D82148",font=("Stencil",15),cursor="hand2").place(x=50,y=15)

En1=Entry(fr1,width=10,justify="center",font=("Impact",25),bd=2,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2")
En1.place(x=60,y=50)

#----------------- Buttons------------------

btn1=Button(fr1,text="1",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=one).place(x=5,y=110)
btn2=Button(fr1,text="2",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=two).place(x=100,y=110)
btn3=Button(fr1,text="3",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=three).place(x=200,y=110)

btn4=Button(fr1,text="4",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=four).place(x=5,y=210)
btn5=Button(fr1,text="5",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=five).place(x=100,y=210)
btn6=Button(fr1,text="6",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=six).place(x=200,y=210)

btn7=Button(fr1,text="7",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=seven).place(x=5,y=310)
btn8=Button(fr1,text="8",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=eight).place(x=100,y=310)
btn9=Button(fr1,text="9",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=nine).place(x=200,y=310)

btn10=Button(fr1,text="0",width=3,font=("Stencil",25),bd=1,relief=RIDGE,bg="white",fg="#D82148",cursor="hand2",command=zero).place(x=5,y=390)
btn11=Button(fr1,image=f,bd=1,relief=RIDGE,bg="whitesmoke",fg="#D82148",cursor="hand2",command=clear).place(x=100,y=390)
btn12=Button(fr1,image=r,bd=1,relief=RIDGE,bg="whitesmoke",fg="#D82148",cursor="hand2",activebackground="whitesmoke",command=enter).place(x=200,y=390)















root1.mainloop()    