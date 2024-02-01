from tkinter import *
from tkinter import ttk
from tkinter.messagebox import*
import webbrowser
import os
import sys , random , math 
import pyttsx3
import cv2
import datetime  #pkg to mange in time and date
from tkinter import ttk
import openpyxl  # to dealing with excel files
from openpyxl import Workbook  #  to create excel fiel
       
root=Tk()
#-------------- speech welcome with objects ------------------
word=pyttsx3.init()
word.say(" Devloper abdalrahman hebishy welcome you in his Application")
word.runAndWait()
root.title("SuperMarket")
root.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\supermarket5.ico")
root.geometry("1024x550+280+50")
root.resizable(False,False)
root.config(background="whitesmoke")

#-------------- images---------------------
image1=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\face.png")

image2=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\telegram.png")
imge2=image2.subsample(4,4)

image3=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\profile.png") 
imge3=image3.subsample(6,6)

image4=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\supermarket1.png")
imge4=image4.subsample(6,6)

image5=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\whats small.png")
imge5=image5.subsample(4,4)

image6=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\exit2.png")
imge6=image6.subsample(5,5)

ground=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\supermarket.png")

log_image=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\login1.png")
imge=log_image.subsample(5,5)

ground_photo=Label(root,image=ground,width=400,height=300,bg="whitesmoke").place(x=120,y=43)

# -----------main title----------------
title=Label(root,text="**الصفحة الرئيسية والدخول**"
   ,font=("tajawal",16,"bold"),fg="gold",bg="black",cursor="hand2",bd="1").pack(fill=X)

#--------------------------- برمجة الأزرار  الفيس و الواتس و التليجرام------------------------
# لنا هناurl نضع اى 
url1='https://www.facebook.com'
url2='https://www.telegram.com'
url3='https://web.whatsapp.com/'

def open_facebook():
    webbrowser.open_new(url1)

def open_telegram():
    webbrowser.open_new(url2)

def open_whats():
    showinfo("OUR whatsup","phon=01557486097")   

def about_us():
    showinfo("المطور","البرنامج برمجتة بواسطة \nعبدالرحمن جميل حبيشى")

def project():
    showinfo("المشروع","مشروع سطح مكتب تكينتر")
    askyesno("المشروع","هل أعجبك برنامجنا؟")

def login():
   user=str(en1.get())
   password=str(en2.get())
   
   if user=="AbdalRahman" and password == "2742003":
       showinfo("الترحيب","  أهلا وسهلا بكم  بياناتك صحيحة ")
       #---------- New-Window------------------
       
        
       
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   else:
       showerror("خطأ","عذرا يوجد خطأ فى كلمة المرور او اسم المستخدم")
       s=cv2.VideoCapture(0) # لوكاميرة لابتوب او محمول:0 لأخذ لقطة شاشة
       ret,image=s.read() #لقراءة الصورة بشكل خفلى
       cv2.imwrite('lock.png',image)     #lock لحفظ الصورة باسم 
       del(s) #لخفاء الألتقاط

def close():
    p=askyesno("اغلاق","هل تريد الخروج من البرنامج؟") 
    if p==0:
        return
    else:
       root.quit()             

#----------- Frame1-----------

fr1=Frame(root , width=300, height=520 ,bg="#138D75",bd="2",relief=GROOVE).place(x=723,y=30)

title1=Label(fr1,width=30,text="مشروع سوبر ماركت",font=("Helvetica",12,"bold"),
            fg="#FF5733",cursor="hand2",bg="whitesmoke").place(x=730,y=40)


title2=Label(fr1,width=30,text="  المطور: عيدالرحمن جميل",font=("Helvetica",12,"bold"),
              fg="#FF5733",cursor="hand2",bg="whitesmoke").place(x=730,y=70)

title3=Label(fr1,width=30,text=" : وسائل الاتصال بنا-",font=("Times New Roman",12,"underline"),
              fg="#17202A",cursor="hand2",bg="#A93226").place(x=740,y=100)

btn1=Button(fr1,text=":حسابنا على الفيس بوك",font=("ariel",10),fg="black",bg="whitesmoke",cursor="hand2"
            ,activebackground="#0000EE",image=image1,
            compound=LEFT,activeforeground="red",command=open_facebook).place(x=800,y=150)

btn2=Button(fr1,text=" حسابنا على التليجرام",image=imge2,compound=LEFT,font=("ariel",10),fg="black",bg="whitesmoke",cursor="hand2"
            ,activebackground="#0000EE",activeforeground="red",command=open_telegram).place(x=800,y=210)

btn3=Button(fr1,text="لمحة عن المطور ",image=imge3,compound=LEFT,font=("ariel",10),fg="black",bg="whitesmoke",cursor="hand2"
            ,activebackground="#0000EE",activeforeground="red",command=about_us).place(x=800,y=270)

btn4=Button(fr1,text=" لمحة عن المشروع",font=("ariel",10),image=imge4,compound=LEFT,fg="black",bg="whitesmoke",cursor="hand2"
            ,activebackground="#0000EE",activeforeground="red",command=project).place(x=800,y=330)

btn5=Button(fr1,text=": رقم الواتساب الخاص بنا",font=("ariel",10),image=imge5,compound=LEFT,fg="black",bg="whitesmoke",cursor="hand2"
            ,activebackground="#0000EE",activeforeground="red",command=open_whats).place(x=800,y=410)

btn6=Button(fr1,text=" :أغلاق البرنامج",font=("ariel",10),image=imge6,compound=LEFT,fg="black",bg="whitesmoke",cursor="hand2"
            ,activebackground="#0000EE",activeforeground="red",command=close).place(x=800,y=470)


#--------------------Frame 2--------------------
fr2=Frame(root,width=722,height=160,bg="#138D75"
          ,bd="2",relief=GROOVE).place(x=1,y=410)

ground_frame=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\login.png")
ground1=ground_frame.subsample(2,2)

rame_photo=Label(fr2,image=ground1).place(x=603,y=430)

lb1=Label(fr2,text=":اسم المستخدم  ",fg="gold",bg="#138D75",
          font=("tajawal",13),cursor="hand2").place(x=500,y=450)

lb2=Label(fr2,text=":كلمة  المرور  ",fg="gold",bg="#138D75",
          font=("tajawal",13),cursor="hand2").place(x=500,y=500)

en1=Entry(fr2,width=20,font=("tajawal",12),justify="center",cursor="hand2")
en1.place(x=310,y=450)

en2=Entry(fr2,width=20,justify="center",font=("tajawal",12),cursor="hand2")
en2.place(x=310,y=500)

log_btn=Button(fr2,text="تسجيل الدخول",font=("tajawal",12),
fg="black",bg="whitesmoke",activebackground="#B8860B",activeforeground="#98F5FF"
               ,compound=LEFT,cursor="hand2",image=imge,command=login).place(x=90,y=470)


root.mainloop()