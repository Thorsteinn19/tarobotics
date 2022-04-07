#!/usr/bin/env python
import serial,threading,rospy
from std_msgs.msg import Int32



data_sensor = 0

def serialreader():
    global data_sensor
    ser = serial.Serial("/dev/ttyUSB1")

    while True:
        data = ser.readline()
        data_sensor = int(data.decode("utf-8"))
        print(data_sensor)


def talker():
    global data_sensor
    pub = rospy.Publisher('arduino', Int32 ,queue_size=10)
    rospy.init_node('arduinor', anonymous=True)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(data_sensor)
        r.sleep()    

if __name__ == '__main__':
    try:
        w = threading.Thread(target=serialreader)
        w.start()
        talker()
    except rospy.ROSInterruptException: pass