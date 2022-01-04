import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(mask, rectangle)
cv.imshow('WeirdShape', weird_shape)

cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked Image', masked)

cv.waitKey(0)