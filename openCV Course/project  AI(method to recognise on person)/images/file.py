import cv2

#----------- متوسط القيم من أجل الدقة فى الصورة-------------------

MODEL_MEAN_VALUES=(78.4463377603,87.7689143744,114.895847746)

#-------------- أنشاء ليستا بالاعمار-----------------

age_list = ['(0,2)','(4,6)','(8,12)','(14-20)','(22,26)',
            '(28,32)','(33,38)','(40,53)','(55,60)','(62,70)','(75,90)','(90,150)']

#-------------- ليست بتحديد الجنس-------------

Gender_list=['Male','Female']

#--------------------- أستدعاء الملفات التى تتعرف على العمر والجنس-------------------

def fileGet():
    age_net=cv2.dnn.readNetFromCaffe(
        'data/deploy_age.prototxt',
        'data/age_net.caffemodel'
    )
    gender_net=cv2.dnn.readNetFromCaffe(
        'data/deploy_gender.prototxt',
        'data/gender_net.caffemodel'
    )
    return (age_net , gender_net)


def read_camera(age_net,gender_net):
    font=cv2.FONT_HERSHEY_COMPLEX       #نوع الخط
    img=cv2.imread("G:\programing Courses\openCV Course\project  AI(method to recognise on person)\images\girl2.jpg")     #استدعاء الصورة
    #----------- الملف الخاص بتحديد الوجة-----------------
    face_cascate=cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          # لتحويل نظام ألوان الصورة
    #--------------  كشف وجوة متعددة فى الصورة الواحدة--------------------
    faces=face_cascate.detectMultiScale(gray,1.1,5)
    if len(faces)>0:                        #لطباعة عدد الأوجة
        print("Found {} Faces".format(str(len(faces)))) 
        
    for (x,y,w,h) in faces :
        # رسم مستطيل حول الوجة
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        # جلب وجة ونسخة وارسالة الى الخوارزمية   
        face_img=img[y:y+h , h:h+w] .copy() 
        blob=cv2.dnn.blobFromImage(face_img , 1 , (227,227),MODEL_MEAN_VALUES,swapRB=False)
        #----------- توقع الجنس----------------       
        gender_net.setInput(blob) 
        gender_p=gender_net.forward()
        gender=Gender_list[gender_p[0].argmax()]
        print("Gender:" + gender)
        #----------- توقع العمر----------------       
        age_net.setInput(blob) 
        age_p=age_net.forward()
        age=age_list[age_p[0].argmax()]
        print("age:" + age)
        G_A="%s %s" % (gender,age)
        cv2.putText(img,G_A,(x,y),font,1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('AbdalRahmn',img)
    cv2.waitKey(0)
if __name__ =='__main__':
    age_net, gender_net =fileGet()  
    read_camera(age_net ,gender_net)  