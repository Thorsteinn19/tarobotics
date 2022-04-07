#!/bin/python3
import cv2
import numpy as np
import sys
import time
from functions.Motor_driver_func import motor_driver
import threading
import simpleaudio as sa

def drive():
    global motor,driving,activate,decodedText
    driving = True
    motor.forward()
    time.sleep(5)
    motor.stop()
    wave_obj = sa.WaveObject.from_wave_file("audio/present.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    while decodedText == "":
        time.sleep(0.1)
    qrcheck=decodedText
    if qrcheck == "valid text":
        wave_obj = sa.WaveObject.from_wave_file("audio/valid.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        motor.right_deg(20)
        time.sleep(2.5)
        motor.forward()
        time.sleep(2)
        motor.stop()
    else:
        for i in range(1,10):
            wave_obj = sa.WaveObject.from_wave_file("audio/invalid.wav")
            play_obj = wave_obj.play()
            motor.right_deg(10)
            play_obj.wait_done()
        motor.stop()

    driving = False
    activate=threading.Thread(target=drive)

def squaredrive():
    global motor,driving,sentry
    while sentry:
        while driving == False:
            motor.forward()
            if driving:
                break
            time.sleep(3)
            if driving:
                break
            motor.right_deg(3)
            if driving:
                break
            time.sleep(1)
            if driving:
                break
            motor.stop()
            if driving:
                break
            time.sleep(2)
            if driving:
                break
            motor.left_deg(3)
            if driving:
                break
            time.sleep(1)
            if driving:
                break
            motor.stop()
            if driving:
                break
            time.sleep(3)
            if driving:
                break
            motor.backwards()
            if driving:
                break
            time.sleep(3)
            if driving:
                break
            motor.stop()

#Fuck this
motor = motor_driver(debug=0)
decodedText=""
driving=False
sentry = False
activate=threading.Thread(target=drive)

scoutpath=threading.Thread(target=squaredrive)
scoutpath.start()

hog = cv2.HOGDescriptor()
driving = False
qr = cv2.QRCodeDetector()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
humancount=0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
#out = cv2.VideoWriter(
#    'output.avi',
#    cv2.VideoWriter_fourcc(*'MJPG'),
#    15.,
#    (640,480))

while(True):
    # Capture frame-by-frame
    time.sleep(0.1)
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
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    decodedText, points, _ = qr.detectAndDecode(frame)
    #print(len(faces),len(weights))
    if len(faces) != 0 or len(weights) !=0:
        if humancount < 2:
            humancount = humancount+1
    else:
        if humancount>0:
            humancount = humancount-1
    if humancount == 2 and driving == False:
        driving=True
        motor.stop()
        activate.start()

    print(humancount, driving)
#     boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
#     for (xA, yA, xB, yB) in boxes:
#         # display the detected boxes in the colour picture
#         cv2.rectangle(frame, (xA, yA), (xB, yB),
#                           (0, 255, 0), 2)

    # Write the output video
    #out.write(frame.astype('uint8'))
    # Display the resulting frame
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
#out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)