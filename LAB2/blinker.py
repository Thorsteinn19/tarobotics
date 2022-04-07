import time

#filedir="/sys/class/leds/led0/brightness"
filedir="C:/Users/stein/Documents/LAB2/mix.txt"
fopen=open(filedir,"w")
fopen.write("0")
fopen.close()

herts=int(input("How many blinks a sec do you want?"))
totaltime= int(input("How many seconds do want to run?"))
rate=1/herts
t=0
while t<totaltime:
    fopen=open(filedir,"w")
    fopen.write("255") # kveikja
    time.sleep(rate/2)
    fopen.close()
#
    fwriter=open(filedir,"w")
    fwriter.write("0") # slökkva
    time.sleep(rate/2)
    fwriter.close()
    t+=rate

ff=open(filedir,"w")
ff.write("255")
ff.close()
