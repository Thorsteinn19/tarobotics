import serial,time

ser = serial.Serial("/dev/ttyUSB0")

while True:
    data = ser.readline()
    data_sensor = data.decode("utf-8")
    print(data_sensor)
    time.sleep(0.1)