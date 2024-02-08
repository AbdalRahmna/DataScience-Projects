#تغيير حجم الصورة ةالنافذة 

import cv2

img=cv2.imread("images/betreq.png")
new_img=cv2.resize(img,(500,500))

cv2.imshow("AbdalRahman",new_img)
cv2.rectangle(new_img,(200,50),(300,100),(0,225,0),5)
cv2.putText(new_img,"Face",(250,120),cv2.FONT_HERSHEY_COMPLEX,1,(225,0,0),2)
p=cv2.waitKey(0)

if p ==27 :
    cv2.destroyAllWindows()
elif p==ord('s'):
    cv2.imwrite("photo.png",new_img)
    cv2.destroyAllWindows()    