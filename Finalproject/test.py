import cv2
import numpy as np
import sys
import time

hog = cv2.HOGDescriptor()
driving = False
qr = cv2.QRCodeDetector()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
humancount=0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

while(True):
    # Capture frame-by-frame
    #time.sleep(0.1)
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
     # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    decodedText, points, _ = qr.detectAndDecode(frame)
    #print(decodedText)
    #print(len(faces),len(weights))
    # if len(faces) != 0 or len(weights) !=0:
    #     if humancount < 1:
    #         humancount = humancount+1
    # else:
    #     if humancount>0:
    #         humancount = humancount-1
    # if humancount == 1 and driving == False:
    #     activate.start()
    #print(humancount)
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
    #Write the output video 
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 
            decodedText, 
            (50, 50), 
            font, 1, 
            (0, 255, 255), 
            2, 
            cv2.LINE_4)
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)