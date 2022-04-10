import serial
from time import sleep

class motor_driver:
    
    def __init__(self, port_name = "/dev/ttyS0", baudrate = 38400, debug = 0):
        self.debug = debug
        self.connect(port_name, baudrate)
        self.print_debug("Serial connected")

    # b'\x01' => Motor 1 stops
    # b'\x02' => Motor 1 drives forward
    # b'\x03' => Motor 1 drives backwards
    # b'\x04' => Motor 2 stops
    # b'\x05' => Motor 2 drives forward
    # b'\x06' => Motor 2 drives backwards

    def connect(self, port_name, baud):
        self.serialPort = serial.Serial(port = port_name, baudrate=baud, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE) # connecting to the serial port

    def disconnect(self):
        self.serialPort.close()  # closing the serial port

    def print_debug(self, debug_message):
        if(self.debug):
            print(debug_message)

    def forward(self):
        self.serialPort.write(b'\x02')  # motor 1 drives forward
        sleep(0.1)
        self.serialPort.write(b'\x06')  # motor 2 drives backwards
        sleep(0.1)

        self.print_debug("Drive forward")
        
    def backwards(self):
        self.serialPort.write(b'\x03')  # motor 1 drives backwards
        sleep(0.1)
        self.serialPort.write(b'\x05')  # motor 2 drives forward
        sleep(0.1)

        self.print_debug("Drive backwards")

    def right(self):
        self.serialPort.write(b'\x02')  # motor 1 drives forward
        sleep(0.1)
        self.serialPort.write(b'\x05')  # motor 2 drives forward
        sleep(0.1)

        self.print_debug("Drive right")

    def left(self):
        self.serialPort.write(b'\x03')  # motor 1 drives backwards
        sleep(0.1)
        self.serialPort.write(b'\x06')  # motor 2 drives backwards
        sleep(0.1)

        self.print_debug("Drive left")

    def right_deg(self, deg):
        self.right()
        deg2 = int(deg/5)
        for i in range(deg2):
            sleep(0.08) # hreyfist um 5 deg í einu

        self.print_debug("Drive right")

    def left_deg(self, deg):
        self.left()
        deg2 = int(deg / 5)
        for i in range(deg2):
            sleep(0.08)  # hreyfist um 5 deg í einu

        self.print_debug("Drive left")

    def stop(self):
        self.serialPort.write(b'\x01')  # motor 1 drives stop
        sleep(0.1)
        self.serialPort.write(b'\x04')  # motor 2 drives stop
        sleep(0.1)

        self.print_debug("Drive stops")


