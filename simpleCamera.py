import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

face_id = input('\n enter user id end press <return> ==> ')
print("\n [INFO] initializing face capture. look the camera and wait ...")
count = 0

cap = cv2.VideoCapture(0) 
cap.set(3, 640)
cap.set(4, 480)
while(True):
    ret, image = cap.read()
    image = cv2.flip(image, -1)             # 상하반전 0 -> 상하좌우 1 -> default
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20,20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x ,y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite("facedetection/dataset/User." + str(face_id)+'.'+str(count)+'.jpg', gray[y:y+h, x:x+w])
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = image[y:y+h, x:x+w]

        #eyes = eyeCascade.detectMultiScale(
        #    roi_gray,
        #    scaleFactor = 1.5,
        #    minNeighbors = 10,
        #    minSize = (5, 5)
        #)

        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('video', image)
    #cv2.imshow('frame', frame)
    #cv2.imshow('gray', gray)


    k = cv2.waitKey(30) & 0xff
    if k == 27:                             # press 'ESC' to quit
        break
    elif count >= 30:
        break

cap.release()
cv2.destroyAllWindows()