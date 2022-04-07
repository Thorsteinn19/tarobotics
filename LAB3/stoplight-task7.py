from gpiozero import LED
from time import sleep

red = LED(6)
amber = LED(13)
green = LED(5)

while True:
    red.on()
    print('Red light is on: [100]')
    sleep(4)
    amber.on()
    print('Yellow and red light is on: [110]')
    sleep(1)
    red.off()
    amber.off()
    green.on()
    print('Green light is on: [001]')
    sleep(5)
    green.off()
    amber.on()
    print('Yellow light is on: [010]')
    sleep(1)
    amber.off()
