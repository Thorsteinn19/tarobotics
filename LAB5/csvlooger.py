import time, csv, threading, datetime, os

class CSVLogger():
    def __init__(self,filename):
        threading.Thread.__init__(self)
        self.data = "Potentiometer"
        self.data2 = "Photoresistor"
        self.filename = filename
        self.f= open(self.filename,"w")
        self.f.close()
        self.threadder()
        
    def writing(self):
        f=open(self.filename,"a")
        writer = csv.writer(f)
        writer.writerow([self.data,self.data2,datetime.datetime.now()])
        f.close()
        print("Data logged: ", self.data,self.data2)
    def schedulerinn(self,timer):
        while True:
            self.writing()
            time.sleep(timer)
    def gitter(self,timer):
        while True:
            os.system("git add {}".format(self.filename))
            os.system('git commit -m "Autologing"')
            os.system('git push')
            time.sleep(timer)
            
    def threadder(self):
        self.logger = threading.Thread(target=self.schedulerinn,args=(10,))
        self.logger.start()
        self.git = threading.Thread(target=self.gitter,args=(300,))
        self.git.start()
    def setdata(self,data,data2):
        self.data= data
        self.data2 = data2
