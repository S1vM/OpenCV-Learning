import cv2 as cv
import numpy as np

img = cv.imread('pictures/group 1.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_Casacade = cv.CascadeClassifier('haar face.xml')

face_rect = haar_Casacade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print(len(face_rect))

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face(s)', img)

cv.waitKey(0)