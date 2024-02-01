from tkinter import*
import cv2 # this pkg dealing with camera to take photo :
from tkinter.messagebox import*


root1=Tk()
root1.title("[Protecting SYstem]")
root1.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\c2.ico")
root1.geometry("290x500+50+20")
#root1.config(background="whitesmoke")
root1.resizable(False,False)
#root1.attributes('-alpha',0.9) #لجعل النافذة شفافة

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
     showinfo("system","your data is correct")
     import pygame
     import pyttsx3
     # ---------- objects--------------
     root=Tk()
     root.title("Displayers music")
     root.geometry("800x600+50+20")
     root.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\icon-social-media.ico")
     root.resizable(False,False)
     root.config(background="whitesmoke")
     #------------------main title------------------

     main=Label(root,text="مشغل ألأغانى",fg="white",
           bg="black",font=("tajawal",16,"bold"),bd=2,relief=GROOVE)
     main.pack(fill=X)

     #--------------- speeh word-------------------
     word=pyttsx3.init()
     word.say(" Devloper abdalrahman hebishy welcome you in his Application")
     word.setProperty("rate",150) #للتحكم فى سرعة ومعدل الصوت
     word.runAndWait()

     #--------------------- frame-------------------------
     fr1=Frame(root,width=300,bg="black",height=590).place(x=0,y=30)

     #---------------------- labels----------------------------
     lb=Label(fr1,text="** قائمة التشغيل**",fg="white",bg="red",font=("tajawal",15,"bold"))
     lb.place(x=0,y=30,width=300)

     lb1=Label(fr1,text=":شكرا على الكلمة الحلوة-",fg="white",bg="black",font=("tajawal",13,))
     lb1.place(x=150,y=80)

     lb2=Label(fr1,text=":براحة علينا يا شيخة-",fg="white",bg="black",font=("tajawal",13,))
     lb2.place(x=165,y=110)

     lb3=Label(fr1,text=":قوم اقف وانت بتكلمنى-",fg="white",bg="black",font=("tajawal",13,))
     lb3.place(x=150,y=160)

     lb4=Label(fr1,text=": أنا مش فاكر-",fg="white",bg="black",font=("tajawal",13,))
     lb4.place(x=200,y=200)

     lb5=Label(fr1,text=":    رقصونى يلا" ,fg="white",bg="black",font=("tajawal",13,))
     lb5.place(x=180,y=250)

     lb6=Label(fr1,text=":  مصطفى حجاج -",fg="white",bg="black",font=("tajawal",13,))
     lb6.place(x=180,y=290)

     lb7=Label(fr1,text=": حكيم ولا واحد -",fg="white",bg="black",font=("tajawal",13,))
     lb7.place(x=190,y=330)

     lb8=Label(fr1,text=":   يا لهوى-",fg="white",bg="black",font=("tajawal",13,))
     lb8.place(x=210,y=380)

     lb9=Label(fr1,text=":  اسلام ساسو -",fg="white",bg="black",font=("tajawal",13,))
     lb9.place(x=200,y=420)

     lb10=Label(fr1,text=":   اية اليوم الحلو دة -",fg="white",bg="black",font=("tajawal",13,))
     lb10.place(x=170,y=465)

     #----------------------- images----------------------

     play=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\login1.png")
     play1=play.subsample(9,9)

     stop=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\exit2.png")
     stop1=stop.subsample(9,9)

     background=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\راديو.png")

     spotify=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\spotify.png")
     spo=spotify.subsample(1,2)



      #----------------- logo label----------------
     lb11=Label(fr1,image=spo,text="spotify",font=("arial",9),bg="black",compound=TOP,cursor="hand2",fg="red")
     lb11.place(x=100,y=500)

     lb12=Label(fr1,text=" **دة شعارنا اسمع وادعلنا**",font=("arial",12),bg="black",cursor="hand2",fg="red")
     lb12.place(x=100,y=580)

     lb13=Label(root,text=" *-*     دة سبوتيفاى الغلابة *-*",image=background,font=("arial",12),bg="black",compound=TOP,cursor="hand2",fg="red")
     lb13.place(x=400,y=200)

#------------------   دوال التشغيل والأيقاف لكل الأغانى-------------------

     def p1():
        pygame.init()
        pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Amr Diab - Shokran Min Hina Le Bokra (Full Version عمرو دياب - شكراً من هنا لبكرة (النسخة الكاملة.mp3")
        pygame.mixer.music.play(loops=0)

     def s1():
        pygame.mixer.music.stop()

     def p2():
      pygame.init()
      pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Bahaa Sultan - Beraha Ya Sheekha (Music Video) _ (بهاء سلطان - براحة يا شيخة (من فيلم المطاريد.mp3")
      pygame.mixer.music.play(loops=0)

     def s2():
       pygame.mixer.music.stop()


     def p3():
       pygame.init()
       pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Bahaa Sultan - Oum O2af _ بهاء سلطان - قوم أقف.mp3")
       pygame.mixer.music.play(loops=0)

     def s3():
       pygame.mixer.music.stop()

     def p4():
       pygame.init()
       pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\G.oka - Ana Msh Faker El Kobleh _  جنرال اوكا -  انا مش فاكر الكوبليه.mp3")
       pygame.mixer.music.play(loops=0)

     def s4():
       pygame.mixer.music.stop()

    
     def p5():
       pygame.init()
       pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Hakim - Ra'asoni - Official Music Video Lyrics _ 2019 _ حكيم - رقصونى - الفيديو الرسمى.mp3")
       pygame.mixer.music.play(loops=0)

     def s5():
       pygame.mixer.music.stop()

     def p6():
        pygame.init()
        pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Moustafa Hagag - Ya Mna3n3 (Official Video) _ مصطفى حجاج - يا منعنع (فيديو كليب).mp3")
        pygame.mixer.music.play(loops=0)

     def s6():
        pygame.mixer.music.stop()


     def p7():
        pygame.init()
        pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Hakim - Wala Wahed _ حكيم - ولا واحد.mp3")
        pygame.mixer.music.play(loops=0)

     def s7():
        pygame.mixer.music.stop()
 

     def p8():
       pygame.init()
       pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Mahmoud El Leithy “Ya Lahwy” 2021 محمود الليثي يالهوي.mp3")
       pygame.mixer.music.play(loops=0)

     def s8():
       pygame.mixer.music.stop()


     def p9():
        pygame.init()
        pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\Mahragan Enty M3lma l  مهرجان انتى معلمة - عمر كمال و حمو بيكا - توزيع اسلام ساسو.mp3")
        pygame.mixer.music.play(loops=0)

     def s9():
        pygame.mixer.music.stop()

     def p10():
        pygame.init()
        pygame.mixer.music.load("C:\\Users\\EL-Hussein Store\\Desktop\\Songs.mp3\\ايه اليوم الحلو ده - احمد سعد من فيلم #عمهم _ Ahmed Saad Eh ElYoum El Helw da.mp3")
        pygame.mixer.music.play(loops=0)

     def s10():
        pygame.mixer.music.stop()

     #--------------دالة ألاغلاق والتعريف بالبرنامج-----------
     def close():
        q=askokcancel("Close","Do you want close program ?")
        if q==0: 
          return
        else:
          root.quit()   
   
     def about():
        showinfo("App","Devloped by AbdalRahman Hebishy ( spotify الغلابة)")

     # -------------------------  honver   للتشغيل دوال تعريف -------------------------
     def on_enter1(e):
        dis1["background"]="blue" #color here that should show when mouse tap on it 

     def on_leave1(e):
        dis1["background"]='white'

     def on_enter2(e):
        dis2["background"]="blue" 
     def on_leave2(e):
        dis2["background"]='white' #color here should be the same color for background btn 

     def on_enter3(e):
       dis3["background"]="blue" 
     def on_leave3(e):
        dis3["background"]='white'

     def on_enter4(e):
        dis4["background"]="blue" 
     def on_leave4(e):
         dis4["background"]='white'

     def on_enter5(e):
        dis5["background"]="blue" 
     def on_leave5(e):
        dis5["background"]='white'

     def on_enter6(e):
       dis6["background"]="blue" 
     def on_leave6(e):
       dis6["background"]='white'

     def on_enter7(e):
       dis7["background"]="blue" 
     def on_leave7(e):
       dis7["background"]='white'

     def on_enter8(e):
        dis8["background"]="blue" 
     def on_leave8(e):
        dis8["background"]='white'

     def on_enter9(e):
        dis9["background"]="blue" 
     def on_leave9(e):
        dis9["background"]='white'

     def on_enter10(e):
         dis10["background"]="blue" 
     def on_leave10(e):
         dis10["background"]='white'

#---------------- دوال honver لازرار الأيقاف--------------------

     def on_enter11(e1):
        st1["background"]="green" #color here that should show when mouse tap on it 
     def on_leave11(e1):
        st1["background"]='white'

     def on_enter22(e):
        st2["background"]="green" 
     def on_leave22(e):
         st2["background"]='white' #color here should be the same color for background btn 

     def on_enter33(e):
          st3["background"]="green" 
     def on_leave33(e):
        st3["background"]='white'

     def on_enter44(e):
        st4["background"]="green" 
     def on_leave44(e):
       st4["background"]='white'

     def on_enter55(e):
        st5["background"]="green" 
     def on_leave55(e):
        st5["background"]='white'

     def on_enter66(e):
        st6["background"]="green" 
     def on_leave66(e):
        st6["background"]='white'

     def on_enter77(e):
        st7["background"]="green" 
     def on_leave77(e):
        st7["background"]='white'

     def on_enter88(e):
        st8["background"]="green" 
     def on_leave88(e):
        st8["background"]='white'

     def on_enter99(e):
         st9["background"]="green" 
     def on_leave99(e):
        st9["background"]='white'

     def on_enter101(e):
        st10["background"]="green" 
     def on_leave101(e):
        st10["background"]='white'

#------------ buttons ---------------

  dis1=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p1)
  dis1.place(x=5,y=70)
  
  dis1.bind("<Enter>",on_enter1)
  dis1.bind("<Leave>",on_leave1)  

  st1=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",
            compound=LEFT,font=("arial",10),cursor="hand2",command=s1)
  st1.place(x=80,y=70)

  st1.bind("<Enter>",on_enter11)
  st1.bind("<Leave>",on_leave11)  


  dis2=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",
            compound=LEFT,font=("arial",10),cursor="hand2",command=p2)
  dis2.place(x=5,y=110)

  dis2.bind("<Enter>",on_enter2)
  dis2.bind("<Leave>",on_leave2)  



  st2=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",
            compound=LEFT,font=("arial",10),cursor="hand2",command=s2)
  st2.place(x=80,y=110)

  st2.bind("<Enter>",on_enter22)
  st2.bind("<Leave>",on_leave22)  


  dis3=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p3)
  dis3.place(x=5,y=160)

  dis3.bind("<Enter>",on_enter3)
  dis3.bind("<Leave>",on_leave3)

  st3=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s3)
  st3.place(x=80,y=160)

  st3.bind("<Enter>",on_enter33)
  st3.bind("<Leave>",on_leave33)  


  dis4=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p4)
  dis4.place(x=5,y=200)

  dis4.bind("<Enter>",on_enter4)
  dis4.bind("<Leave>",on_leave4)

  st4=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s4)
  st4.place(x=80,y=200)

  st4.bind("<Enter>",on_enter44)
  st4.bind("<Leave>",on_leave44)  


  dis5=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p5)
  dis5.place(x=5,y=240)

  dis5.bind("<Enter>",on_enter5)
  dis5.bind("<Leave>",on_leave5)

  st5=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s5)
  st5.place(x=80,y=240)

  st5.bind("<Enter>",on_enter55)
  st5.bind("<Leave>",on_leave55)  


  dis6=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p6)
  dis6.place(x=5,y=280)

  dis6.bind("<Enter>",on_enter6)
  dis6.bind("<Leave>",on_leave6)

  st6=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s6)
  st6.place(x=80,y=280)

  st6.bind("<Enter>",on_enter66)
  st6.bind("<Leave>",on_leave66)  



  dis7=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p7)
  dis7.place(x=5,y=320)

  dis7.bind("<Enter>",on_enter7)
  dis7.bind("<Leave>",on_leave7)

  st7=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s7)
  st7.place(x=80,y=320)

  st7.bind("<Enter>",on_enter77)
  st7.bind("<Leave>",on_leave77)  

  dis8=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p8)
  dis8.place(x=5,y=370)

  dis8.bind("<Enter>",on_enter8)
  dis8.bind("<Leave>",on_leave8)

  st8=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s8)
  st8.place(x=80,y=370)

  st8.bind("<Enter>",on_enter88)
  st8.bind("<Leave>",on_leave88)  


  dis9=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p9)
  dis9.place(x=5,y=410)

  dis9.bind("<Enter>",on_enter9)
  dis9.bind("<Leave>",on_leave9)

  st9=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s9)
  st9.place(x=80,y=410)

  st9.bind("<Enter>",on_enter99)
  st9.bind("<Leave>",on_leave99)  


  dis10=Button(fr1,text="play",image=play1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=p10)
  dis10.place(x=5,y=455)

  dis10.bind("<Enter>",on_enter10)
  dis10.bind("<Leave>",on_leave10)

  st10=Button(fr1,text="stop",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=s10)
  st10.place(x=80,y=455)
  st10.bind("<Enter>",on_enter101)
  st10.bind("<Leave>",on_leave101)  

# ---------- frame2---------------
  fr2=Frame(root,width=500,height=200,bg="gray",bd=2,relief=GROOVE)
  fr2.place(x=300,y=540)
  btn1=Button(fr2,text="Close ",image=stop1,bg="white",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,font=("arial",10),cursor="hand2",command=close)
  btn1.place(x=40,y=5)

  btn2=Button(fr2,text="about us",bg="black",fg="red"
            ,activebackground="red",activeforeground="black",compound=LEFT,height=1,font=("arial",10),cursor="hand2",command=about)
  btn2.place(x=300,y=5)
  root.mainloop()

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