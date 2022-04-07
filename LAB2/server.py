from morssecode import ledcontrol
import time
import socket
import os
while True:
    with socket.socket() as s:

        host ="192.168.1.124"
        port = 8001

        s.bind((host, port))

        s.listen()

        con, addr = s.accept()

        with con:

            while True:

                data = str(con.recv(1024),"utf-8")
                print(data)
                if not data:
                    break
                filedir="/sys/class/leds/led0/brightness"

                con.sendall(bytes(data,"utf-8"))

                if data[0] == "b":

                    herts=data[1:]
                    herts=int(herts)
                    if herts < 200 | herts!=0:
                        os.system('cd /sys/class/leds/led0; sudo sh -c "echo timer > trigger"')

                    else:
                        os.system('cd /sys/class/leds/led0; sudo sh -c "echo none > trigger"')

                    if herts == 0:
                        fzero=open(filedir,"w")
                        fzero.write("0")
                        fzero.close()

                    elif herts >= 200:
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
                else:
                    os.system('sudo sh -c "echo none > trigger"')
                    ledcontrol(data)


