import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('/Users/shreyas/Desktop/Face Recognition/data/haarcascade_frontalface_alt2.xml')


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame) #imgshow
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]
        img_item = 'my-img.png'
        cv2.imwrite(img_item, roi_gray)
        
        color = (255,0,0) #BGR
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle (frame, (x,y), (end_cord_x, end_cord_y), color, stroke)
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
