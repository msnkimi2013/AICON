import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

myColorFinder = ColorFinder(True)

hsvVals = {'hmin': 8, 'smin': 124, 'vmin': 24, 'hmax': 255, 'vmax': 255}

#  spark


#           {'hmin': 5, 'smin': 0, 'vmin': 223, 'hmax': 57, 'smax': 91, 'vmax': 255}
#           {'hmin': 6, 'smin': 72, 'vmin': 189, 'hmax': 26, 'smax': 154, 'vmax': 255}
#           {'hmin': 0, 'smin': 31, 'vmin': 203, 'hmax': 35, 'smax': 137, 'vmax': 255}
#           {'hmin': 21, 'smin': 78, 'vmin': 189, 'hmax': 34, 'smax': 130, 'vmax': 255}


# video import or webcam
# cap = cv2.VideoCapture()



while True:
    # Grab the image
    # image
    # img = cv2.imread('./construction_fire.jpeg')
    img = cv2.imread('./test_images/2s.jpg')





    # Specify the new dimensions (width, height)
    new_dimensions = (700, 500)

    # Resize the image
    img = cv2.resize(img, new_dimensions)





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
    cv2.imshow("Mask", mask)

    cv2.waitKey(50)