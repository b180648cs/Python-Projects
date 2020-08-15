qfrom cv2 import cv2
import time
a=1
video=cv2.VideoCapture(0)

while True:
    check,frame=video.read()
    print(frame)
    a=a+1
    gray=frame
    face_cascade=cv2.CascadeClassifier("E:\\python projects\\cv2\data\\haarcascade_frontalface_default.xml")
        
    

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

    for x,y,w,h in faces:
        gray=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow("Legend",gray)
       
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()