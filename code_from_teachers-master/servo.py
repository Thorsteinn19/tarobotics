import time
from adafruit_servokit import ServoKit  # Set channels to the number of servo channels on your kit.
kit = ServoKit(channels=8) # 8 servo connectors on the robot
kit.frequency = 50
kit.servo[0].set_pulse_width_range(500,2500)
kit.servo[1].set_pulse_width_range(620,2250)
while 1:
    kit.servo[0].angle = 180  # Servo in slot 1 on robot
    kit.servo[1].angle = 180
    time.sleep(1)
    kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    time.sleep(1)