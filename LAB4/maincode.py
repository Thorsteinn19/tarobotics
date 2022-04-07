from larsen import PWMLEDboard
pwmleadboard = PWMLEDboard([4, 22, 27, 5, 6],23,24, 1)
while True:
    pwmleadboard.larsen()
    pwmleadboard.button.when_pressed = pwmleadboard.stop_lights