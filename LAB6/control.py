import RPi.GPIO as GPIO
from gpiozero import Button
import time,board
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
from arduinoclass import Arduinoread
from simple_pid import PID
i2c=board.I2C()

oled= adafruit_ssd1306.SSD1306_I2C(128,32,i2c,addr=0x3c)
WIDTH = 128
HEIGHT= 31
BORDER = 5
MS1=13
MS2=26
ENABLE=19
DIR=25
STEP=12
Pin1=27
Pin2=22
Button1 = Button(23)
lastpos=None
pid = PID(1,1,1,setpoint = 0)
pid.output_limits = (0,114)
ser = Arduinoread()

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin1,GPIO.OUT)
GPIO.setup(Pin2,GPIO.OUT)
GPIO.setup(MS1,GPIO.OUT)
GPIO.setup(MS2,GPIO.OUT)
GPIO.setup(ENABLE,GPIO.OUT)
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)


GPIO.output(ENABLE,0)
GPIO.output(MS1,0)
GPIO.output(MS2,0)
GPIO.output(DIR,0)

forward= GPIO.PWM(Pin1,100)
backward=GPIO.PWM(Pin2,100)
backward.start(0)
count=1
currentpos = 0
calib = True
try:
    while True:
        time.sleep(1)
        dcmotor = ser.dcmotor
        pid.setpoint = (dcmotor/1023)*114
        rpm = round(60/(ser.pps*10**-6)/700)
        pidout = pid(rpm)
        backward.ChangeDutyCycle(int(pidout*100/114))
        GPIO.output(DIR,0)
        stepper = int(ser.stepper*200/1023)
        degree=round(currentpos*360/200)
        print("Potentiometer DC", dcmotor,"Peotentiometer Stepper",ser.stepper)
        #Fixed dc rotation
        backward.ChangeDutyCycle(int(dcmotor*100/1023))
        # Display image
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)

        font = ImageFont.load_default()

        text = "Deg: {} - RPM:{}".format(degree,rpm)
        (font_width, font_height) = font.getsize(text)
        draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
            text, font=font, fill=255)


        oled.image(image)
        oled.show()
        count += 1

        move = currentpos-stepper
        if move <=0:
            GPIO.output(DIR,0)
        else:
            GPIO.output(DIR,1)        
        if abs(move)>1:
            for i in range(abs(move)):
                GPIO.output(STEP,1)
                time.sleep(0.005)
                GPIO.output(STEP,0)
        currentpos = currentpos - move
        if calib:
            GPIO.output(DIR,1)
            while Button1.is_pressed == False:
                GPIO.output(STEP,1)
                time.sleep(0.005)
                GPIO.output(STEP,0)
            print("Button pressed, this is now home positon")
            time.sleep(1)
            currentpos = 0
            calib = False

except KeyboardInterrupt:

    oled.fill(0)
    oled.show()
    GPIO.cleanup()

