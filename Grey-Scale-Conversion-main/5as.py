# this is the conversion or resizing of all types

# library used for image processing and computer vision
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("mytest.jpg", 1)
# Loading the image

# resize method used to resize the image and chnging its x, y dimensions
half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
                          interpolation=cv2.INTER_NEAREST)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()


