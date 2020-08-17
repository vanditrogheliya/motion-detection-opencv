import cv2
import numpy as np

video = cv2.VideoCapture('motion.avi')

_,frame1 = video.read()
_,frame2 = video.read()
while video.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_TOZERO)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(frame1, contours, -1, (0,255,0),3)
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour)>600:
            cv2.rectangle(frame1, (x, y), (x+w, y+h ), (0,255,0), 3)

    cv2.imshow('original',frame1)
    frame1 = frame2
    _, frame2 = video.read()

    if cv2.waitKey(40) == 27:
        break;

video.release()
cv2.destroyAllWindows()