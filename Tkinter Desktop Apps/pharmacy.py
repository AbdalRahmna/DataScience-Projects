from tkinter import *
from tkintermapview import TkinterMapView

root=Tk()
root.title("[Pharmarcy-location]:تحديد موقع الصيدليات المناوبة")
root.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\pharmacy-logo.ico")
root.geometry("1200x800+20+10")
root.resizable(False,False)
root.config(background="whitesmoke")

#------------- All functions used-----------------------

def con():
    country=EN.get()
    map.set_tile_server("https://maps.google.com/", max_zoom=40)
    map.set_address(country,marker=True)

def markzy():
    map=TkinterMapView(root,width=800,height=600 ,corner_radius=0)
    map.place(x=500,y=45)
    map.set_tile_server("https://maps.google.com/", max_zoom=40)
    map.set_position(30.02961486642975, 31.445149014077817)
    map.set_zoom(15)
    marker=map.set_marker(30.02961486642975, 31.445149014077817)
    marker.set_text("AbdalRahman[الصيدلية المركزية]")


#------------- Title1 -----------------

title=Label(root,text=" *-* مشروع الصيدليات المناوبة *-*",
            font=("Tajwal",16,"bold"),bg="black",fg="white",bd=1,relief=GROOVE,cursor="hand2").pack(fill=X)

#---------- logo for program------------

logo=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\back pharmacy.png")
lab_log=Label(root,width=225,bg="whitesmoke",height=250,image=logo,relief=GROOVE,cursor="hand2").place(x=1,y=30)

logo1=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\pharmacy logo.png")
lab_log1=Label(root,width=225,bg="whitesmoke",height=250,image=logo1,relief=GROOVE,cursor="hand2").place(x=230,y=30)

#-------- label + entery + button-----------

l=Label(root,text="->>country:",font=("Tajwal",13),fg="black",bg="whitesmoke",cursor="hand2").place(x=3,y=300)

EN=Entry(root,width=12,font=("Tajwal,12"),fg="red",bd=2,relief=GROOVE,justify="center",cursor="hand2").place(x=98,y=300)

def on_enter(e):
    btn["background"]="#ED9121"

def on_leave(e):
    btn["background"]="black"

btn=Button(root,text=" Get-country ",bg="black",fg="white"
           ,font=("Tajawal",12),bd=1,relief=SOLID,
           cursor="hand2",activebackground="#B8860B",width=10,activeforeground="#B22222",command=con)
btn.place(x=220,y=300)

btn.bind("<Enter>",on_enter)
btn.bind("<Leave>",on_leave)


#---------- pharatcyes buttons-------

def on_enter1(e):
    btn1["background"]="#ED9121"

def on_leave1(e):
    btn1["background"]="white"

btn1=Button(root,text="صيدلية المركزية",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B",command=markzy)
btn1.place(x=10,y=350)

btn1.bind("<Enter>",on_enter1)
btn1.bind("<Leave>",on_leave1)



def on_enter2(e):
    btn2["background"]="#ED9121"

def on_leave2(e):
    btn2["background"]="white"

btn2=Button(root,text="صيدلية المزرعة",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn2.place(x=130,y=350)

btn2.bind("<Enter>",on_enter2)
btn2.bind("<Leave>",on_leave2)


def on_enter3(e):
    btn3["background"]="#ED9121"

def on_leave3(e):
    btn3["background"]="white"

btn3=Button(root,text="صيدلية الطحان",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn3.place(x=250,y=350)

btn3.bind("<Enter>",on_enter3)
btn3.bind("<Leave>",on_leave3)


def on_enter4(e):
    btn4["background"]="#ED9121"

def on_leave4(e):
    btn4["background"]="white"

btn4=Button(root,text="صيدلية جماصينى",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn4.place(x=10,y=385)

btn4.bind("<Enter>",on_enter4)
btn4.bind("<Leave>",on_leave4)

def on_enter5(e):
    btn5["background"]="#ED9121"

def on_leave5(e):
    btn5["background"]="white"

btn5=Button(root,text="صيدلية الفاروق",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn5.place(x=130,y=385)

btn5.bind("<Enter>",on_enter5)
btn5.bind("<Leave>",on_leave5)

def on_enter6(e):
    btn6["background"]="#ED9121"

def on_leave6(e):
    btn6["background"]="white"

btn6=Button(root,text="صيدلية أبوكر",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn6.place(x=250,y=385)

btn6.bind("<Enter>",on_enter6)
btn6.bind("<Leave>",on_leave6)


def on_enter7(e):
    btn7["background"]="#ED9121"

def on_leave7(e):
    btn7["background"]="white"

btn7=Button(root,text=" صيدلية سمرقند",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn7.place(x=10,y=420)

btn7.bind("<Enter>",on_enter7)
btn7.bind("<Leave>",on_leave7)


def on_enter8(e):
    btn8["background"]="#ED9121"

def on_leave8(e):
    btn8["background"]="white"

btn8=Button(root,text=" صيدلية زهور",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn8.place(x=130,y=420)

btn8.bind("<Enter>",on_enter8)
btn8.bind("<Leave>",on_leave8)


def on_enter9(e):
    btn9["background"]="#ED9121"

def on_leave9(e):
    btn9["background"]="white"

btn9=Button(root,text=" صيدلية الذئاب",
            cursor="hand2",bg="white",fg="black",
            bd=1,relief=SOLID,font=("Tajwal",12),
            width=13,activeforeground="#B22222",activebackground="#B8860B")
btn9.place(x=250,y=420)

btn9.bind("<Enter>",on_enter9)
btn9.bind("<Leave>",on_leave9)

#-------- part of mapview---------------

map=TkinterMapView(root,width=800,height=600 ,corner_radius=0)
map.place(x=500,y=45)

root.mainloop()