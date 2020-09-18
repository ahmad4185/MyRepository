# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:30:21 2019

@author: Ahmad4185
"""


#================================#
#     IMPORTING LIBRARIES        #
#================================#

import RPi.GPIO as GPIO #For GPIO Operations
import time #For Delay Function


#================================#
#     SETTING OF GPIO PART       #
#================================#

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#================================#
#       MACROS FOR PROGRAM       #
#================================#

TRIG = 23   #GPIO Pin for Ultrasonic Trigger
ECHO = 24   #GPIO Pin for Ultrasonic Echo
SETTLING_TIME = 0.2 #Settling time for Ultrasonic sensor
CLEAR_TIME = 0.00001 #Clear Time for Ultrasonic sensor

DELAY = 0.2 #Sampling Time for taking data from Ultrasonic sensor
THRESHOLD = 30 #Distane threshold in centimeters

FLAG = 1

def Ultrasonic(Trigger, Echo, ClearTime, Flag, SettlingTime):
    

    # This code is used when we have to initialize the Ultrasonic sensor.
    # Use it once in a code only. For the rest of the program, set the 
    # Flag to 0 

    if (Flag == 1):
    
        GPIO.setup(Trigger, GPIO.OUT)
        GPIO.setup(Echo, GPIO.IN)

        GPIO.output(Trigger, False) #Trigger pin is cleared to avoid residual noise
        time.sleep(SettlingTime)    #Time to set the Ultrasonic sensor
        return "ultrasonic sensor has been settled"
    else:   
        GPIO.output(Trigger, True)  #Initializing of Trigger
        time.sleep(ClearTime)       #Delay for Trigger
        GPIO.output(Trigger, False) #Closing the Trigger operation

        while (GPIO.input(Echo)==0):
            pulse_start = time.time()       
        while (GPIO.input(Echo)==1):
            pulse_end = time.time()

        distance = (pulse_end-pulse_start)*17150 #Converting distance into centimeters
        return round(distance, 2) #Rounding distance values

    

Ultrasonic(TRIG, ECHO, CLEAR_TIME,FLAG, SETTLING_TIME) #Initializing the Ultrasonic sensor 
FLAG = 0

while(1):
	
    distance = Ultrasonic(TRIG, ECHO, CLEAR_TIME,FLAG, SETTLING_TIME)
    print ("Distance: ", distance, "cm")
    time.sleep(DELAY)

    if (distance < THRESHOLD):
        time.sleep(DELAY)

        while (distance <THRESHOLD):

            distance = Ultrasonic(TRIG, ECHO, CLEAR_TIME,FLAG,SETTLING_TIME)
            print ("Inside the while loop: ", distance, "cm")
            time.sleep(DELAY)

