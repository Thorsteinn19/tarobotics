from gpiozero import LED
from time import sleep


red = LED(22)
yellow = LED(27)
green = LED(17)
choice = input('E or A ? ').lower()
if choice == 'e':
    while True:
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
elif choice == 'a':
    while True:
        red.on()
        sleep(2)
        red.off()
        green.on()
        sleep(2)
        green.off()
        yellow.on()
        sleep(2)
        yellow.off()
