from threading import Thread
import math
from time import sleep
import getch

from DWM_library.dwm_class import DWM
from functions.Motor_driver_func import motor_driver

import simpleaudio as sa



dwm = DWM(debug = 1)
motors = motor_driver(debug=0)

# for i in range(3):
#     dwm.get_pos_avg(30)
# for i in range(3):
#     dwm.get_pos_avg(10)
# for i in range(10):
#     dwm.get_pos_avg(1)
#     dwm.get_pos()


def get_angle(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    rad = math.atan2(delta_y, delta_x)

    theta = rad * 180 / math.pi
    
    return theta
    


x_input = 10980
y_input = 0

margin = 250

def get_acc_data():
    dwm.get_acc_data()

acc_thread = Thread(target=get_acc_data)
acc_thread.start

while 1:
    user_input = getch.getch()  # User input, but not displayed on the screen
    print(user_input)
    
    if (user_input == 'w'):
        motors.forward()
    
    if (user_input == 'a'):
        motors.left_deg(10)

    if (user_input == 'd'):
        motors.right_deg(10)

    if (user_input == 's'):
        motors.backwards()

    if (user_input == 'q'):
        exit(0)
    
    if (user_input == 'f'):
        motors.stop()

    if (user_input == 'i'):
        print(" ")
        x_input = int(input("X: "))
        y_input = int(input("Y: "))

    if (user_input == 'r'):
        dwm.get_pos()
        if (dwm.x_pos <= x_input + margin and dwm.x_pos >= x_input - margin and dwm.y_pos <= y_input + margin and dwm.y_pos >= y_input - margin):
            print("On destination")
        else:
            dwm.get_pos_avg(1)
            old_x = dwm.x_pos
            old_y = dwm.y_pos

            motors.forward()
            sleep(2)
            #motors.stop()
            dwm.get_pos()

            desired_angle = get_angle(dwm.x_pos, dwm.y_pos, x_input, y_input)
            print("Desired angle = {}".format(desired_angle))

            heading_angle = get_angle(old_x, old_y, dwm.x_pos, dwm.y_pos)
            print("Heading angle = {}".format(heading_angle))

            diff_angle = heading_angle - desired_angle
            print("Diff angle = {}".format(diff_angle))

            if (diff_angle < 0):
                motors.left_deg(abs(diff_angle))
            else:
                motors.right_deg(abs(diff_angle))

            motors.stop()

    if (user_input == 't'):
        wave_obj = sa.WaveObject.from_wave_file("audio/cutG.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
    
    if (user_input == 'm'):
        wave_obj = sa.WaveObject.from_wave_file("audio/mom.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

          