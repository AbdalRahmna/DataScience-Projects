import cv2
img1=cv2.imread("basic.jpg")          # الصورة ألأساسية
img2=cv2.imread("images/one.jpg")    

if img1.shape == img2.shape:
    
    print("The image have the same sizes and channels")
    
    diff=cv2.subtract(img1,img2)                 #  للمقارنة مابين الصور بشكل أدق
    
    b ,g ,r =cv2.split(diff)                     #  يعتبر 3طبقات للمقارنة مابين الصور 
    
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 :
        print(" images are Completely The Same")
        cv2.rectangle(img2,(50,100),(125,150),(0,255,0),1)
        cv2.putText(img2," images are The same",(5,70),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,0,0),1)
else:
    cv2.rectangle(img2,(50,100),(125,150),(0,255,0),1)  # لأنشاء مربع
    cv2.putText(img2,"The images are Different",(5,70),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,0,0),1)
    print("the image are differnt")
cv2.imshow("AbdalRahman",img2)
cv2.waitKey(0)