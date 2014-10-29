# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)

GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)

enterPath = u'./enter.sh'
exitPath = u'./exit.sh'

while True:
	if GPIO.input(16) == False:
		GPIO.output(21,True)
		os.system(enterPath)
		GPIO.output(21,False)
	elif GPIO.input(20) == False:
		GPIO.output(21,True)
		os.system(exitPath)
		GPIO.output(21,False)
