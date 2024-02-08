#  رسم ألأشكال وألكتابة على الصور 

import cv2
img=cv2.imread("images/twins.png")       

#line:خط  , rectangle:مربع , text: وضع نص , circle:دائرة

#cv2.line(img1,(x,y),(end,height),(red,green,blue),think font)

cv2.line(img,(10,10),(200,10),(0,255,0),10)  #لأنشاء خط

cv2.rectangle(img,(150,20),(400,200),(0,255,0),2)  # لأنشاء مربع
cv2.putText(img,"baby face",(200,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)


cv2.imshow("AbdalRahman",img)

p=cv2.waitKey()
if p== ord("q"):
    cv2.destroyAllWindows()
elif p==ord("s"):
    cv2.imwrite("D:\\twins.png",img)
    cv2.destroyAllWindows()
    print("The image is saved")














            