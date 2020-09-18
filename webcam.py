import cv2
import os

count=0
path = 'C:/project_test'

cam = cv2.VideoCapture(0)
while True:
    retval, frame = cam.read()

    if retval != True:
           raise ValueError("Can't read frame")

    cv2.imwrite(os.path.join(path , str(count)+'.jpg'), frame)
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0: break
    count+=1

cam.release()
cv2.destroyAllWindows()
