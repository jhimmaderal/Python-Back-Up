import cv2 as cv


# Image
img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img) # Name of window, varialble


# Video
#capture = cv.VideoCapture('Resources/Videos/dog.mp4')
#
#while True:
#  isTrue, frame = capture.read()
#  cv.imshow('Video', frame)
#
#  if cv.waitKey(20) & 0xFF ==ord('d'):
#    break
#
#capture.release()
#cv.destroyAllWindows()

cv.waitKey(0)