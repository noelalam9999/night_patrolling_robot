import RPi.GPIO as GPIO
from time import sleep
class Servo:  
    def __init__(self):
        pass
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(11,GPIO.OUT) 
        # self.pwm = GPIO.PWM(11,50)
        # self.pwm.start(0)
        

    def SetAngle(self, angle):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT) 
        self.pwm = GPIO.PWM(11,50)
        self.pwm.start(0)
        self.duty = angle/ 18 + 2
        GPIO.output(11, True)
        self.pwm.ChangeDutyCycle(self.duty)
        sleep(3)
        GPIO.output(11, False)
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
        GPIO.cleanup()   

turn = Servo()
turn.SetAngle(120)
    
        
