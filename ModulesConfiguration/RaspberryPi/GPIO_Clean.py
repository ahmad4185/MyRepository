# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:30:21 2019

@author: Ahmad4185
"""


#This file is added to clean up the GPIO pins after running the file. 
#It is important, otherwise you will be not able to run your program again
#Or your program will consistently run even if you break the program. 
#Cleaning GPIO pins will stop the process. 


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

