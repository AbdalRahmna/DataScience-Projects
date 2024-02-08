#   عرض الفديوهات فى البرنامج وزر ألأغلاق
import cv2 
cam=cv2.VideoCapture("vedios\أجمل قاعة أفراح في العالم.mp4")
while (True) :
    ret,frame=cam.read()
    cv2.imshow("Abdalrahman",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):   #1: as its viedio   # 0xff=>Esc(Q)
            break
 









