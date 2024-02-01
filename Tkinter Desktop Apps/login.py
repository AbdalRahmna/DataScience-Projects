from tkinter import*
from tkinter.messagebox import*
import pyttsx3

root=Tk()
root.title("Login-Signup:[SYSTEM]")
root.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\blue-logo-of-personal-login.ico")
root.geometry("400x500+100+50")
root.resizable(False,False)
root.config(background="whitesmoke")

#--------- رسالة ترحيب صوتية---------

word=pyttsx3.init()
word.say(" Devloper abdalrahman hebishy welcome you in his Application")
word.setProperty("rate",100) #للتحكم فى سرعة ومعدل الصوت
word.runAndWait()

#----------- important images---------------
Gmail=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\GMail.png")

password=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\login password btn.png")
passwd=password.subsample(10,10)

close=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\exit.png")
clos=close.subsample(10,10)

user=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\blue logo of personal login.png")
use=user.subsample(6,6)

sif=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\signup2.png")
si=sif.subsample(4,4)

#---------------- الدوال---------------------

def on1(event=None):
    signup_btn["background"]="black" 
def lv1(event=None):
    signup_btn["background"]='white'

def on2(event=None):
    login_btn["background"]="black" 
def lv2(event=None):
    login_btn["background"]='white'

def hide(event=None):
    root.geometry("400x340+100+50")

def show():
    showinfo("نظام التسجيل","لقد تم التسجيل")

def ask():
   p=askyesno("نظام التسجيل","هل لديك حساب فعلا")
   if p==0 :
        return
   else:
       askyesno("نظام التسجيل","هل تريد التسجيل وتابعة التقدم؟")
    
def quit1():
    c=askokcancel("الخروج","هل تريد الخروج؟")    
    if c==0:
        return 
    else:
        root.quit()

#----------- images-----------------

background=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\back ground photo.png")

login=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\btnlog.png")
log=login.subsample(5,5)

signup=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\btn sognup.png")
sign=signup.subsample(5,5)

#------------------- buttons and  background------------------------

back=Label(root,text="*-* :واجهة تسجيل المستخدم*-*",fg="#EE82EE",
           font=("tajwal",16,"bold"),compound=BOTTOM
           ,image=background,width=200,
           height=200,bg="whitesmoke",cursor="hand2").place(x=100,y=10)

login_btn=Button(root,text="login-in",fg="#EE82EE",bg="whitesmoke"
                 ,activebackground="#FFD700",
                 activeforeground="#ADD8E6",compound=TOP,font=("tajawal",12),
                 image=log,cursor="hand2",bd=1,relief=GROOVE)

login_btn.place(x=100,y=250)


signup_btn=Button(root,text="sign-up",fg="#EE82EE",bg="whitesmoke"
                 ,activebackground="#FFD700",
                 activeforeground="#ADD8E6",compound=TOP,font=("tajawal",12),
                 image=sign,cursor="hand2",bd=1,relief=GROOVE)

signup_btn.place(x=250,y=250)

#--------- log system-----------

def log1(event=None):
    root.geometry('600x500+100+50')
    
    F1=Frame(root,bg='white',bd=0,relief=GROOVE)
    F1.place(x=400,y=5,width=205,height=500)
    
    b1=Button(F1,image=clos,bd=0,relief=SOLID,
              bg="whitesmoke",fg="whitesmoke",activebackground="#7CFC00",activeforeground="#008000",cursor="hand2",command=hide)
    b1.place(x=180,y=170)
    
    lb=Label(F1,text="LOGIN-SYSTEM",fg="red",
            bg="white",font=("times for roman",16,"underline"))
    lb.place(x=10,y=5)
     
    lb1=Label(F1,text="-Email:",fg="red",
            bg="yellow",font=("times for roman",16),image=Gmail,compound=LEFT,cursor="hand2")
    lb1.place(x=10,y=35)
    
    
    en1=Entry(F1,width=13,fg="black",bg="white",font=("times for roman",16),cursor="hand2")
    en1.place(x=10,y=70)

    lb2=Label(F1,text="Username",fg="red",
            bg="yellow",font=("times for roman",16),image=use,compound=LEFT,cursor="hand2")
    lb2.place(x=10,y=110)

    en2=Entry(F1,width=13,fg="black",bg="white",font=("times for roman",16),cursor="hand2")
    en2.place(x=10,y=150)

    lb3=Label(F1,text="PASSWORD",fg="red",
            bg="yellow",font=("times for roman",16),cursor="hand2",image=passwd,compound=LEFT)
    lb3.place(x=10,y=190)

    en3=Entry(F1,width=13,fg="black",bg="white",font=("times for roman",16),cursor="hand2")
    en3.place(x=10,y=230)
    
    b1=Button(F1,text="login",image=use,bg="white"
              ,font=("times for roman",12),cursor="hand2"
              ,fg="blue",activebackground="#1F1F1F"
              ,activeforeground="#7CFC00",compound=LEFT,command=show)
    b1.place(x=50,y=300)

    b2=Button(F1,text="signup",bg="white",font=("times for roman",12),cursor="hand2"
              ,fg="blue",activebackground="#1F1F1F",
              activeforeground="#7CFC00",compound=LEFT,image=si,command=ask)

    b2.place(x=50,y=350)
    
#--------------- sign system------------
def sigh1(event=None):
    root.geometry('600x500+100+50')
    
    F1=Frame(root,bg='white',bd=0,relief=GROOVE)
    F1.place(x=400,y=5,width=205,height=500)
    
    b3=Button(F1,image=clos,bd=0,relief=SOLID,
              bg="whitesmoke",fg="whitesmoke",activebackground="#7CFC00",activeforeground="#008000",cursor="hand2",command=hide)
    b3.place(x=180,y=170)
    
    l=Label(F1,text="SIGN-SYSTEM",fg="red",
            bg="white",font=("times for roman",16,"underline"))
    l.place(x=10,y=5)
     
    lb11=Label(F1,text="-Email1:",fg="red",
            bg="yellow",font=("times for roman",16),image=Gmail,compound=LEFT,cursor="hand2")
    lb11.place(x=10,y=35)
    
    
    en11=Entry(F1,width=13,fg="black",bg="white",font=("times for roman",16),cursor="hand2")
    en11.place(x=10,y=70)

    lb22=Label(F1,text="Username1",fg="red",
            bg="yellow",font=("times for roman",16),image=use,compound=LEFT,cursor="hand2")
    lb22.place(x=10,y=110)

    en22=Entry(F1,width=13,fg="black",bg="white",font=("times for roman",16),cursor="hand2")
    en22.place(x=10,y=150)

    lb33=Label(F1,text="PASSWORD1",fg="red",
            bg="yellow",font=("times for roman",16),cursor="hand2",image=passwd,compound=LEFT)
    lb33.place(x=10,y=190)

    en33=Entry(F1,width=13,fg="black",bg="white",font=("times for roman",16),cursor="hand2")
    en33.place(x=10,y=230)
    
    b11=Button(F1,text="login",image=use,bg="white"
              ,font=("times for roman",12),cursor="hand2"
              ,fg="blue",activebackground="#1F1F1F"
              ,activeforeground="#7CFC00",compound=LEFT,command=show)
    b11.place(x=50,y=300)

    b22=Button(F1,text="signup",bg="white",font=("times for roman",12),cursor="hand2"
              ,fg="blue",activebackground="#1F1F1F",
              activeforeground="#7CFC00",compound=LEFT,image=si,command=ask)

    b22.place(x=50,y=350)

#----------- images-----------------

background=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\back ground photo.png")

login=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\btnlog.png")
log=login.subsample(5,5)

signup=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\profesinal login images\\btn sognup.png")
sign=signup.subsample(5,5)

#------------------- buttons and  background------------------------

back=Label(root,text="*-* :واجهة تسجيل المستخدم*-*",fg="#EE82EE",
           font=("tajwal",16,"bold"),compound=BOTTOM
           ,image=background,width=200,
           height=200,bg="whitesmoke",cursor="hand2").place(x=100,y=10)

login_btn=Button(root,text="login-in",fg="#EE82EE",bg="whitesmoke"
                 ,activebackground="#FFD700",
                 activeforeground="#ADD8E6",compound=TOP,font=("tajawal",12),
                 image=log,cursor="hand2",bd=1,relief=GROOVE,command=log1)

login_btn.place(x=100,y=250)


signup_btn=Button(root,text="sign-up",fg="#EE82EE",bg="whitesmoke"
                 ,activebackground="#FFD700",
                 activeforeground="#ADD8E6",compound=TOP,font=("tajawal",12),
                 image=sign,cursor="hand2",bd=1,relief=GROOVE,command=sigh1)

signup_btn.place(x=250,y=250)

close_btn=Button(root,bg="whitesmoke"
                 ,activebackground="#FF6347",
                 font=("tajawal",10),
                 image=clos,cursor="hand2",bd=1,relief=GROOVE,command=quit1)

close_btn.place(x=340,y=5)

#---------  events -----------------
login_btn.bind('<Enter>' , on2)
login_btn.bind('<Leave>' , lv2)

signup_btn.bind('<Enter>' , on1)
signup_btn.bind('<Leave>' , lv1)

root.bind('<Control-v>',hide) #لأخفاء الجزء ctr+v



root.mainloop()
