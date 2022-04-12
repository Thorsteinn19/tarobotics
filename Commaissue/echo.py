import serial

serialport=serial.Serial(port="/dev/ttyS0",baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)


serialport.write(b'hallo')
while 1:
    print(ser.readline().decode('ascii'))
