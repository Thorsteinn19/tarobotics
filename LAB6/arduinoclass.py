from os import read
import threading, serial,time

class Arduinoread():
    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial('/dev/ttyS0',9600,timeout=1)
        self.dcmotor = 0
        self.stepper = 0
        self.pps = 1
        self.dir = 0
        self.readin = ""
        self.threadder()

    def dataread(self):
        while True:
            self.ser.write(bytes("a","utf-8"))
            if self.ser.inWaiting():
                readin = self.ser.readline().decode("utf-8").strip().split()
                self.dcmotor = int(readin[2])
                self.stepper = int(readin[1])
                self.pps = float(readin[0])
                if self.pps == 0:
                    self.pps = 1
                self.dir = int(readin[3])
                

    def threadder(self):
        self.logger = threading.Thread(target=self.dataread)
        
        self.logger.start()
        


