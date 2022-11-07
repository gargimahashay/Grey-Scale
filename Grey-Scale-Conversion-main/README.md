# Grey-Scale Conversion

## Discription
Here we convert colorful images or video and change their dimensions too from image processing.
##  Library used

**OpenCV-Python**: OpenCV is an excellent tool for image processing and computer vision tasks. It is an open-source library that performs functions like face detection, objection tracking, landmark detection, and much more.


**Matplotlib**: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy and hard things possible, interactive figures that can zoom, pan, update, visual style and layout.

## Execution Steps:

1.	We use imread method to read the image from the system.
2.	We use Imshow method to show the image.
3.	We use imwrite method to write or create here we used it to create  a new image.
4.	We use videocapture method to take input the video and give a parameter “0” that give access to open webcam and start recording.
5.	We use cvtColor method to convert the color here we used it to convert from colorful to gey by using BGR2GREY.
6.	DestroyAllWindows used to release all window after performing  the task and free up the memory.

