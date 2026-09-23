import cv2 as cv
import numpy as np

img = cv.imread('pictures/cats2.jpg')
cv.imshow('Cats',img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', grey)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny edges', canny)

contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countout(s) found')

 
cv.waitKey(0)