from gpiozero import Button, LEDBoard, PWMLED
from signal import pause
from time import sleep
from smbus2 import SMBus

class PWMLEDboard(object):

    def __init__(self,ledpins,buttonpin,switchpin,initstate):
        self.index = initstate
        self.numled = len(ledpins)
        self.offstate = self.createoff()
        self.dirbool = True
        self.runbool = True
        self.button= Button(buttonpin)
        self.switcher = Button(switchpin)
        self.ledpin=ledpins
        self.led=LEDBoard(ledpins[0],ledpins[1],ledpins[2],ledpins[3],ledpins[4], pwm=True)
        self.state = self.createnewstate()
        self.led.value = self.state
        self.acceleration = accel()


    def stop_lights(self):
        self.runbool = not self.runbool
        while True:
            print("You stopped on LED number ", self.index+1)
            ask = input("Do you want to continue (y/n): ").lower()
            if ask == "y":
                self.runbool = True
                break
            elif ask == "n":
                quit()
            else:
                print("invalid input")

    def createoff(self):
        zerolist=[]
        for _ in range(self.numled):
            zerolist.append(0)
        return tuple(zerolist)

    
    def larsen(self):
        
        if self.switcher.is_pressed:
            if self.runbool:
                xtilt=self.acceleration.accelread()
                
                if -100 < xtilt and xtilt < 100:
                    if self.index == self.numled-1 or self.index == 0:
                        self.dirbool = not self.dirbool
                    self.state = self.createnewstate()
                    self.index = self.state.index(1)
                    self.led.value = self.state

                    sleep(0.2)
                elif xtilt < -100:
                    
                    if self.index == self.numled-1:
                        pass
                    else:
                        self.dirbool = True
                        self.state = self.createnewstate()
                        self.index = self.state.index(1)
                        self.led.value = self.state
                        sleep(0.2)
                else:
                    
                    if self.index == 0:
                        pass
                    else:
                        self.dirbool = False
                        self.state = self.createnewstate()
                        self.index = self.state.index(1)
                        self.led.value = self.state
                        sleep(0.2)
        else:
            self.led.value = self.offstate

    def createnewstate(self):
        returnvalue = []

        for i in range(self.numled):
            if self.dirbool:
                if i+1 == self.index:
                    returnvalue.append(0)
                elif i-1 == self.index:
                    returnvalue.append(1)

                elif i == self.index:
                    returnvalue.append(0.25)
                elif i-2 == self.index:
                    returnvalue.append(0.25)
                else:
                    returnvalue.append(0)

            else:
                if i+1 == self.index:
                    returnvalue.append(1)
                elif i-1 == self.index:
                    returnvalue.append(0)
                elif i == self.index:
                    returnvalue.append(0.25)
                elif i+2 == self.index:
                    returnvalue.append(0.25)
                else:
                    returnvalue.append(0)  

        return tuple(returnvalue)


class accel(object):
    
    def __init__(self):
        self.bus= SMBus(1)
        self.bus.write_byte_data(0x53, 0x2C, 0x0A)
        self.bus.write_byte_data(0x53, 0x2D, 0x08)

    def accelread(self):
        maindata = self.bus.read_byte_data(0x53, 0x33)
        #print("X1", format(maindata, '#010b'))
        higherdata = self.bus.read_byte_data(0x53,0x32)

#        print("X0",format(higherdata,'#010b'))
        x01 = ((maindata & 0x03) * 256) + higherdata
        if x01 > 511 :
	        x01 -= 1024
        return x01
