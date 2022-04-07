import serial
from servoclass import Servomotor
from csvlooger import CSVLogger

datalogger = CSVLogger("Angles.csv")


ser = serial.Serial('/dev/ttyS0',9600,timeout=1)
ser.flush()

servo = Servomotor(18)
servo2 = Servomotor(17)

try:
    while True:
        ser.write(1)
        if ser.inWaiting():
            photor = int(ser.readline().decode("utf-8").strip())
            potent = int(ser.readline().decode("utf-8").strip())
            angle2= int(potent*180/1023)
            angle1= int(photor*180/1023)

            servo.changeangle(angle2)
            if photor > 800:
                servo2.changeangle(180)
            else:
                servo2.changeangle(0)
            datalogger.setdata(photor,potent)
            #print("Datavalues: Photoresistor ",photor," Potentiometer ",potent)
            
except KeyboardInterrupt:
    quit()


