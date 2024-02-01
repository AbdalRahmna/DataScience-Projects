from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql
import pyttsx3

class Student:
   # ----------- أنشاء نافذة البرنامج---------------
    def __init__(self,root):
        self.root=root
        self.root.title("برنامج ادارة الجامعة")
        self.root.geometry("1350x690+1+1")
        self.root.iconbitmap("C:\\Users\\EL-Hussein Store\\Desktop\\images\\student2 (1).ico")
        self.root.config(background="silver")
        self.root.resizable(False,False)
        
        title=Label(self.root,
        text="* نظام تسجيل الطلاب *",
        bg="red",fg="white",bd="1",font=("Helvetica",16,"bold"),cursor="hand2")
        title.pack(fill=X)
    
    #--------------- Variables-----------------
        self.id=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.phon=StringVar() 
        self.moahl=StringVar()
        self.gender=StringVar()
        self.address=StringVar()
        self.se1=StringVar()
        self.se2=StringVar()
        self.dell=StringVar()
    
    #       ----------------- انشاء أدوات التحكم بالبرنامج----------------------
        Mange_Frame=Frame(self.root,bg="white",bd="3",relief=GROOVE)
        Mange_Frame.place(x=1137,y=30,height=400,width=210) 
        
        lbl_ID=Label(Mange_Frame,text=":كود الطالب",bg="white")
        lbl_ID.pack()
        
        id_entery=Entry(Mange_Frame,textvariable=self.id,bd="2",width=25,justify="center",cursor="hand2")
        id_entery.pack()
        
        lbl_name=Label(Mange_Frame,text=":أسم الطالب")
        lbl_name.pack()
        
        name_entery=Entry(Mange_Frame,textvariable=self.name,bd="2",width=25,justify="center",cursor="hand2")
        name_entery.pack()
        
        lbl_email=Label(Mange_Frame,text=":ايميل الطالب")
        lbl_email.pack()
        
        email_entery=Entry(Mange_Frame,textvariable=self.email,bd="2",width=25,justify="center",cursor="hand2")
        email_entery.pack()
        
        lbl_phon=Label(Mange_Frame,text=":هاتف الطالب")
        lbl_phon.pack()
        
        phon_entery=Entry(Mange_Frame,textvariable=self.phon,bd="2",width=25,justify="center",cursor="hand2")
        phon_entery.pack()
        
        lbl_certi=Label(Mange_Frame,text=":مؤهلات الطالب")
        lbl_certi.pack()
        
        certi_entery=ttk.Combobox(Mange_Frame,textvariable=self.moahl,
                                  width=25,cursor="hand2",values=("A+","A","B+","B","C+","C","D","F"),state="readonly")
        certi_entery.pack()
        
        lbl_gender=Label(Mange_Frame,text=":اختر جنس الطالب",bg="white")
        lbl_gender.pack()
        
        comb_gender=ttk.Combobox(Mange_Frame,textvariable=self.gender,values=("ذكر","أنثى"),state="readonly",width=25,cursor="hand2")
        comb_gender.pack()
        
        lbl_address=Label(Mange_Frame,text=":عنوان الطالب",bg="white")
        lbl_address.pack()
        
        address_entery=Entry(Mange_Frame,bd="2",textvariable=self.address,width=25,justify="center",cursor="hand2")
        address_entery.pack()
        
        lbl_delet=Label(Mange_Frame,fg="red",bg="white",text=":حذف طالب بلأسم")
        lbl_delet.pack()
        
        delet_entery=Entry(Mange_Frame,textvariable=self.dell,bd="2",width=25,justify="center",cursor="hand2")
        delet_entery.pack()
    
    
    # --------------- buttons------------------
        btn_frame=Frame(self.root,bg="white",bd="2",relief=GROOVE)
        btn_frame.place(x=1137,y=435,width=210,height=260)
        
        title1=Label(btn_frame,text=":لوحة التحكم",font=("Deco",14,"underline"),bg="red",fg="white") 
        title1.pack(fill=X)
        
        add_btn=Button(btn_frame,text=":اضافة طالب",activebackground="#58D68D",bg="#4A4A4A",fg="white",cursor="hand2"
                       ,width=10,height=2,bd="2",relief=GROOVE,command=self.add_student)
        add_btn.place(x=110,y=33)
        
        del_btn=Button(btn_frame,text=":حذف طالب",activebackground="#CB4335",bg="#4A4A4A",fg="white",cursor="hand2"
                       ,width=10,height=2,bd="2",relief=GROOVE,command=self.delete)
        del_btn.place(x=10,y=33)
        
        update_btn=Button(btn_frame,text=": تعديل بيان طالب",activebackground="#5DADE2",bg="#4A4A4A",fg="white",cursor="hand2"
                          ,width=10,height=2,bd="2",relief=GROOVE,command=self.update)
        update_btn.place(x=10,y=190)
        
        clear_btn=Button(btn_frame,text=":تفريغ الحقول",activebackground="#FFB533",bg="#4A4A4A",fg="white",cursor="hand2"
                         ,width=10,height=2,bd="2",relief=GROOVE,command=self.clear)
        clear_btn.place(x=10,y=110)
        
        about_btn=Button(btn_frame,text=":من نحن",activebackground="#33FF5B",cursor="hand2",bg="#4A4A4A",fg="white",
                         width=10,height=2,bd="2",relief=GROOVE,command=self.about_us)
        about_btn.place(x=110,y=190)
        
        Exit_btn=Button(btn_frame,text=":اغلاق البرنامج",activebackground="#FFF933",cursor="hand2",bg="#4A4A4A",fg="white"
                        ,width=10,height=2,bd="2",relief=GROOVE,command=root.quit)
        Exit_btn.place(x=110,y=110)
    
    
    # --------------search mangement-----------------------

        search_frame=Frame(self.root,bg="white",)
        search_frame.place(x=1,y=30,width=1134,height=50)       
        
        lbl_search=Label(search_frame,text=":البحث عن طالب",font=("ariel",10),bg="white")
        lbl_search.place(x=1034,y=12)
        
        combo_search=ttk.Combobox(search_frame,textvariable=self.se1,values=("Id","email","phon","Name"),justify="right",state="readonly",cursor="hand2")
        combo_search.place(x=885,y=12)
        
        search_entery=Entry(search_frame,textvariable=self.se2,justify="right",bd="2",cursor="hand2",width=25)
        search_entery.place(x=700,y=12)
         
        search_btn=Button(search_frame,text="بحث",bg="red",bd="2",relief=GROOVE,
                          activebackground="#D7FF33",width=10,height=1,fg="white",cursor="hand2",command=self.search)
        
        search_btn.place(x=600,y=12)
    
    # --------------------------details عرض النتائج والبيانات---------------------------

        Details_frame=Frame(self.root,bg="#DAF7A6")
        Details_frame.place(x=1,y=82,width=1134,height=610)
        
        #----------- scrolls--------------
        scroll_x=Scrollbar(Details_frame,orient=HORIZONTAL)
        
        scroll_y=Scrollbar(Details_frame,orient=VERTICAL)   
        #------ treeview ------
        self.student_tabel=ttk.Treeview(Details_frame,
        columns=("address","gender","certi","phon","email","name","ID"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_tabel.place(x=18,y=1,width=1130,height=580)
        #----------------:( يلزم استخدام الطريقتين معا )(أسطر 4)) scrool لحل مشكلة عدم ظهور --------------
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)
        
        #-----------------  : للتحكم بالى هنكتبة فى اثشي تبع كل عمود--------------------
        self.student_tabel["show"]="headings"
        self.student_tabel.heading("address",text="عنوان الطالب")       
        self.student_tabel.heading("gender",text="جنس الطالب") 
        self.student_tabel.heading("certi",text="موهلات الطالب")
        self.student_tabel.heading("phon",text="رقم تليفون الطالب")  
        self.student_tabel.heading("email",text="ايميل الطالب")
        self.student_tabel.heading("name",text="اسم الطالب")
        self.student_tabel.heading("ID",text="كود الطالب")  
       #-----------------------:للتحكم فى حجم كل عمود لكى تظهر كلها معا-----------------
          
        self.student_tabel.column("address",width=130)
        
        self.student_tabel.column("gender",width=30)
        
        self.student_tabel.column("certi",width=65)
        
        self.student_tabel.column("phon",width=65)
        
        self.student_tabel.column("email",width=70)
        
        self.student_tabel.column("name",width=100)
        
        self.student_tabel.column("ID",width=12)
        
        self.student_tabel.bind("<ButtonRelease-1>",self.get_cursor)
     
     
     # ----- con + add database-----
        self.fetch_all() # fetchلاستدعاء دالة 
        
    def add_student(self): 
            con=pymysql.connect(
                 host='localhost',
                 user='root',
                 passwd='',
                database="student")
            cur = con.cursor()  #دالة العمليات
            # لتنفيذ العمليات
            cur.execute(' insert into students values (%s , %s , %s , %s , %s , %s , %s  )',
                (
                self.address.get(),
                self.gender.get(),
                self.moahl.get(),
                self.phon.get(),
                self.email.get(),
                self.name.get(),
                self.id.get()
                ))
            
            
            con.commit()
            self.fetch_all()         #لجلبها وأبقائها قبل ما يقفل السيرفر
            self.clear()
            con.close()    

   #--------------------: جلب البيانات-----------------
    def fetch_all(self):
        con=pymysql.connect(
              host='localhost',
              user="root",
              passwd="",
              database='student')
        cur = con.cursor()
        cur.execute('select * from students') #تنفذ امر معين
        rows=cur.fetchall() #لجلب كل البيانات الموجودة بكل الصفوف
        if len(rows) !=0:
             self.student_tabel.delete(*self.student_tabel.get_children())
             for row in rows :
                  self.student_tabel.insert("",END,value=row)
              
        
        con.commit()
        con.close() 
    #-----------------: دالة مسح اى بيان للطالب------------------           
    def delete(self):
        con=pymysql.connect(
              host="localhost",
              user="root",
              passwd="",
              database='student')
        cur = con.cursor()
        cur.execute('delete from students where name=%s' , self.dell.get())           
        con.commit()
        self.fetch_all()
        con.close()
    
    #----------------    :دالة تفريغ الحقول------------------
    def clear(self):
         self.id.set('')
         self.name.set('')
         self.email.set('')
         self.phon.set('')
         self.gender.set('')
         self.moahl.set('')
         self.address.set('')
         self.dell.set('')

    #--------------------( cursor :دالة استدعاء ) ------------------

    def get_cursor(self,ev):
         cursor_row = self.student_tabel.focus()   #  دالة الضغط والتحديد  
         contents = self.student_tabel.item(cursor_row)
         row=contents['values']
         self.id.set(row[6])
         self.name.set(row[5])
         self.email.set(row[4])
         self.phon.set(row[3])
         self.moahl.set(row[2])
         self.gender.set(row[1])
         self.address.set(row[0])

    #----------------- : دالة تعديل البيانات-----------------------

    def update(self):
        con=pymysql.connect(
                 host='localhost',
                 user='root',
                 passwd='',
                database="student")
        cur = con.cursor()
        cur.execute('update students set address=%s , gender=%s , moahl=%s, phon=%s ,email=%s ,name=%s where id=%s ' ,
                (
                self.address.get(),
                self.gender.get(),
                self.moahl.get(),
                self.phon.get(),
                self.email.get(),
                self.name.get(),
                self.id.get()
                ))
        con.commit()
        self.fetch_all()         
        self.clear()
        con.close() 
    #------------------- دالة البحث----------------------------
    def search(self):
        con=pymysql.connect(
              host='localhost',
              user="root",
              passwd="",
              database='student')
        cur = con.cursor()
        cur.execute("select * from students where " + 
            str(self.se1.get()) +" LIKE '%"+str(self.se2.get()) + " %'")   
        rows=cur.fetchall() 
        if len(rows) !=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for row in rows :
                  self.student_tabel.insert("",END,value=row)
            con.commit()
        con.close() 
    
    #--------------------- دالة من نحن-------------------------------
    def about_us(self):
        showinfo("Devloped by :AbdalRahman Gameel Hebishy","welcome to our system")
        askyesno("question","هل أعجبك نظامانا ؟")         
    
root=Tk()
#=========== speeh welcome================
word=pyttsx3.init()
word.say(" Devloper abdalrahman hebishy welcome you in his Application")
word.runAndWait()

ob=Student(root)
root.mainloop()