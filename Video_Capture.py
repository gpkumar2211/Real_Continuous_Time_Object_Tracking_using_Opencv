import cv2
from trackers import *

cap = cv2.VideoCapture(r"D:\Full Stack Data Science AI & ML\ClassNotes\Feb 20_Color_Detection\object_tracking\object_tracking\highway.mp4")

while True:
    ret,frame = cap.read()
    cv2.imshow("Frame",frame)
    key = cv2.waitKeyEx(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()