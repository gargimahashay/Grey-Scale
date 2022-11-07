# This is the code for comverting an image in grey scale

# library used for image processing and computer vision
import cv2
# for reading image
img = cv2.imread('mytest.jpg', 0)
print(img)
# for display image
cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

