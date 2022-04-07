import argparse
import cv2
from apriltag import Detector
#import apriltag
import os
import multiprocessing


def apscan(image):
    
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    at_detector = Detector()
    tags = at_detector.detect(gray)
    for tag in tags:
        fam = tag.tag_family.decode("utf-8")
        (posx,posy)=(int(tag.center[0]),int(tag.center[1]))
        taggid = tag.tag_id
        print("Family",fam,"\nPosition: X:",posx,"Y:",posy,"\nID",taggid)
    if len(tags) == 0:
        print("No apriltag on the image")


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
arguments = vars(ap.parse_args())
apimage = cv2.imread(os.path.join(os.getcwd(),arguments["image"]))

proc = multiprocessing.Process(target=apscan,args=(apimage,))
proc.start()
proc.join(timeout=2)
proc.terminate()