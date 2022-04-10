import math
from time import sleep
import getch
from Finalproject.functions.Motor_driver_func import motor_driver
from adafruit_servokit import ServoKit  # Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=8) # 8 servo connectors on the robot
kit.frequency = 50
kit.servo[0].set_pulse_width_range(500,2500)
kit.servo[1].set_pulse_width_range(620,2250)

motors = motor_driver(debug=0)
try:
    while 1:
        motors.forward()
        kit.servo[0].angle = 180  # Servo in slot 1 on robot
        kit.servo[1].angle = 180
        sleep(1)
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
        motors.backwards()
        sleep(1)
        motors.right()
        sleep(2)
        motors.left()
        sleep(2)
except:
    motors.stop()
    exit(0)
