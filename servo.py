import RPi.GPIO as GPIO
from time import sleep
class Camera:  
    def __init__(self):
        pass
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(11,GPIO.OUT) 
        # self.pwm = GPIO.PWM(11,50)
        # self.pwm.start(0)
        

    def SetAngle(self, angle):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37,GPIO.OUT) 
        self.pwm = GPIO.PWM(37,50)
        self.pwm.start(0)
        self.duty = angle/ 18 + 2
        GPIO.output(37, True)
        self.pwm.ChangeDutyCycle(self.duty)
        sleep(2)
        GPIO.output(37, False)
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
        GPIO.cleanup()   

    def camera(self):
        for i in range(90,180,15):
            self.SetAngle(i)
        for i in range(180,90,-15):
            self.SetAngle(i)
        for i in range(90,0,-15):
            self.SetAngle(i)
        for i in range(0,90,15):
            self.SetAngle(i)

camera = Camera()
camera.SetAngle(30)   

