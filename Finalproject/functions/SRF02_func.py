import time
from smbus import SMBus
from adafruit_servokit import ServoKit

class SRF02:

    current_value = 0

    def __init__(self, i2c_bus, i2c_address, servo_kit, servo_number, forward_angle, side_angle):
        self.i2c_bus = i2c_bus
        self.i2c_address = i2c_address
        self.servo_kit = servo_kit
        self.servo_number = servo_number
        self.forward_angle = forward_angle
        self.side_angle = side_angle



    def scan(self, print_bool):
        self.i2c_bus.write_byte_data(self.i2c_address, 0, 0x51)  # Tell sensor to scan in mm

        high = self.i2c_bus.read_byte_data(self.i2c_address, 2)  # Read the high byte of the value
        #print(high) # print the value of High byte

        low = self.i2c_bus.read_byte_data(self.i2c_address, 3)  # Read the low byte of the value
        #print(low) # print the value of low byte

        self.current_value = high * 256 + low

        if(print_bool): # For debugging
            print(self.current_value)

        time.sleep(0.1)  # Sleep for some


    def scan_side(self, print_bool):
        wait_value = 0.5
        self.servo_kit.servo[self.servo_number].angle = self.side_angle
        time.sleep(wait_value)
        self.scan("Side value: {}", print_bool)
        time.sleep(wait_value)
        self.servo_kit.servo[self.servo_number].angle = self.forward_angle
        time.sleep(wait_value)

        if(print_bool): # For debugging
            print(self.current_value)


    def scan_custom(self, angle, print_bool):
        wait_value = 0.5
        self.servo_kit.servo[self.servo_number].angle = angle
        time.sleep(wait_value)
        self.scan(print_bool)
        time.sleep(wait_value)
        self.servo_kit.servo[self.servo_number].angle = self.forward_angle
        time.sleep(wait_value)