import time
from morsecodefunc import morseconvert

def ledcontrol(textstring):

    filedir="/sys/class/leds/led0/brightness"
    fopen=open(filedir,"w")
    fopen.write("0")
    fopen.close()
    morse=morseconvert(textstring)

    morselist = morse.split("_ ")
    timeint=0.3
    for name in morselist:
        time.sleep(4*timeint)
        name = name.split(" ")
        for letter in name:
            time.sleep(2*timeint)
            for mchar in letter:
                fopen=open(filedir,"w")
                fopen.write("255")
                time.sleep(timeint)
                fopen.close()
                fwriter=open(filedir,"w")
                fwriter.write("0")
                if mchar == ".":
                    time.sleep(timeint)

                elif mchar == "-":
                    time.sleep(3*timeint)

                print(mchar)
                fwriter.close()

    ff=open(filedir,"w")
    ff.write("255")
    ff.close()


if __name__ == "__main__":
    names= "a"
    ledcontrol(names)

