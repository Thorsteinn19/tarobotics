from gpiozero import Button, LED
from signal import pause
from time import sleep
import threading

class Ledbutton(threading.Thread):

    def __init__(self,ledpin,button):
        threading.Thread.__init__(self)
        self.buttonnum=button
        self.ledpin=ledpin
        self.led=LED(ledpin)

    def blink(self):
        pin = threading.Thread(target=self.__blinker, args=((self.led,self.buttonnum)))
        pin.start()

    def __blinker(self,led,buttonpin):
        print("Button " +str(buttonpin)+" is pressed")
        for _ in range(1,10):
            led.on()
            sleep(0.1)
            led.off()
            sleep(0.1)

def blink(blinker):
    blinker.blink()

blinker1= Ledbutton(24,1)
blinker2= Ledbutton(18,2)
button1= Button(12)
button2 = Button(16)
button1.when_pressed =blinker1.blink
button2.when_pressed =blinker2.blink
pause()
