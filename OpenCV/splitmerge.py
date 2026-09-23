import cv2 as cv
import numpy as np

img = cv.imread('pictures/london.jpg')
cv.imshow('London', img)

b,g,r = cv.split(img)


blank = np.zeros(img.shape[:2], dtype='uint8', )
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Green', green)
cv.imshow('Red', red)

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#Merging color chanels
merged = cv.merge([b, g, r])
cv.imshow('merged', merged)

cv.waitKey(0)