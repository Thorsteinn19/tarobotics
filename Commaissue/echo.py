import serial

serialport=serial.Serial(port="/dev/ttyS0",baudrate=9600, timeout=1)


serialport.write(bytes("a","utf-8"))
while 1:
    if serialport.inWaiting():
        inputstring=ser.readline().decode('utf-8')
        print(inputstring)
