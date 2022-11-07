# this is for the video resizing and quality

# library used for image processing and computer vision
import cv2
# for recording the video
cap = cv2.VideoCapture(0)

# several functions for editing in image according pixels
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

