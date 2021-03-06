import RPi.GPIO as GPIO
import time
class Sonar:
    def sonar(self,trig,echo):
        try:
            GPIO.setmode(GPIO.BOARD)

            self.PIN_TRIGGER = trig
            self.PIN_ECHO = echo

            GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(self.PIN_ECHO, GPIO.IN)

            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

            

            time.sleep(2)

            

            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(self.PIN_ECHO)==0:
                    pulse_start_time = time.time()
            while GPIO.input(self.PIN_ECHO)==1:
                    pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            return distance

        finally:
            GPIO.cleanup()