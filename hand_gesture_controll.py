#!/usr/bin/env python

import cv2 as cv
import numpy as np

print('Choose camera that you use: ')
print('USB camera (1)')
print('Build in camera (0)')
camera = input()

def trackbar():
  pass

#to convert color space from BGR to HSV
def RGBtoHSV(frame, b1, g1, r1, b2, g2, r2):
  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  lower_blue = np.array([b1,g1,r1])
  upper_blue = np.array([b2,g2,r2])
  mask = cv.inRange(hsv, lower_blue, upper_blue)
  res = cv.bitwise_and(frame,frame, mask= mask)
  return res

if camera == 1:
  cap = cv.VideoCapture(1)
else:
  cap = cv.VideoCapture(0)
print('Press Esc to quit the program')

while True:
  ret, frame = cap.read()
  res = RGBtoHSV(frame)
  cv.imshow('Converted', res)
  cv.imshow("Original", frame)
  key = cv.waitKey(1)
  if key == 27:
    break
cap.release()
cv.destroyAllWindows()
