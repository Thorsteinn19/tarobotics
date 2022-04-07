import time
import os
#filedir="/sys/class/leds/led0/brightness"
filedir="C:/Users/stein/Documents/LAB2/mix.txt"
fopen=open(filedir,"w")
fopen.write("0")
fopen.close()

herts=int(input("How many blinks a sec do you want?"))
if herts < 200 | herts!=0:
    os.system('cd /sys/class/leds/led0; sudo sh -c "echo timer > trigger"')

else:
    os.system('cd /sys/class/leds/led0; sudo sh -c "echo none > trigger"')

if herts == 0:
    fzero=open(filedir,"w")
    fzero.write("0")
    fzero.close()

elif herts > 200:
    fzero=open(filedir,"w")
    fzero.write("1")
    fzero.close()

else:
    rate=(1/herts)*1000
    print(rate/2)
    ondir="/sys/class/leds/led0/delay_on"

    fon=open(ondir,"w")
    fon.write(str(int(rate/2)))
    fon.close()

    foff=open("/sys/class/leds/led0/delay_off","w")
    foff.write(str(int(rate/2)))
    foff.close()
