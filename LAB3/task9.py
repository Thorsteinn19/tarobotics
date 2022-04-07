from gpiozero import LED, Button
from time import sleep
from signal import pause
button = Button(12)
button2 = Button(16)
red = LED(6)
yellow = LED(13)
green = LED(5)
pgreen = LED(18)
pred = LED(24)
choice = input('E or A ? ').lower()

def carlightcycle():
    if choice == 'e':
        
        red.on()
        sleep(2)
        yellow.on()
        sleep(2)
        red.off()
        yellow.off()
        green.on()
        sleep(3)
        green.off()
        yellow.on()
        sleep(2)
        yellow.off()
        red.on()

    elif choice == 'a':

        red.off()
        green.on()
        sleep(2)
        green.off()
        yellow.on()
        sleep(2)
        yellow.off()
        red.on()

def pedestriancycle():
    pred.off()
    pgreen.on()
    sleep(4)
    pgreen.off()
    pred.on()

red.on()
pred.on()
button.when_pressed = carlightcycle
button2.when_pressed = pedestriancycle
pause()
