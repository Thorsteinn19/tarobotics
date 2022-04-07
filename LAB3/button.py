from gpiozero import Button
from signal import pause 

def button_pressed():
    print('Button is pressed')

def button_released():
    print('Button is released')

button = Button(25)

button.when_pressed = button_pressed

button.when_released = button_released

pause()
