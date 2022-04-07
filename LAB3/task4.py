from gpiozero import Button, LED
from signal import pause

led = LED('4')
button = Button('18')

def led_on():
    print('Button is pressed')
    led.on()

def led_off():
    print('Button is not pressed')
    led.off()


button.when_pressed = led_on

button.when_released = led_off

pause()
