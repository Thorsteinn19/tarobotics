from morssecode import ledcontrol
import os
os.system('cd /sys/class/leds/led0; sudo sh -c "echo timer > trigger"')
#ledcontrol("a")
