from tkinter import*
from tkinter import PhotoImage
import webview 
import pyttsx3

#     === objects ===
app=Tk()
app.title("Social App")
app.geometry("1000x600+100+200")
app.iconbitmap(r"C:\\Users\\EL-Hussein Store\\Desktop\\images\\icon-social-media.ico")
app.resizable=(False,False)
app.config(background="whitesmoke")
# ========= welcome speeh============
word=pyttsx3.init()
word.say(" Devloper abdalrahman hebishy welcome you in his Application")
word.runAndWait()

#      ========== oop ==========

def face_book():
    url='https://www.facebook.com'
    webview.create_window(
       "AbdalRahman Hebishy [Facebook]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,

    )
    webview.start()


def you_tube():
    url='https://www.youtube.com'
    webview.create_window(
        "AbdalRahman Hebishy[youtube]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()


def instagram():
    url='https://www.instegram.com/'
    webview.create_window(
        "AbdalRahman Hebishy[instegram]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()

def tele_gram():
    url='https://www.telegram.com'
    webview.create_window(
        "AbdalRahman Hebishy[telegram]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()

def linkedin():
    url='https://www.linkedin.com/'
    webview.create_window(
        "AbdalRahman Hebishy[linkedin]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()


def whats():
    url='https://web.whatsapp.com/'
    webview.create_window(
        "AbdalRahman Hebishy[whats app]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()


def mess():
    url='https://www.messanger.com/'
    webview.create_window(
        "AbdalRahman Hebishy[massenger]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()


def spot():
    url='https://www.spotify.com/'
    webview.create_window(
        "AbdalRahman Hebishy[spotify]",
        url,
        width=1100,
        height=800,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()

def Gmail():
    url='https://accounts.google.com/b/0/AddMailService'
    webview.create_window(
        "AbdalRahman Hebishy[GMAIL]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()

def Twiter():
    url='https://twitter.com/home?'
    webview.create_window(
        "AbdalRahman Hebishy[Twiter]",
        url,
        width=800,
        height=600,
        resizable=(False,False),
        background_color="#D8D8D8",
        x=190 , y=120,
        zoomable=True,
    )
    webview.start()



# ==== Top title ====

title1=Label(app,text="Social Application System",font=("Courier",16,"underline"),fg="black",bg="white")
title1.pack(fill=X)

# ======= background image =========

logo=PhotoImage(file ="C:\\Users\\EL-Hussein Store\\Desktop\\images\\profile.png")
pan=Label(app,image=logo,bg="whitesmoke")
pan.place(x=240,y=85,height=400,width=700)

#       ======== Buttom title  ========


title2=Label(app,text="تطبيق مواقع التواصل الأجتماعى ",font=("Courier",26,'bold'),fg="black",bg="whitesmoke")
title2.place(x=290,y=520)


#      ============= frame and frame-title ===========

side=Frame(app,width=250,height=780,bg="white",bd=0,relief=GROOVE).place(x=0,y=24)

side_title1=Label(side,text="Devloped by:\nAbdalRahman Hebishy",fg="black"
                  ,bg="white",font=("italic",13)).place(x=5,y=15)

#         =========== images ===========

profile=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\profile.png")

facebook=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\face.png")

youtube=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\yotube.png")

insta=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\instagram.png")
ins=insta.subsample(5,5)

tele=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\telegram.png")
tel=tele.subsample(2,2)

link=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\linkedin.png")
lin=link.subsample(3,3)

what=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\whatsup.png")
wha=what.subsample(3,3)

massenger=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\messenger.png")
mass=massenger.subsample(5,5)

spotify=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\spotify.png")
spo=spotify.subsample(2,2)

Gmi=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\GMail.png")

twit=PhotoImage(file="C:\\Users\\EL-Hussein Store\\Desktop\\images\\Twiter.png")
twi=twit.subsample(3,3)

# ============  Buttons,profile and frame-title,  ============

lb=Label(side,text="Zahra-web",
            cursor="hand2",image=profile,
            compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white"
            )

lb.place(x=25,y=55)


side_title2=Label(side,text="Social App:",fg="black"
                  ,bg="white",font=("Courier",13)).place(x=5,y=280)


btn1=Button(side,text="facebook",
            cursor="hand2",image=facebook,
            compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=face_book
            )

btn1.place(x=5,y=320)



btn2=Button(side,text="youtube",
            cursor="hand2",image=youtube,
            compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=you_tube
            )

btn2.place(x=5,y=390)


btn3=Button(side,text="instagram",
            cursor="hand2",image=ins,
            compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=instagram
            )

btn3.place(x=5,y=450)

btn4=Button(side,text="telegram",
            cursor="hand2",image=tel,
            compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=tele_gram
            )

btn4.place(x=5,y=510)

btn5=Button(side,text="linkedin",
            cursor="hand2",image=lin
            ,compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=linkedin
            )

btn5.place(x=5,y=600)


btn6=Button(side,text="whats",
            cursor="hand2",image=wha
            ,compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=whats
            )

btn6.place(x=100,y=510)

btn7=Button(side,text="messanger",
            cursor="hand2",image=mass
            ,compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=mess
            )

btn7.place(x=100,y=450)


btn8=Button(side,
            cursor="hand2",image=spo
            ,text="spotify",compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=spot
            )

btn8.place(x=100,y=300)

btn9=Button(side,
            cursor="hand2",image=Gmi
            ,text="GMAIL",compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=Gmail
            )

btn9.place(x=100,y=390)

btn10=Button(side,
            cursor="hand2",image=twi
            ,text="Twiter",compound=TOP,
            width=100,
            bd=0,relief=RIDGE,
            bg="white",
            command=Twiter
            )

btn10.place(x=100,y=610)

app.mainloop()