import cv2
from playsound import playsound

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')  #لأستدعاء خوارزمية التعرف على لنار
cap = cv2.VideoCapture(0)
while (True) :
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire=fire_cascade.detectMultiScale(frame,1.2,5)               #detect_MultiScale:تستخدم لتحديد الأمااكن المختلة لوجود الحرائق            
                                                                 # ودقة الكاميرا وعدد أنواع الحرائق frame  وتأخذ قيمة  
    for (x,y,w,h) in fire :
      roi_gray=gray[y:y+h , x:x+w] 
      roi_color=frame[y:y+h ,x:x+w]
      print("The fire is detected")
      playsound("audio.mp3")
    
    cv2.imshow("AbdalRahman[Fire_detection]",frame)
    p=cv2.waitKey(1)
    if p & 0xff ==ord('q'):
       break












