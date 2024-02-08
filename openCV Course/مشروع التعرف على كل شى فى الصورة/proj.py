import cv2
img =cv2.imread("images\employee.png")

classnames=[]  #  list
classfile = 'files/thing.names'
with open (classfile,'rt') as f :                        # classfile يعنى انادى على  f بمجرد أن أنادى على حرف   
    classnames=f.read().rstrip('\n').split('\n')             #  rstrip('\n):لقراءة السطر ألأول ثم ألأنتقال على السطر الى بعضة    
                                                                # split('\n'):لقراءة السطر الذى يلية
#print(classnames)

p ='files/frozen_inference_graph.pb'
v ='files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

net=cv2.dnn_DetectionModel(p,v)                 #  لعمل كشف  و فحص على الملفين
net.setInputSize(320,230)                       #           العرض وألأرتفاع     
net.setInputScale(1.0/127.5)                    #      القياس
net.setInputMean((127.5,127.5,127.5))           #   المتوسط
net.setInputSwapRB(True)                       #            نظام ألألوان

classIds , confs , bbox =net.detect(img,confThreshold=0.5)  # (0-1)دقة الفحص فى الصورة  

#print(classIds,bbox)

for classId ,confidence , box in zip(classIds.flatten(),confs.flatten(),bbox):
    cv2.rectangle(img,box,color=(0,225,0),thickness=3)
    cv2.putText(img,classnames[classId-1],
                (box[0]+10,box[1]+20),
                cv2.FONT_HERSHEY_COMPLEX,1,
                (0,0,225),thickness=2)


cv2.imshow("AbdalRahaman",img)
cv2.waitKey(0)