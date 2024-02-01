# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:39:55 2023

@author: EL-Hussein Store
"""
from math import pi
from tkinter import*
from tkinter.messagebox import *
import pyttsx3
#---------- speech------------------
word=pyttsx3.init()
word.say("Devloper abdalRahman welcome with you")
word.runAndWait()
#----------- Objects window------------
root=Tk()
root.title("Calculate the Areas")
root.geometry("1024x600+100+100")
root.resizable(False,False)
root.config(background="whitesmoke")
root.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\زهور-زرقاء.ico")
#--------------- Frame 1------------------------------------
F1=Frame(root,bg="black",cursor="hand2",bd=2,relief=GROOVE,height=30,width=1024).place(x=10,y=5)
title=Label(F1,text="*-* -(Calculation-Areas-Project)- *-*",font=("ariel",16,"underline"),bg="black",fg="red",relief=SOLID)
title.pack(fill=X)

#-------------- All Labels------------------
label1=Label(root,text="enter the length",font=("ariel",12,"italic"),bg="black",fg="blue",relief=SOLID)
label1.place(x=250,y=50)

label2=Label(root,text="enter the width",font=("ariel",12,"italic"),bg="black",fg="blue",relief=SOLID)
label2.place(x=250,y=100)

label3=Label(root,text="enter the height",font=("ariel",12,"italic"),bg="black",fg="blue",relief=SOLID)
label3.place(x=250,y=150)

label4=Label(root,text="",font=("ariel",12,"italic"),bg="black",fg="blue",relief=SOLID)
label4.place(x=310,y=200)

label5=Label(root,text="Result=",font=("ariel",12,"italic"),bg="black",fg="blue",relief=SOLID)
label5.place(x=250,y=200)

label6=Label(root,text="meter",font=("ariel",12,"italic"),bg="whitesmoke",fg="blue")
label6.place(x=500,y=50)

label7=Label(root,text="meter",font=("ariel",12,"italic"),bg="whitesmoke",fg="blue")
label7.place(x=500,y=100)

label8=Label(root,text="meter",font=("ariel",12,"italic"),bg="whitesmoke",fg="blue")
label8.place(x=500,y=150)

#--------- Variables-----------
en1=IntVar()
en1.set("0 meter")
en2=IntVar()
en2.set("0 meter")
en3=IntVar()
en3.set("0 meter")

#---------------- All Enteries---------------------

entery1=Entry(root,width=10,font=("ariel",12,"italic"),bg="black",fg="red",relief=SOLID,cursor="hand2",textvariable=en1)
entery1.place(x=400,y=50)

entery2=Entry(root,width=10,font=("ariel",12,"italic"),bg="black",fg="red",relief=SOLID,cursor="hand2",textvariable=en2)
entery2.place(x=400,y=100)

entery3=Entry(root,width=10,font=("ariel",12,"italic"),bg="black",fg="red",relief=SOLID,cursor="hand2",textvariable=en3)
entery3.place(x=400,y=150)
#============ All Functions=========================
def volume_cubic():
    l=float(entery1.get())
    w=float(entery2.get())
    h=float(entery3.get())
    v=(l*w*h)
    if v>=0:
        showinfo("calculate of volume",str(v)+"M^3")
        label4.configure(text=str(v)+"m^2")
    else:
       showerror("calculate the volume"," that value is not valid")
       label4.cnfigure(text=" this value is not valid")

def area_square():
    l=eval(entery1.get())
    w=eval(entery2.get())
    area=(l*w)
    if area>=0:
        showinfo("calculate of Area",str(area)+"M*2")
        label4.configure(text=str(area)+"m^2")
    else:
        showerror("calculate the Area"," that value is not valid")
        label4.cnfigure(text=" this value is not valid")
 
def area_triangle():
       l=eval(entery1.get())
       w=eval(entery2.get())
       A=(0.5*l*w)
       if A>=0:
          showinfo("calculate of Area",str(A)+"M^2")
          label4.configure(text=str(A)+"m^2")
       else:
          showinfo("calculate the Area"," that value is not valid")
          label4.cnfigure(text=" this value is not valid") 
def circle_area(): 
     r=eval(entery1.get())
     A=(pi*r**2)
     if A>=0:
        showinfo("calculate of Area",str(A)+"M^2")
        label4.configure(text=str(A)+"m^2")
     else:
        showerror("calculate the Area"," that value is not valid")
        label4.cnfigure(text=" this value is not valid") 
def volume_circle(): 
     h=eval(entery3.get()) 
     r=eval(entery1.get())
     v=(pi*r**2*h)
     if v>=0:
         showinfo("calculate of Volume",str(v)+"M^3")
         label4.configure(text=str(v)+"m^3")
     else:
         showerror("calculate the Area"," that value is not valid")
         label4.cnfigure(text=" this value is not valid") 

def Quit():
    p=askokcancel("Close","Do you want to close Programm?")
    if p==0:
        return
    else:
        root.quit()

def Dev():
    showinfo("Devloper","Devloped by AbdalRahman Hebishy")

def hide(event=None):
    root.geometry("240x600")
def show(event=None):
    root.geometry("1024x600")

#=========== Frame2=================
F2=Frame(root,width=240,height=599,bd=1,relief=GROOVE,background="black").place(x=1,y=35)
#============= Some important Images:===============================
image1=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\student1.png")
image2=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\student2.png")
image3=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\student3.png")
g=image3.subsample(2,2)
#================== Label for background=======
ground=Label(root,text="*-* DESkTop Application *-*",image=image1,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,bd=2,compound=TOP)
ground.place(x=790,y=50)

ground1=Label(root,text="*-* DESkTop Application *-*",image=image2,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,bd=2,compound=TOP)
ground1.place(x=410,y=300)

ground3=Label(root,text="*-* DESkTop Application *-*",image=g,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,bd=2,compound=TOP)
ground3.place(x=5,y=400)
#================ functions on-enter and on-leave========================

def on_enter(event=None):
    btn1['background']="orange"
def on_leave(event=None):
    btn1["background"]="black"    

def on_enter1(event=None):
    btn2['background']="orange"
def on_leave1(event=None):
    btn2["background"]="black"    

def on_enter2(event=None):
    btn3['background']="orange"
def on_leave2(event=None):
    btn3["background"]="black" 

def on_enter3(event=None):
    btn4['background']="orange"
def on_leave3(event=None):
    btn4["background"]="black"         

def on_enter4(event=None):
    btn5['background']="orange"
def on_leave4(event=None):
    btn5["background"]="black"        

def on_enter5(event=None):
    btn6['background']="red"
def on_leave5(event=None):
    btn6["background"]="black"     

def on_enter6(event=None):
    btn7['background']="#872657"
def on_leave6(event=None):
    btn7["background"]="black"   

def on_enter7(event=None):
    btn8['background']="red"
def on_leave7(event=None):
    btn8["background"]="black"  

def on_enter8(event=None):
    btn9['background']="#872657"
def on_leave8(event=None):
    btn9["background"]="black"           

def on_enter9(event=None):
    btn10['background']="#B0E0E6"
def on_leave9(event=None):
    btn10["background"]="black"         

#------------------- Desigen of Next page: -------------------------
def Next():
#------------ objects of next page--------------------
  pro=Tk()
  pro.title("Calculator-of-Age")
  pro.geometry("500x500+100+50")
  pro.resizable(False,False)
  pro.config(background="whitesmoke")
  pro.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\زهور-زرقاء.ico")
  #---------------- labels and enters-------------------
  labell=Label(pro,text=" Enter your Age",bg="yellow",fg="red",relief=SOLID,bd=2,cursor="hand2")
  labell.place(x=10,y=10)

  age=StringVar()
  age.set("00")

  ent=Entry(pro,width=2,bg="orange",textvariable=age,cursor="hand2")
  ent.place(x=120,y=10)

  def calc():
    year=(ent.get())
    months=int(year)*12
    weaks=int(months)*4
    days=int(year)*365
    line_One=(f"my age in years: {year}")
    line_two=(f"my age in months: {months}")
    line_three=(f"my age in weaks: {weaks}")
    line_four=(f"my age in days: {days}")
        
    l=[line_One,line_two,line_three,line_four]
    showinfo("my age :",l)
  but=Button(pro,text="calculate the Age",command=calc,bg="#e91e63",fg="white")
  but.place(x=50,y=100)

  but_1=Button(pro,text=" Close",command=lambda:root.destroy(),bg="red",fg="black",relief=SOLID)
  but_1.place(x=300,y=100)

  pro.mainloop()
#============ All Buttons========================
btn1=Button(F2,text="Volume Cubic",command=volume_cubic,font=("ariel",12,"italic"),bg="black",activeforeground="red",fg="blue",relief=GROOVE,activebackground="black",cursor="hand2")
btn1.place(x=10,y=50)

btn1.bind('<Enter>',on_enter)
btn1.bind('<Leave>',on_leave)

btn2=Button(F2,text="Square Area",command=area_square,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activebackground="black",activeforeground="red")
btn2.place(x=10,y=100)

btn2.bind('<Enter>',on_enter1)
btn2.bind('<Leave>',on_leave1)

btn3=Button(F2,text="Triangle Area",command=area_triangle,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activeforeground="red",activebackground="black")
btn3.place(x=10,y=150)

btn3.bind('<Enter>',on_enter2)
btn3.bind('<Leave>',on_leave2)

btn4=Button(F2,text="circle Area",command=circle_area,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activeforeground="red",activebackground="black")
btn4.place(x=10,y=200)

btn4.bind('<Enter>',on_enter3)
btn4.bind('<Leave>',on_leave3)

btn5=Button(F2,text="volume circle",command=volume_circle,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activeforeground="red",activebackground="black")
btn5.place(x=10,y=250)

btn5.bind('<Enter>',on_enter4)
btn5.bind('<Leave>',on_leave4)


btn6=Button(F2,text="Close",command=Quit,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activebackground="black",activeforeground="red")
btn6.place(x=10,y=300)

btn6.bind('<Enter>',on_enter5)
btn6.bind('<Leave>',on_leave5)

btn7=Button(F2,text="about_us",command=Dev,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activebackground="black",activeforeground="red")
btn7.place(x=100,y=300)

btn7.bind('<Enter>',on_enter6)
btn7.bind('<Leave>',on_leave6)

btn8=Button(F2,text="hide",command=hide,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activebackground="black",activeforeground="red")
btn8.place(x=10,y=350)

btn8.bind('<Enter>',on_enter7)
btn8.bind('<Leave>',on_leave7)

btn9=Button(F2,text="show",command=show,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activebackground="black",activeforeground="red")
btn9.place(x=100,y=350)

btn9.bind('<Enter>',on_enter8)
btn9.bind('<Leave>',on_leave8)

btn10=Button(F2,text="Next-Page",command=Next,font=("ariel",12,"italic"),bg="black",fg="blue",relief=GROOVE,cursor="hand2",activebackground="black",activeforeground="red")
btn10.place(x=50,y=550)

btn10.bind('<Enter>',on_enter9)
btn10.bind('<Leave>',on_leave9)

root.bind('<Control-v>',hide)


root.mainloop()