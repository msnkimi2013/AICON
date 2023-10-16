import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

myColorFinder = ColorFinder(True)

hsvVals = {'hmin': 8, 'smin': 124, 'vmin': 24, 'hmax': 255, 'vmax': 255}


# video import or webcam
# cap = cv2.VideoCapture()



while True:
    # Grab the image
    # image
    img = cv2.imread('./construction_fire.jpeg')
    # video
    # success, img = cap.read()

    # cropping the image
    # img = img[0:900, :]

    # Find the color
    imgColor, mask = myColorFinder.update(img, hsvVals)




    # Display
    img = cv2.resize(img, (0,0), None, 2, 2 )
    imgColor = cv2.resize(imgColor, (0, 0), None, 2, 2)
    cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgColor)
    cv2.waitKey(50)