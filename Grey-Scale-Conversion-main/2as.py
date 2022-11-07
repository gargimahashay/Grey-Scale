# This is for the creating copy of an image

# library used for image processing and computer vision
import cv2
# for reading image
img = cv2.imread('mytest.jpg', 0)
print(img)
# display the image
cv2.imshow('imaksh', img)
cv2.waitKey(5000)

cv2.destroyAllWindows()


cv2.imwrite("mt_copy.jpg", img)


