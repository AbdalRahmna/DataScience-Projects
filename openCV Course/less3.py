#عرض أبعاد الصورة والبكسلات(imageinfo)

import cv2
img=cv2.imread("images/rabit.png")

pixels = img.size                    #    لجلب حجم الصورة أى عدد البكسلات
dimenions = img.shape                #   لجلب أبعاد الصورة
print("Number of pixels=",pixels)
print("dimensions=",dimenions)

cv2.imshow("AbdalRahman",img)

p=cv2.waitKey(0)


           