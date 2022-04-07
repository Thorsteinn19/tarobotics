#!/usr/bin/env python
from pyowm.weatherapi25 import weather
from std_msgs.msg import Int32
import rospy,serial,threading,time

weathertemp = 0
potentval = 0
humidity = 0

def listener():
    rospy.init_node('controlsub',anonymous=True)
    while True:
        rospy.Subscriber('weather', Int32, changeweather)
        rospy.Subscriber('humid',Int32,changehumid)
        rospy.Suvscriber('arduinor',Int32,changepotent)
def changehumid(data):
    global humidity
    humidity = int(data.data)
def changeweather(data):
    global weathertemp
    
    weathertemp = int(data.data)

def changepotent(data):
    global potentval
    potentval = data.data
    
def serialwriter():
    global weathertemp
    ser = serial.Serial('/dev/ttyUSB15',9600,timeout=1)
    while True:
        ser.write(bytes(str(weathertemp)+str(humidity),"utf-8"))
        ser.flush()
        rospy.loginfo("Humidity: "+str(humidity)+" - Temp: "+str(weathertemp) + "Potentiometer:" + str(potentval))
        time.sleep(1)
            
if __name__ == '__main__':
    try:
        w = threading.Thread(target=serialwriter)
        w.start()
        listener()
    except rospy.ROSInterruptException: pass