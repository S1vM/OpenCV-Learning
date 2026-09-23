import cv2 as cv
import numpy as np

img = cv.imread('pictures/london.jpg')

cv.imshow('London', img)

#Transaltion
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]]) 
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# x --> right
# -y --> up
# y --> down


translated = translate(img, 100, 100)
cv.imshow('translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint == None:
        rotPoint =(width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height) 

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Flipping

# 0 --> x-axis
# 1 --> y-axis
# -1 --> both x and y axis

flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)

