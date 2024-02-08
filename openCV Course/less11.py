# لو أنا عايز ألأتقط صورة للمستخدم  دون أن ]اخذ أنتباهه من الكاميرا

import cv2
cam=cv2.VideoCapture(0)   # لفتح الكاميرا وأستعمالهل
ret,frame=cam.read()      #  للقراءة الصورة الملتقطة
cv2.imwrite("D://took.png",frame)  # لحفظها باسم معين فى مسار
del(cam)                     #لأخفاء ألتقاط الصورة


#لتشغيل الكاميرا أخذ صورة أو تسجيل فديو


import cv2

cam=cv2.VideoCapture(0)

while True:
   ret,image=cam.read()
   cv2.imshow("AbdalRahamn",image)
   p=cv2.waitKey(1)
   if p & 0xff ==ord('q'):
      break
   elif p==ord('s'):
      ret,image=cam.read()
      cv2.imwrite("D:\\took.png",image)
      break
       
   
   
   
   











