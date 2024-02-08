from tkinter import *
import pyttsx3
import speech_recognition as sr
from pydub.playback import play
import qrcode
import time
from tkinter.messagebox import *
from pydub import AudioSegment

root=Tk()
root.title("Employees Qrcode[AbdalRahman]")
root.geometry("500x470+500+100")
root.iconbitmap("images\Qr-Code2.ico")
root.resizable(False,False)
root.config(background="whitesmoke")

#--------- function to welcome----------------
def welcome():
    music=AudioSegment.from_mp3("sounds\welcome.mp3")
    play(music)

#----------  functions of sounds and recognion of sounds------------------

wel=pyttsx3.init()
voices = wel.getProperty('voices')          #لجلب المايك والتعامل مع ألأصوات
wel.setProperty('voice',voices[0])          #لأستعمال مايك الجهاز 

def Speak(audio):
    wel.say(audio)
    wel.runAndWait()

def TakeCommands():
    command = sr.Recognizer()
    with sr.Microphone() as mic :
        command.phrase_threshold=0.5       # دقة التسمع والتصنت
        audio = command.listen(mic)         #    لأستماع ألى المايك
        try:
           query=command.recognize_google(audio, language='ar')        # لتحديد الغة وطريقة التعرف عليها
        except Exception as Error :
            print(Error)     
        return query.lower()


def bt1():
    query=TakeCommands()
    name=query
    En1.insert(0,name)

def bt2():
    query=TakeCommands()
    name=query
    En2.insert(0,name)

def bt3():
    query=TakeCommands()
    name=query
    En3.insert(0,name)

def bt4():
    query=TakeCommands()
    name=query
    En4.insert(0,name)


#--------- Function to save file----------------
def Sv():
    namefile=En5.get()
    name=En1.get()
    co=En2.get()
    jo=En3.get()
    code=En4.get()
    info=qrcode.make("Name:"+name+"\n"+"\n"+"Country:" + co+"\n"+"\n"+"JOB:"+ jo+ "\n"+"\n"+ "Employee Code :"+ code)
    info.save("G:\\programing Courses\\openCV Course\\Employees project\\employee" + namefile +'.jpg' )
    showinfo('save','save ['+ namefile + ']employee')

def Exit():
    p=askokcancel("quit","Do you want to Quit from program ?")
    if p==0:
        return
    else:
        root.quit()

#---------- background-photo and some images---------------

photo=PhotoImage(file="images\Qr-Code3.png")
background=Label(root,image=photo,width=495,height=200).place(x=2,y=4)

sound=PhotoImage(file="images\sound.png")
sound1=sound.subsample(6,6)

save=PhotoImage(file="images\save.png")
save1=save.subsample(6,6)

ext=PhotoImage(file="images\Exit.png")
ext1=ext.subsample(6,6)
#----------------labels  -------------------

l1=Label(root,text="Emp Name :",background="whitesmoke",cursor="hand2",foreground="gold",font=("Tajawel",15)).place(x=10,y=230)

l2=Label(root,text="Country :",background="whitesmoke",cursor="hand2",foreground="gold",font=("Tajawel",15)).place(x=10,y=270)

l3=Label(root,text="Emp Job :",background="whitesmoke",cursor="hand2",foreground="gold",font=("Tajawel",15)).place(x=10,y=310)

l4=Label(root,text="Emp Code :",background="whitesmoke",cursor="hand2",foreground="gold",font=("Tajawel",15)).place(x=10,y=350)

#-------------------Entiries ------------------------------------

En1=Entry(root,width=20,justify=CENTER,foreground="black",cursor="hand2",background="whitesmoke",font=("Tajawel",10))
En1.place(x=130,y=230)

En2=Entry(root,width=20,justify=CENTER,foreground="black",cursor="hand2",background="whitesmoke",font=("Tajawel",10))
En2.place(x=130,y=270)

En3=Entry(root,width=20,justify=CENTER,foreground="black",cursor="hand2",background="whitesmoke",font=("Tajawel",10))
En3.place(x=130,y=310)

En4=Entry(root,width=20,justify=CENTER,foreground="black",cursor="hand2",background="whitesmoke",font=("Tajawel",10))
En4.place(x=130,y=350)

#----------------- Buttons--------------------------------

btn1=Button(root,image=sound1,cursor="hand2",background="tomato",activebackground="white",command=bt1)
btn1.place(x=280,y=230)

btn2=Button(root,image=sound1,cursor="hand2",background="tomato",activebackground="white",command=bt2)
btn2.place(x=280,y=270)

btn3=Button(root,image=sound1,cursor="hand2",background="tomato",activebackground="white",command=bt3)
btn3.place(x=280,y=310)

btn4=Button(root,image=sound1,cursor="hand2",background="tomato",activebackground="white",command=bt4)
btn4.place(x=280,y=350)

#-----label and entery to save  ------------------

l5=Label(root,text="Save :",background="whitesmoke",cursor="hand2",foreground="gold",font=("Tajawel",15)).place(x=10,y=390)

En5=Entry(root,width=20,justify=CENTER,foreground="black",cursor="hand2",background="whitesmoke",font=("Tajawel",10))
En5.place(x=130,y=390)

btn5=Button(root,text="Save",compound=LEFT,image=save1,cursor="hand2",foreground="yellow",activeforeground="gold",background="tomato",activebackground="white",command=Sv)
btn5.place(x=280,y=390)

l6=Label(root,text="Devloped By : AbdalRahman Hebishy  ",background="whitesmoke",font=("Tajawel",15,"italic"))
l6.place(x=135,y=425)

btn6=Button(root,text="Exit",image=ext1,compound=LEFT,cursor="hand2",foreground="yellow",activeforeground="gold",background="tomato",activebackground="white",command=Exit)
btn6.place(x=400,y=310)

welcome()
root.mainloop()
