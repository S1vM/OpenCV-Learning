import cv2 as cv

img = cv.imread('pictures/cats2.jpg')
cv.imshow('Cats', img)

#Averaging blur
average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

#Gaussian blur
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian blur', gauss)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

#Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)