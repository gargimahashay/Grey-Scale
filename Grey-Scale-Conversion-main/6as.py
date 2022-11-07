
# library used for image processing and computer vision
import cv2
# for reading image from local
img = cv2.imread('mytest.jpg', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)
# user input to change accodingly
scale_percent = int(input("Enter the percent you want to small the image:"))  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
# resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
# resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)

# resize the image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)


print('Resized Dimensions : ', resized.shape)

# for showing the image
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
# releasing all windows
cv2.destroyAllWindows()


# this is the user se input karake then resize kare