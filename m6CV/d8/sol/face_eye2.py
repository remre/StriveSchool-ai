import cv2
import numpy as np 


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)

    for (x,y,w,h) in faces:
        p1 = (x,y)
        p2 = (x+w, y+h)
        cv2.rectangle(img,p1,p2,(0,0,255),3)
        roi_gray = gray_frame[p1[1]:p2[1],p1[0]:p2[0]]
        roi_color = img[p1[1]:p2[1],p1[0]:p2[0]]
        
        eyes = eye_classifier.detectMultiScale(roi_gray)
        for (xe,ye,we,he) in eyes:
           p1e = (xe,ye)
           p2e = (xe+we, ye+he)
           cv2.rectangle(roi_color,p1e,p2e,(255,0,0),3)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()