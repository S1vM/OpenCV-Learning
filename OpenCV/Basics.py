import cv2 as cv

img = cv.imread('pictures/london.jpg')
cv.imshow('London',img)

#Converting to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilate image
dilated = cv.dilate(canny, (7,7), iterations=5)
cv.imshow('Dilated', dilated)

#Erode image
eroded = cv.erode(dilated, (7,7), iterations=5)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)