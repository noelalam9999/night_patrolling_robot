import RPi.GPIO as GPIO 
from time import sleep
class Driver:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.R_EN = 35
        self.L_EN = 33
        self.RPWM = 32
        self.LPWM = 31
        GPIO.setup(self.R_EN, GPIO.OUT)
        GPIO.setup(self.RPWM, GPIO.OUT)
        GPIO.setup(self.L_EN, GPIO.OUT)
        GPIO.setup(self.LPWM, GPIO.OUT)
        GPIO.output(self.R_EN, True)
        GPIO.output(self.L_EN, True)
    def neutral(self):
        GPIO.output(self.RPWM, False)  # Stop turning right
        GPIO.output(self.LPWM, False)  # stop turning left
    
    def right(self):
        GPIO.output(self.LPWM, False)  # stop turning left
        GPIO.output(self.RPWM, True)  # start turning right

    def left(self):
        GPIO.output(self.RPWM, False)  # Stop turning right
        GPIO.output(self.LPWM, True)  # start turning left      
    
    def cleanup(self):
        GPIO.cleanup()


driver = Driver()
driver.right()
sleep(3)
driver.left()
sleep(3)
driver.neutral()
driver.cleanup()