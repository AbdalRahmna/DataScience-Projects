# فتح صورة وعرضها وعمل زر لحفظ و أغلاق الصورة

import cv2

img=cv2.imread("images/elephent.png",0)       #0 : الصفر هنا لجعل الصورة بألأبيض وألأسود


cv2.imshow("AbdalRahmn",img)

k=cv2.waitKey(0)
if k == ord("q"):        #27 in ascicode => quit(q) and we can use ord()
    cv2.destroyAllWindows()
elif k == ord("s") :
    cv2.imwrite("D:\\elephent.png",img)
    print("The image is saved")
    cv2.destroyAllWindows()
 


