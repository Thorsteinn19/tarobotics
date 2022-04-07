#!/usr/bin/env python

import pyowm,time,rospy,threading
from std_msgs.msg import Int32

temprature = 0
humidity = 0

def talker():
    global temprature
    pub = rospy.Publisher('weather', Int32 ,queue_size=10)
    pub2 = rospy.Publisher('humid', Int32,queue_size=10)
    rospy.init_node('weatherc', anonymous=True)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        weather = temprature
        pub.publish(weather)
        pub2.publish(humidity)
        rospy.loginfo("Temprature is %s",weather)
        r.sleep()
            

def weathercommand():
    global temprature, humidity
    APIKEY='5b22170cf9d57041c6a4ef88d5009089'     
    while True:
        OpenWMap=pyowm.OWM(APIKEY)                   
        Weather=OpenWMap.weather_manager()
        location = Weather.weather_at_place('Reykjavik,IS')
        Data=location.weather                  
        temprature = int(round(Data.temperature("kelvin")["temp"]))
        humidity = int(Data.humidity)
        time.sleep(30)
        


if __name__ == '__main__':
    try:
        w = threading.Thread(target=weathercommand)
        w.start()
        talker()
    except rospy.ROSInterruptException: pass

