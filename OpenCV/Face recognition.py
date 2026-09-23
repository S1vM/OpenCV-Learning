import numpy as np
import cv2 as cv

haar_Casacade = cv.CascadeClassifier('haar face.xml')

people = ['Ben Affleck', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.read('face_trained.yml')

img = cv.imread(r'/Users/murugan/Desktop/OpenCV/Faces/Ben Affleck/9.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

face_rect = haar_Casacade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in face_rect:
    face_region = gray[y:y+h, x:x+w]

    label,confidence = face_recogniser.predict(face_region)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)