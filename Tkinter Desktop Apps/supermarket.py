from tkinter import*
from tkinter.messagebox import *
from tkinter import ttk
import random , math , os 


class Super :
    def __init__(self,pro):
        self.pro=pro
        self.pro.title("سوبر ماركت")
        self.pro.geometry("1300x700+30+10")
        self.pro.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\supermarket7.ico")
        self.pro.resizable(False,False)  
        self.pro.config(background="whitesmoke")
        main_title=Label(self.pro,text="Super-Market: ادارة المشاريع "
                         ,font=("tajawal",16,"bold"),bg="#0B2F3A",fg="white",cursor="hand2")
        main_title.pack(fill=X)        
        
        
        # ------------ متغيرات الحساب الكلى------------------
        self.bacoliat = StringVar()
        self.adoat = StringVar()
        self.kahrba =StringVar()
        #------------------- متغيرات البقوليات--------------------
        self.e1=IntVar()
        self.e2=IntVar()
        self.e3=IntVar()
        self.e4=IntVar()
        self.e5=IntVar()
        self.e6=IntVar()
        self.e7=IntVar()
        self.e8=IntVar()
        self.e9=IntVar()
        self.e10=IntVar()
        self.e11=IntVar()
        self.e12=IntVar()
        self.e13=IntVar()
        self.e14=IntVar()
        #--------------------- متغيرات الوازم المنزلية--------------------
        self.eq1=IntVar()
        self.eq2=IntVar()
        self.eq3=IntVar()
        self.eq4=IntVar()
        self.eq5=IntVar()
        self.eq6=IntVar()
        self.eq7=IntVar()
        self.eq8=IntVar()
        self.eq9=IntVar()
        self.eq10=IntVar()
        self.eq11=IntVar()
        self.eq12=IntVar()
        self.eq13=IntVar()
        self.eq14=IntVar()
        #------------ متغيرات ألأدوات الكهربية--------------
        self.ee1=IntVar()
        self.ee2=IntVar()
        self.ee3=IntVar()
        self.ee4=IntVar()
        self.ee5=IntVar()
        self.ee6=IntVar()
        self.ee7=IntVar()
        self.ee8=IntVar()
        self.ee9=IntVar()
        self.ee10=IntVar()
        self.ee11=IntVar()
        
        #------------------------  متغيرات بيانات المشترى-----------------

        self.NAME=StringVar()
        self.PHON=StringVar()
        self.FATORA=StringVar()
        rado=random.randint(1000,9999)
        self.FATORA.set(str(rado))
        
        #---------------- CUstomer DATA  (Frame1) بيانات المشتري--------------------
        
        fr1=Frame(self.pro,bg="#0B4C5F",relief=GROOVE,bd=2)
        fr1.place(x=960,y=32,width=338,height=170)
        
        title=Label(fr1,text=":بيانات المشترى-",font=("tajawal",13,"underline"),bg="#0B4C5F",fg="tomato",cursor="hand2")
        title.place(x=233,y=0)
        
        his_name=Label(fr1,text=":أسم المشترى-",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="white",cursor="hand2")
        his_name.place(x=230,y=40)
        
        his_phon=Label(fr1,text=":رقم المشترى-",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="white",cursor="hand2")
        his_phon.place(x=230,y=80)
        
        bill_num=Label(fr1,text=":أسم الفاتورة-",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="white",cursor="hand2")
        bill_num.place(x=230,y=120)

        en_name=Entry(fr1,width=20,cursor="hand2",textvariable=self.NAME,bd=2,relief=GROOVE,justify="center")
        en_name.place(x=100,y=40)

        en_phon=Entry(fr1,width=20,cursor="hand2",textvariable=self.PHON,bd=2,relief=GROOVE,justify="center")
        en_phon.place(x=100,y=80)
        
        en_bill=Entry(fr1,width=20,cursor="hand2",bd=2,textvariable=self.FATORA,relief=GROOVE,justify="center")
        en_bill.place(x=100,y=120)

        
        btn_customer=Button(fr1,text="  تأكيد الحساب",font=("tajawal",13),bg="whitesmoke",fg="#0B4C5F",
                activebackground="#FF1493",activeforeground="#00BFFF",width=10,cursor="hand2",command=self.billing)
        
        btn_customer.place(x=0,y=50)

        #-------------------- فاتورة----------------------------

        fatora=Label(fr1,text="[الفاتورة]",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        fatora.place(x=125,y=145)

        fr2=Frame(self.pro,bd=2,width=338,height=399,bg="white",relief=GROOVE)
        fr2.place(x=960,y=205)
        #--------------- جزء مهم سكرول بالتيكست------------------ 
        '''
        عند انشاء اى سكرول نمر ب 4 مراحل :ملحوظة هامة
        1-انشاءة
        2-yscrollcommand=sc_y.set
        3- location (side,fill)تحدد موقعة 
        4-view (xview or yview)
        '''
        
        sc_y=Scrollbar(fr2,orient=VERTICAL)
        self.textarea=Text(fr2,yscrollcommand=sc_y.set)
        sc_y.pack(side=LEFT,fill=Y)
        sc_y.config(command=self.textarea.yview)#8B814C
        self.textarea.pack(fill=BOTH,expand=1)

        #--------------price   -----------------
        fr3=Frame(self.pro,bd=2,width=657,height=112,bg="#0B4C5F",relief=GROOVE)
        fr3.place(x=641,y=574)
        
        hesab=Button(fr3,text="الحساب",width=13,height=1,font=("tajwal,10")
                     ,bg="#DBA901",fg="whitesmoke",activebackground="#E9967A",activeforeground="black",bd=1,command=self.total,relief=GROOVE,cursor="hand2")
        hesab.place(x=528,y=10)

        fatora1=Button(fr3,text="تصدير الفاتورة",width=13,height=1,font=("tajwal,10")
                     ,bg="#DBA901",fg="whitesmoke",activebackground="#E9967A",activeforeground="black",bd=1,relief=GROOVE,cursor="hand2",command=self.welcome)
        
        fatora1.place(x=528,y=50)

        clear=Button(fr3,text="افراغ الحقول",width=13,height=1,font=("tajwal,10")
                     ,bg="#DBA901",fg="whitesmoke",activebackground="#E9967A",activeforeground="black",bd=1,relief=GROOVE,cursor="hand2",command=self.clear)
        
        clear.place(x=400,y=10)

        Exit=Button(fr3,text="أغلاق البرنامج",width=13,height=1,font=("tajwal,10")
                     ,bg="#DBA901",fg="whitesmoke",activebackground="#E9967A",activeforeground="black",bd=1,relief=GROOVE,cursor="hand2",command=pro.quit)
        
        Exit.place(x=400,y=50)

        lbl_o1=Label(fr3,text=":الحساب الكلى للبقوليات",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        lbl_o1.place(x=220,y=10)

        lbl_o2=Label(fr3,text=" :حساب الوازم المنزلية",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        lbl_o2.place(x=220,y=45)

        lbl_o3=Label(fr3,text=" :حساب ألادوات الكهربية",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        lbl_o3.place(x=220,y=80)
        
        en1=Entry(fr3,width=24,textvariable=self.bacoliat,justify="center",cursor="hand2")
        en1.place(x=40,y=12) 

        en2=Entry(fr3,width=24,textvariable=self.adoat,justify="center",cursor="hand2")
        en2.place(x=40,y=45) 

        en3=Entry(fr3,width=24,textvariable=self.kahrba,justify="center",cursor="hand2")
        en3.place(x=40,y=82) 
        
        #-------------- Frame[item1]----------------
        F1=Frame(self.pro,bd=2,width=318,height=664 ,bg="#0B4C5F",relief=GROOVE)
        F1.place(x=1,y=35)
        #------------ Labels of item1------------
        t =Label(F1,text="البقوليات",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        t.place(x=122,y=0) 
        
        it1 =Label(F1,text=":القمح -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it1.place(x=250,y=25) 
        
        it2 =Label(F1,text=":الأرز -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it2.place(x=250,y=70) 
        
        it3=Label(F1,text=":برغل -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it3.place(x=250,y=120) 
        
        it4=Label(F1,text=":  فاصولياء -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it4.place(x=230,y=170) 
        
        it5=Label(F1,text=":عدس -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it5.place(x=252,y=220) 
        
        it6=Label(F1,text=": مكرونة -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it6.place(x=240,y=270) 
        
        it7=Label(F1,text=": فول  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it7.place(x=255,y=320) 
        
        it8=Label(F1,text=":حمص -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it8.place(x=250,y=370) 
        
        it9=Label(F1,text=": ملح ببهارات -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it9.place(x=220,y=420) 
        
        it10=Label(F1,text=": ترمس -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it10.place(x=250,y=470) 
        
        it11=Label(F1,text=": فلفل أسود  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it11.place(x=230,y=520) 
       
        it12=Label(F1,text=":ذرة -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it12.place(x=265,y=550) 
        
        it13=Label(F1,text=":لوبيا -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it13.place(x=260,y=590) 
        
        it14=Label(F1,text=":شوفان -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        it14.place(x=260,y=620) 
        #--------- Enterys of item 1-------------
        
        ent1=Entry(F1,width=24,justify="center",textvariable=self.e1,cursor="hand2")
        ent1.place(x=70,y=25)

        ent2=Entry(F1,width=24,justify="center",textvariable=self.e2,cursor="hand2")
        ent2.place(x=70,y=70)

        ent3=Entry(F1,width=24,justify="center",textvariable=self.e3,cursor="hand2")
        ent3.place(x=70,y=120)

        ent4=Entry(F1,width=24,justify="center",textvariable=self.e4,cursor="hand2")
        ent4.place(x=70,y=170)

        ent5=Entry(F1,width=24,justify="center",textvariable=self.e5,cursor="hand2")
        ent5.place(x=70,y=220)

        ent6=Entry(F1,width=24,justify="center",textvariable=self.e6,cursor="hand2")
        ent6.place(x=70,y=270)

        ent7=Entry(F1,width=24,justify="center",textvariable=self.e7,cursor="hand2")
        ent7.place(x=70,y=320)

        ent8=Entry(F1,width=24,justify="center",textvariable=self.e8,cursor="hand2")
        ent8.place(x=70,y=370)

        ent9=Entry(F1,width=24,justify="center",textvariable=self.e9,cursor="hand2")
        ent9.place(x=70,y=420)

        ent10=Entry(F1,width=24,justify="center",textvariable=self.e10,cursor="hand2")
        ent10.place(x=70,y=470)

        ent11=Entry(F1,width=24,justify="center",textvariable=self.e11,cursor="hand2")
        ent11.place(x=70,y=520)

        ent12=Entry(F1,width=24,justify="center",textvariable=self.e12,cursor="hand2")
        ent12.place(x=70,y=550)

        ent13=Entry(F1,width=24,justify="center",textvariable=self.e13,cursor="hand2")
        ent13.place(x=70,y=590)

        ent14=Entry(F1,width=24,justify="center",textvariable=self.e14,cursor="hand2")
        ent14.place(x=70,y=620)
        #--------- Frame [item2]--------------------
        
        F2=Frame(self.pro,bd=2,width=318,height=664 ,bg="#0B4C5F",relief=GROOVE)
        F2.place(x=321,y=35)
        
        #------------ Labels of item2------------
        il =Label(F2,text="الوازم المنزلية",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        il.place(x=122,y=0) 
        
        il1 =Label(F2,text=":صحون -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il1.place(x=250,y=25) 
        
        il2 =Label(F2,text=":كأس -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il2.place(x=262,y=70) 
        
        il3=Label(F2,text=":شوك -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il3.place(x=262,y=120) 
        
        il4=Label(F2,text=":  ملاعق -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il4.place(x=250,y=170) 
        
        il5=Label(F2,text=":سكاكين -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il5.place(x=252,y=220) 
        
        il6=Label(F2,text=": مكنسة -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il6.place(x=252,y=270) 
        
        il7=Label(F2,text=": مصفاة  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il7.place(x=250,y=320) 
        il8=Label(F2,text=":طنجرة -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        
        il8.place(x=255,y=370) 
        il9=Label(F2,text=": صينية  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il9.place(x=250,y=420) 
        
        il10=Label(F2,text=": فتاحة علب -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il10.place(x=240,y=470) 
        
        il11=Label(F2,text=":  مقشرة  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il11.place(x=250,y=520) 
        
        il12=Label(F2,text=":اكياس-",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il12.place(x=268,y=550) 
        
        il13=Label(F2,text=":وعاء الخلط -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il13.place(x=240,y=590) 
        
        il14=Label(F2,text=":ابريق -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        il14.place(x=265,y=620) 
             
         #--------- Enterys of item 2-------------
        
        v1=Entry(F2,width=24,textvariable=self.eq1,justify="center",cursor="hand2")
        v1.place(x=70,y=25)

        v2=Entry(F2,width=24,textvariable=self.eq2,justify="center",cursor="hand2")
        v2.place(x=70,y=70)

        v3=Entry(F2,textvariable=self.eq3,width=24,justify="center",cursor="hand2")
        v3.place(x=70,y=120)

        v4=Entry(F2,textvariable=self.eq4,width=24,justify="center",cursor="hand2")
        v4.place(x=70,y=170)

        v5=Entry(F2,textvariable=self.eq5,width=24,justify="center",cursor="hand2")
        v5.place(x=70,y=220)

        v6=Entry(F2,textvariable=self.eq6,width=24,justify="center",cursor="hand2")
        v6.place(x=70,y=270)

        v7=Entry(F2,textvariable=self.eq7,width=24,justify="center",cursor="hand2")
        v7.place(x=70,y=320)

        v8=Entry(F2,textvariable=self.eq8,width=24,justify="center",cursor="hand2")
        v8.place(x=70,y=370)

        v9=Entry(F2,textvariable=self.eq9,width=24,justify="center",cursor="hand2")
        v9.place(x=70,y=420)

        v10=Entry(F2,textvariable=self.eq10,width=24,justify="center",cursor="hand2")
        v10.place(x=70,y=470)

        v11=Entry(F2,textvariable=self.eq11,width=24,justify="center",cursor="hand2")
        v11.place(x=70,y=520)

        v12=Entry(F2,textvariable=self.eq12,width=24,justify="center",cursor="hand2")
        v12.place(x=70,y=550)

        v13=Entry(F2,textvariable=self.eq13,width=24,justify="center",cursor="hand2")
        v13.place(x=70,y=590)

        v14=Entry(F2,textvariable=self.eq14,width=24,justify="center",cursor="hand2")
        v14.place(x=70,y=620)
        
        #--------- Frame [item3]--------------------
        
        F3=Frame(self.pro,bd=2,width=318,height=540 ,bg="#0B4C5F",relief=GROOVE)
        F3.place(x=643,y=35)
        
        #------------ Labels of item3------------
        iv =Label(F3,text=" الأجهزة الكهربية",font=("tajawal",13,"bold"),bg="#0B4C5F",fg="gold",cursor="hand2")
        iv.place(x=122,y=0) 

        iv1 =Label(F3,text=":تلفزيون -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv1.place(x=250,y=25) 
        
        iv2 =Label(F3,text=":غسالة -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv2.place(x=262,y=70) 
        
        iv3=Label(F3,text=":راديو -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv3.place(x=262,y=120) 
        
        iv4=Label(F3,text=":  كمبيوتر -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv4.place(x=250,y=170) 
        
        iv5=Label(F3,text=":تليفون  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv5.place(x=260,y=220) 
        
        iv6=Label(F3,text=":  مكنسة- كهربية -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv6.place(x=210,y=270) 
        
        iv7=Label(F3,text=":  غسالة أطباق -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv7.place(x=220,y=320) 
        
        iv8=Label(F3,text=":شفاط -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv8.place(x=265,y=370) 
        
        iv9=Label(F3,text=":  مصابيح كهربية   -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv9.place(x=200,y=420) 
        
        iv10=Label(F3,text=":  منشار -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv10.place(x=250,y=470) 
        
        iv11=Label(F3,text=":  شنيور  -",font=("tajawal",11),bg="#0B4C5F",fg="whitesmoke",cursor="hand2")
        iv11.place(x=250,y=510) 
        
         #--------- Enterys of item 3-------------
        
        m1=Entry(F3,textvariable=self.ee1,width=24,justify="center",cursor="hand2")
        m1.place(x=70,y=25)

        m2=Entry(F3,textvariable=self.ee2,width=24,justify="center",cursor="hand2")
        m2.place(x=70,y=70)

        m3=Entry(F3,textvariable=self.ee3,width=24,justify="center",cursor="hand2")
        m3.place(x=70,y=120)

        m4=Entry(F3,textvariable=self.ee4,width=24,justify="center",cursor="hand2")
        m4.place(x=70,y=170)

        m5=Entry(F3,textvariable=self.ee5,width=24,justify="center",cursor="hand2")
        m5.place(x=70,y=220)

        m6=Entry(F3,textvariable=self.ee6,width=24,justify="center",cursor="hand2")
        m6.place(x=70,y=270)

        m7=Entry(F3,textvariable=self.ee7,width=24,justify="center",cursor="hand2")
        m7.place(x=70,y=320)

        m8=Entry(F3,textvariable=self.ee8,width=24,justify="center",cursor="hand2")
        m8.place(x=70,y=370)

        m9=Entry(F3,textvariable=self.ee9,width=24,justify="center",cursor="hand2")
        m9.place(x=60,y=420)

        m10=Entry(F3,textvariable=self.ee10,width=24,justify="center",cursor="hand2")
        m10.place(x=70,y=470)

        m11=Entry(F3,textvariable=self.ee11,width=24,justify="center",cursor="hand2")
        m11.place(x=70,y=505)

       #----------- الحساب الكلى------------
        self.welcome()   #لتنفيذ اوامر الدالة الفاتورة
    def total(self):   
         #------------------ حساب البقوليات----------------------
        self.kameh=self.e1.get()*1.5
        self.rez=self.e2.get()*2
        self.porhal=self.e3.get()*2.5
        self.phasolia=self.e4.get()*3
        self.adsy=self.e5.get()*2
        self.makarona=self.e6.get()*3.5
        self.phool=self.e7.get()*5
        self.homos=self.e8.get()*3
        self.malh=self.e9.get()*1
        self.temas=self.e10.get()*10
        self.falfal=self.e11.get()*15
        self.dora=self.e12.get()*2
        self.lopia=self.e13.get()*3
        self.shofan=self.e14.get()*14
        
        self.totalito=float(
                    self.kameh
                    +self.rez
                    +self.porhal
                    +self.phasolia
                    +self.adsy
                    +self.makarona
                    +self.phool
                    +self.homos
                    +self.malh
                    +self.temas
                    +self.falfal
                    +self.dora
                    +self.lopia
                    +self.shofan
                    )
        
        self.bacoliat.set(str(self.totalito)+"$")


        #------------------ حساب الوازم المنزلية------------------
        self.kameh1=self.eq1.get()*10
        self.rez1=self.eq2.get()*15
        self.porhal1=self.eq3.get()*12
        self.phasolia1=self.eq4.get()*16
        self.adsy1=self.eq5.get()*18
        self.makarona1=self.eq5.get()*20
        self.phool1=self.eq6.get()*22
        self.homos1=self.eq7.get()*23
        self.malh1=self.eq8.get()*14
        self.temas1=self.eq9.get()*16
        self.falfal1=self.eq10.get()*21
        self.dora1=self.eq1.get()*24
        self.lopia1=self.eq1.get()*26
        self.shofan1=self.eq1.get()*15

        self.home=float(
            self.kameh1+
            self.rez1+
            self.porhal1+
            self.phasolia1+
            self.adsy1+
            self.makarona1+
            self.phool1+
            self.homos1+
            self.malh1+
            self.temas1+
            self.falfal1+
            self.dora1+
            self.lopia1+
            self.shofan1)
        self.adoat.set(str(self.home)+"$")
        
        #------------------حساب الأجهزة الكهربية----------------
        
        self.kameh2=self.ee1.get()*200
        self.rez2=self.ee2.get()*320
        self.porhal2=self.ee3.get()*150
        self.phasolia2=self.ee4.get()*170
        self.adsy2=self.ee5.get()*320
        self.makarona2=self.ee6.get()*370
        self.phool2=self.ee7.get()*200
        self.homos2=self.ee8.get()*150
        self.malh2=self.ee9.get()*125
        self.temas2=self.ee10.get()*130
        self.falfal2=self.ee11.get()*600

        self.khrab=float(
            self.kameh2+
            self.rez2+
            self.porhal2+
            self.phasolia2+
            self.adsy2+
            self.makarona2+
            self.phool2+
            self.homos2+
            self.malh2+
            self.temas2+
            self.falfal2
            )
        self.kahrba.set(str(self.khrab)+"$")
        #---------الحساب الكلى-------
        self.all=float(self.khrab+
                       self.home+
                       self.totalito)
        
        #------------دالة الفاتورة----------------    
          
    def welcome(self):
        self.textarea.delete('1.0',END)  # لمسح البيانات القديمة عند كل دخول
        self.textarea.insert(END ,"\t سوبر ماركت المعلم يرحب بكم" )
        self.textarea.insert(END,"\n ********************************************************")
        self.textarea.insert(END,f"\n\t رقم الفاتورة    :{self.FATORA.get()} ")
        self.textarea.insert(END,f"\n\t المشترى    : {self.NAME.get()} " )
        self.textarea.insert(END,f"\n\t رقم التليفون     :{self.PHON.get()}"   )
        self.textarea.insert(END,"\n ")
        self.textarea.insert(END,"\n  ")
        self.textarea.insert(END,"\n ***************************************************************")
        self.textarea.insert(END,f"    \nالسعر  |   \t   العدد  | \t    المشتريات   ")
        self.textarea.insert(END,"\n ***************************************************************")
    
    def save(self):
        op=askyesno("حفظ","هل تريد حفظ الفاتورة؟")
        if op > 0 :   # 0=no , yes>0
          self.bb=self.textarea.get('1.0',END)
          f1=open('C:\\Users\\EL-Hussein Store\\Desktop\\tkinter(Desktop App)\\المشاريع بصيغة exe\\buys'+str(self.FATORA.get())+".txt","w",encoding="utf-8")
          f1.write()
          f1.close()
        else :
            return
              
    def clear(self):
        #--------- افراغ بقوليات---------
        self.e1.set(0)
        self.e2.set(0)
        self.e3.set(0)
        self.e4.set(0)
        self.e5.set(0)
        self.e6.set(0)
        self.e7.set(0)
        self.e8.set(0)
        self.e9.set(0)
        self.e10.set(0)
        self.e11.set(0)
        self.e12.set(0)
        self.e13.set(0)
        self.e14.set(0)
        #------- افراغ لاوازم منزلية---------
        self.eq1.set(0)
        self.eq2.set(0)
        self.eq3.set(0)
        self.eq4.set(0)
        self.eq5.set(0)
        self.eq6.set(0)
        self.eq7.set(0)
        self.eq8.set(0)
        self.eq9.set(0)
        self.eq10.set(0)
        self.eq11.set(0)
        self.eq12.set(0)
        self.eq13.set(0)
        self.eq14.set(0)

        # ------- افراغ اجهزة كهربية-------
        self.ee1.set(0)
        self.ee2.set(0)
        self.ee3.set(0)
        self.ee4.set(0)
        self.ee5.set(0)
        self.ee6.set(0)
        self.ee7.set(0)
        self.ee8.set(0)
        self.ee9.set(0)
        self.ee10.set(0)
        self.ee11.set(0)

        #------------ افراغ حقول الاسم والتليفون والفاتورة والحسابات-------------------
        self.bacoliat.set("0$")
        self.adoat.set("0$")
        self.kahrba.set("0$")
        self.NAME.set("")
        self.PHON.set("")
        
    #------------  الفاتورة والدفع------------ 
    def billing(self):
      
      if self.NAME.get() == "" or self.PHON=="":
        showerror("خطأ","لا يجوز ترك حقل اسم المشترى ورقم تليفونة فارغا") 
      
      if self.bacoliat.get()=="0$" and self.adoat.get()=="0$" and self.kahrba.get()=="0$":
        showerror("خطا","لم يتم اختيار اى عنصر لشرائة")
      else:
           self.welcome()
           
           if self.e1.get()!=0:
              self.textarea.insert(END,f"\n {self.kameh} \t \t {self.e1.get()} \t \t القمح")
           
           if self.e2.get()!=0:
              self.textarea.insert(END,f"\n {self.rez} \t \t {self.e2.get()} \t \t الأرز")

           if self.e3.get()!=0:
              self.textarea.insert(END,f"\n {self.porhal} \t \t {self.e3.get()} \t \t برغل")
              
           if self.e4.get()!=0:
              self.textarea.insert(END,f"\n {self.phasolia} \t \t {self.e4.get()} \t \t فاصولياء")
            
           if self.e5.get()!=0:
              self.textarea.insert(END,f"\n {self.adsy} \t \t {self.e5.get()} \t \t عدس")                
            
           if self.e6.get()!=0:
              self.textarea.insert(END,f"\n {self.makarona} \t \t {self.e6.get()} \t \tمكرونة ")                
           
           if self.e7.get()!=0:
              self.textarea.insert(END,f"\n {self.phool} \t \t {self.e7.get()} \t \فول ")
            
           
           if self.e8.get()!=0:
              self.textarea.insert(END,f"\n {self.homos} \t \t {self.e8.get()} \t \حمص ")
            
           if self.e9.get()!=0:
              self.textarea.insert(END,f"\n {self.malh} \t \t {self.e9.get()} \t \ملح ببهارات ")
            
           if self.e10.get()!=0:
              self.textarea.insert(END,f"\n {self.temas} \t \t {self.e10.get()} \t \ ترمس ")
            
           if self.e11.get()!=0:
              self.textarea.insert(END,f"\n {self.falfal} \t \t {self.e11.get()} \t \ فلفل أسود ")
           
           if self.e12.get()!=0:
              self.textarea.insert(END,f"\n {self.dora} \t \t {self.e12.get()} \t \ ذرة ")
           
           if self.e13.get()!=0:
              self.textarea.insert(END,f"\n {self.lopia} \t \t {self.e13.get()} \t \ لوبيا ")
            
           if self.e14.get()!=0:
              self.textarea.insert(END,f"\n {self.shofan} \t \t {self.e14.get()} \t \ شوفان ")
            
           
           
           if self.eq1.get()!=0:
              self.textarea.insert(END,f"\n {self.kameh1} \t \t {self.eq1.get()} \t \t صحون")
           
           if self.eq2.get()!=0:
              self.textarea.insert(END,f"\n {self.rez1} \t \t {self.eq2.get()} \t \t كأس")

           if self.eq3.get()!=0:
              self.textarea.insert(END,f"\n {self.porhal1} \t \t {self.eq3.get()} \t \t شوك")
              
           if self.eq4.get()!=0:
              self.textarea.insert(END,f"\n {self.phasolia1} \t \t {self.eq4.get()} \t \t ملاعق")
            
           if self.eq5.get()!=0:
              self.textarea.insert(END,f"\n {self.adsy1} \t \t {self.eq5.get()} \t \t سكاكين")                
            
           if self.eq6.get()!=0:
              self.textarea.insert(END,f"\n {self.makarona1} \t \t {self.eq6.get()} \t \مكنسة ")                
           
           if self.eq7.get()!=0:
              self.textarea.insert(END,f"\n {self.phool1} \t \t {self.eq7.get()} \t \مصفاة ")
            
           
           if self.eq8.get()!=0:
              self.textarea.insert(END,f"\n {self.homos1} \t \t {self.eq8.get()} \t \طنجرة ")
            
           if self.eq9.get()!=0:
              self.textarea.insert(END,f"\n {self.malh1} \t \t {self.eq9.get()} \t \صينية  ")
            
           if self.eq10.get()!=0:
              self.textarea.insert(END,f"\n {self.temas1} \t \t {self.eq10.get()} \t \ فتاحة علب ")
            
           if self.eq11.get()!=0:
              self.textarea.insert(END,f"\n {self.falfal1} \t \t {self.eq11.get()} \t \  مقشرة ")
           
           if self.e12.get()!=0:
              self.textarea.insert(END,f"\n {self.dora1} \t \t {self.eq12.get()} \t \ أكياس ")
           
           if self.eq13.get()!=0:
              self.textarea.insert(END,f"\n {self.lopia1} \t \t {self.eq13.get()} \t \ وعاء خلط ")
            
           if self.eq14.get()!=0:
              self.textarea.insert(END,f"\n {self.shofan1} \t \t {self.eq14.get()} \t \ ابريق ")
             
           
           
           if self.ee1.get()!=0:
              self.textarea.insert(END,f"\n {self.kameh2} \t \t {self.eq1.get()} \t \t تلفزيون")
           
           if self.ee2.get()!=0:
              self.textarea.insert(END,f"\n {self.rez2} \t \t {self.eq2.get()} \t \t غسالة-ملابس")

           if self.ee3.get()!=0:
              self.textarea.insert(END,f"\n {self.porhal2} \t \t {self.eq3.get()} \t \t راديو")
              
           if self.ee4.get()!=0:
              self.textarea.insert(END,f"\n {self.phasolia2} \t \t {self.eq4.get()} \t \t كمبيوتر")
            
           if self.ee5.get()!=0:
              self.textarea.insert(END,f"\n {self.adsy2} \t \t {self.eq5.get()} \t \t تليفون")                
            
           if self.ee6.get()!=0:
              self.textarea.insert(END,f"\n {self.makarona2} \t \t {self.eq6.get()} \t \مكنسة-كهربية ")                
           
           if self.ee7.get()!=0:
              self.textarea.insert(END,f"\n {self.phool2} \t \t {self.eq7.get()} \t \غسالة أطباق ")
            
           
           if self.ee8.get()!=0:
              self.textarea.insert(END,f"\n {self.homos12} \t \t {self.eq8.get()} \t \شفاط ")
            
           if self.ee9.get()!=0:
              self.textarea.insert(END,f"\n {self.malh2} \t \t {self.eq9.get()} \t \مصابيح كهربية  ")
            
           if self.ee10.get()!=0:
              self.textarea.insert(END,f"\n {self.temas2} \t \t {self.eq10.get()} \t \  منشار ")
            
           if self.ee11.get()!=0:
              self.textarea.insert(END,f"\n {self.falfal2} \t \t {self.eq11.get()} \t \  شنيور ")
           
           self.textarea.insert(END,"\n------------------------------------------")
           self.textarea.insert(END,f"\n\t{self.all} $\t     : المجموع الكلى ")
           self.textarea.insert(END,"\n------------------------------------------")
           self.save()

        
        
        
        
pro=Tk()
ob=Super(pro)
pro.mainloop()

'''
        -important Notes
        :لاغلاق الى برنامج يوجد 3 طرق 
        1-root.quit()
        2-root.destroy()
        3-lambda:root.destroy() 
        
        -:عندما نريد ان نكتب فى داخل فايل بالغة العربية
        -encoding="utf-8" 
         
         '''