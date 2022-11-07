# This is the code for converting grey scale of video

# This is for the creating copy of an image
import cv2
# take input videocapture
source = cv2.VideoCapture('nature.mp4')
# here we divide the video into frames as we know it is a set of images.
# for reading or extracting the image from video
while True:
    ret, img = source.read()
    # cvtColor used to convert color here we change the video into grey
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # for display
    cv2.imshow("Live", gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
# for releasing all window
cv2.destroyAllWindows()
source.release()

