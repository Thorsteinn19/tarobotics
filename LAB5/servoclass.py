import pigpio

class Servomotor(object):
    def __init__(self,pin):
        self.pin=pin
        self.pwm = pigpio.pi()
        self.angle = 0
        self.pwm.set_PWM_frequency(self.pin,50)
        self.pwm.set_servo_pulsewidth(self.pin,500)

    def changeangle(self,angle):
        self.angle = angle
        self.pwm.set_servo_pulsewidth(self.pin,int(500+(angle/180)*2000))
        
