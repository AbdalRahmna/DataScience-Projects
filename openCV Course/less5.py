#تغيير نظام ألألوان للصورة الى الرمادى

import cv2
img=cv2.imread("images/bird.png")

gray=cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

cv2.imshow("AbdalRahmn",gray)
cv2.waitKey(0)