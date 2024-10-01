import RPi.GPIO as GPIO
from time import sleep
import datetime
from ischedule import schedule, run_loop
import os
import sys

#Define which GPIO pin controls which relay module
Relaymodule_white = 14
Relaymodule_blue = 15
Relaymodule_green = 18
Relaymodule_white_tra =23 
 

#Define which GPIO pin controls which stepping motor
#If you do not want to synchronize the movement of filters and light sources, prepare scripts for the filter table and the light source table.
motorGpio_low_actuator = (12, 16, 20, 21)     
motorGpio_high_actuator = (24, 25, 8, 7)      
motorGpio_filter_light = (4, 17, 27, 22)      


rightRotation = (0x08,0x04,0x02,0x01)  #Definition of right rotation 
leftRotation = (0x01,0x02,0x04,0x08)   #Definition of left rotation
 
#Set up GPIO pins to drive relay modules and stepper motors
#If you do not want to synchronize the movement of filters and light sources, prepare scripts for the filter table and the light source table.
def setup():
    GPIO.setmode(GPIO.BCM)      
    for pin in motorGpio_low_actuator:
        GPIO.setup(pin,GPIO.OUT)
    for pin in motorGpio_high_actuator:
        GPIO.setup(pin,GPIO.OUT)
    for pin in motorGpio_filter_light:
        GPIO.setup(pin,GPIO.OUT)

    GPIO.setup(Relaymodule_white, GPIO.OUT)
    GPIO.setup(Relaymodule_blue, GPIO.OUT)
    GPIO.setup(Relaymodule_green, GPIO.OUT)
    GPIO.setup(Relaymodule_white_tra, GPIO.OUT)
 
#Define parameters for running the stepping motors (for y axis actuator)
def moveSteps_low(lrset, ms, steps):
    for i in range(steps):
        moveOnePeriod_low(lrset, ms)

#Define parameters for running the stepping motors (for x axis actuator)       
def moveSteps_high(lrset, ms, steps): 
    for i in range(steps):
        moveOnePeriod_high(lrset, ms)

#Define parameters for running the stepping motors (for Light source table and optical filter table)  
#If you do not want to synchronize the movement of filters and light sources, prepare scripts for the filter table and the light source table.       
def moveSteps_filter_light(lrset, ms, steps):
    for i in range(steps):
        moveOnePeriod_filter_light(lrset, ms)

#Definition of GPIO pin inputs and outputs to drive a stepper motor (for x axis actuator)
def moveOnePeriod_low(lrset, ms):
    for j in range(0, 4, 1):
        for i in range(0, 4, 1):
            if lrset == 1:
                GPIO.output(motorGpio_low_actuator[i], ((leftRotation[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))
            else:
                GPIO.output(motorGpio_low_actuator[i], ((rightRotation[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))
        if ms < 2:  #Set to 2 ms if less than 2 ms, since 1 ms will not work.
            ms = 2
        sleep(ms * 0.001)
        
#Definition of GPIO pin inputs and outputs to drive a stepper motor (for y axis actuator)
def moveOnePeriod_high(lrset, ms):
    for j in range(0, 4, 1):
        for i in range(0, 4, 1):
            if lrset == 1:
                GPIO.output(motorGpio_high_actuator[i], ((leftRotation[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))
            else:
                GPIO.output(motorGpio_high_actuator[i], ((rightRotation[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))
        if ms < 2:  #Set to 2 ms if less than 2 ms, since 1 ms will not work.
            ms = 2
        sleep(ms * 0.001)
        
#Definition of GPIO pin inputs and outputs to drive a stepper motor (for Light source table and optical filter table)
#If you do not want to synchronize the movement of filters and light sources, prepare scripts for the filter table and the light source table.
def moveOnePeriod_filter_light(lrset, ms):
    for j in range(0, 4, 1):
        for i in range(0, 4, 1):
            if lrset == 1:
                GPIO.output(motorGpio_filter_light[i], ((leftRotation[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))
            else:
                GPIO.output(motorGpio_filter_light[i], ((rightRotation[j] == 1 << i) and GPIO.HIGH or GPIO.LOW))
        if ms < 2:  #Set to 2 ms if less than 2 ms, since 1 ms will not work.
            ms = 2
        sleep(ms * 0.001)


 
#End processing
def end():
    GPIO.cleanup()   #Clear GPIO. If you don't put it on, you'll get a warning.


#About 0.7°/step
#128 steps = shaft rotates 90°
#Parameter of stepping motor(Rotation direction 0 or 1,Rotation speed,Steps)

#Code sample for imaging 1 well 

    #Trans-illumination white 

    #GPIO.output(Relaymodule_white_tra, GPIO.HIGH)  #Turning on LED
    #sleep(3)   #Holds still for 3 seconds while lit
    #os.system("/home/raspberry4/Experiment/test1_1.sh")    #Capture image (Directory indicates path to sh file)
    #GPIO.output(Relaymodule_white_tra, GPIO.LOW)   #Turning off LED
    #sleep(3)

    #Epi-illumination blue 

    #moveSteps_filter_light(1,3,128)    #Rotate the light source table and optical filter table 90°.
    #GPIO.output(Relaymodule_blue, GPIO.HIGH)
    #sleep(3)
    #os.system("/home/raspberry4/Experiment/test2_1.sh")
    #GPIO.output(Relaymodule_blue, GPIO.LOW)
    #sleep(3)

    #Epi-illumination green 

    #moveSteps_filter_light(1,3,128)    #Rotate the light source table and optical filter table 90°.
    #GPIO.output(Relaymodule_green, GPIO.HIGH)
    #sleep(3)
    #os.system("/home/raspberry4/Experiment/test3_1.sh")
    #GPIO.output(Relaymodule_green, GPIO.LOW)
    #sleep(3)

    #Epi-illumination white
    
    #moveSteps_filter_light(0,3,256)    #Rotate the light source table and optical filter table 180° in opposite directions and return them to their original positions
    #GPIO.output(Relaymodule_white, GPIO.HIGH)
    #sleep(3)
    #os.system("/home/raspberry4/Experiment/test4_1.sh")
    #GPIO.output(Relaymodule_white, GPIO.LOW)
    #sleep(3)
    

def loop():
    print("working...")
   
    #Movement from initial position to well 1
    moveSteps_high(0,3,480)
    moveSteps_low(1,3,130)
    
    #Trans-illumination white 
    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_1.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    #Epi-illumination blue 
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_1.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    #Epi-illumination green 
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_1.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    #Epi-illumination white
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_1.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    
    #From well1 to well2
    moveSteps_high(0,3,600)

    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_2.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_2.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_2.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_2.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    
    
    #From well2 to well3
    moveSteps_high(0,3,600)

    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_3.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_3.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_3.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_3.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    #Homing motion of x axis from well3 to well1
    moveSteps_high(1,3,1880)
    moveSteps_high(0,3,480)
    
    
    #From well1 to well4
    moveSteps_low(1,3,600)

    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_4.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_4.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_4.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_4.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    
    
    #From well4 to well5
    moveSteps_high(0,3,600)
    
    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_5.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_5.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_5.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_5.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    #From well5 to well6
    moveSteps_high(0,3,600)
    
    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_6.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_6.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_6.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_6.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    
    #Homing motion of x axis from well6 to well4
    moveSteps_high(1,3,1880)
    moveSteps_high(0,3,480)
    
    #From well4 to well7
    moveSteps_low(1,3,600)
    
    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_7.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_7.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_7.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_7.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    
    #From well7 to well8
    moveSteps_high(0,3,600)
    #tra white
    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_8.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_8.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_8.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_8.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)
    
    
    #From well8 to well9
    moveSteps_high(0,3,600)
    
    GPIO.output(Relaymodule_white_tra, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test1_9.sh")
    GPIO.output(Relaymodule_white_tra, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_blue, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test2_9.sh")
    GPIO.output(Relaymodule_blue, GPIO.LOW)
    sleep(3)
    
    moveSteps_filter_light(1,3,128)
    GPIO.output(Relaymodule_green, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test3_9.sh")
    GPIO.output(Relaymodule_green, GPIO.LOW)
    sleep(3)
  
    moveSteps_filter_light(0,3,256)
    GPIO.output(Relaymodule_white, GPIO.HIGH)
    sleep(3)
    os.system("/home/raspberry4/Experiment/test4_9.sh")
    GPIO.output(Relaymodule_white, GPIO.LOW)
    sleep(3)

    
    #From well9 to Initial position
    moveSteps_high(1,3,1780)
    sleep(3)
    moveSteps_low(0,3,1430)
    
    print("done")
  
       
def job():
    setup()                     #Do setup()
    loop()                      #Do loop()
    end()                       #Do end()
    
    
job()

#Script interval 1200=20min, 1800=30min
schedule(job, interval=1200)

run_loop()
    
    



