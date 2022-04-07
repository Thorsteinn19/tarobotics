from os import read
import threading, serial,time

class Arduinoread():
    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial('/dev/ttyS0',9600,timeout=1)
        self.readin = ""
        self.threadder()

    def dataread(self):
        while True:
            self.ser.write(bytes("a","utf-8"))
            if self.ser.inWaiting():
                self.readin = self.ser.readline().decode("utf-8")
            
                

    def threadder(self):
        self.logger = threading.Thread(target=self.dataread)
        
        self.logger.start()
        


