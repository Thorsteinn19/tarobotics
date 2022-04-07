from gpiozero import Button, LED
from signal import pause
from time import sleep
import threading
button1 = Button(12)
button2 = Button(16)
led1=LED(18)
led2=LED(24)

class ledthread(threading

def button1thread(button):
    print("active")
    while True:
        button.when_pressed = onled1
        pause()
#    button.when_released = offled1
    
def button2thread(button):
    print("active")
    while True:
        button.when_pressed = onled2
        pause()
#    button2.when_released = offled2
    

def onled1():
    print("Button 1  is pressed")
    for _ in range(1,10):
        led1.on()
        sleep(0.1)
        led1.off()
        sleep(0.1)


def onled2():
    print("Button 2 is pressed")
    for _ in range(1,10):
        led2.on()
        sleep(0.1)
        led2.off()
        sleep(0.1)


def main():
    thread1= threading.Thread(target=button1thread,)
    thread2= threading.Thread(target=button2thread)
    thread1.start()
    thread2.start()
    thread2.join()
    thread1.join()


#if __name__ == '__main__':
#    Process(target=button1thread).start()
#    Process(target=button2thread).start()
#namebut.is_pressed = pressedbutton
#namebut.when_released = releasedbutton
main()
