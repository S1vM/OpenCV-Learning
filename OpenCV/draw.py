import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#paint the image of a certain colour
blank[:] = 0,0,255
cv.imshow('Green', blank)

#Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,250,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#Draw a circle
cv.circle(blank, (250,250), 40, (0,0,255))
cv.imshow('Circle', blank)

#Draw a line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow('Line', blank)

#Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)