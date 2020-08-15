import RPi.GPIO as GPIO
import time
from sonar import Sonar 
from motion import Driver
from turn import Servo
#from servo import Camera
def main():
    #camera = Camera()
    #camera.camera()
    #driver.__init__()
    #servo.__init__()
    sonar=Sonar()
    try:
        while True:
            motion=0
            servo = Servo()
            front_center_obs = sonar.sonar(5,15)
            front_right_obs = sonar.sonar(7,19)
            front_left_obs = sonar.sonar(3,13)
            print(front_left_obs,front_center_obs,front_right_obs)
            if front_center_obs>100 :
                if front_right_obs>75:
                    if front_left_obs>75:
                        motion=1
                        servo.SetAngle(120)
                    else:
                        servo = Servo()
                        servo.SetAngle(135)
                        motion=1
                else:
                    if front_left_obs>75:
                        servo.SetAngle(105)
                        motion=1
                    else:                 
                        back_center_obs = sonar.sonar(18,26)
                        back_right_obs = sonar.sonar(16,24)
                        back_left_obs = sonar.sonar(38,40)
                        print("back",back_left_obs,back_center_obs,back_right_obs)
                        if back_center_obs>75 :
                            if back_right_obs>75:
                                if back_left_obs>75:
                                    servo.SetAngle(105)
                                    motion =2
                                else: 
                                    servo.SetAngle(135)
                                    motion =2
                            else:
                                if back_left_obs>75:
                                    servo.SetAngle(105)
                                    motion = 2
                                else: 
                                    motion =0
                        else:
                           motion =0
            else:
                servo = Servo()
                back_center_obs = sonar.sonar(18,26)
                back_right_obs = sonar.sonar(16,24)
                back_left_obs = sonar.sonar(38,40)
                print("back",back_left_obs,back_center_obs,back_right_obs)
                if back_center_obs>100:
                    if back_right_obs>75:
                        if back_left_obs>75:
                            if front_right_obs>75:
                                servo.SetAngle(135)
                            else:
                                servo.SetAngle(105)
                            
                            motion=2
                        else: 
                            servo.SetAngle(135)
                            motion=2
                    else:
                        if back_left_obs>75:
                            servo.SetAngle(105)
                            motion=2
                        else: 
                            motion=0
                else: 
                    motion=0
            print(motion)
            if motion==1:
                driver=Driver()
                driver.left()
                time.sleep(3)
                driver.cleanup()
                
                motion=0
            elif motion ==0:
                print("report HQ")
                motion=0
            elif motion==2:
                print("entered back command")
                

                driver=Driver()
                driver.right()
                time.sleep(3)
                driver.cleanup()   
                motion=0
            else:
                print("motion undefined")
    except KeyboardInterrupt:
        driver=Driver()
        driver.cleanup()
        print("Interrupted")
        motion=0

main()

