# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os
import manager

GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#13赤19青26緑


while True:
  if GPIO.input(16) == False:
    #入室

    GPIO.output(26,True)

    path = u'./my_felica_dump.sh'
    os.system(path)

    dump_bool = manager.dump(1) 

    if dump_bool:
      GPIO.output(26,False)
      GPIO.output(19,True)
      time.sleep(0.2)
      GPIO.output(19,False)
      time.sleep(0.2)
      GPIO.output(19,True)
      time.sleep(0.2)

    else:
      GPIO.output(26,False)

      GPIO.output(13,True)
      time.sleep(0.1)
      GPIO.output(13,False)
      time.sleep(0.1)
      GPIO.output(13,True)
      time.sleep(0.1)
      GPIO.output(13,False)
      time.sleep(0.1)
      GPIO.output(13,True)
      time.sleep(0.1)


  elif GPIO.input(20) == False:
    #退室 

    GPIO.output(26,True)

    path = u'./my_felica_dump.sh'
    os.system(path)

    dump_bool = manager.dump(0) 

    if dump_bool:

      GPIO.output(26,False)
      GPIO.output(19,True)
      time.sleep(0.2)
      GPIO.output(19,False)
      time.sleep(0.2)
      GPIO.output(19,True)
      time.sleep(0.2)

    else:
      GPIO.output(26,False)

      GPIO.output(13,True)
      time.sleep(0.1)
      GPIO.output(13,False)
      time.sleep(0.1)
      GPIO.output(13,True)
      time.sleep(0.1)
      GPIO.output(13,False)
      time.sleep(0.1)
      GPIO.output(13,True)
      time.sleep(0.1)

  else:
    GPIO.output(13,False)
    GPIO.output(19,False)
    GPIO.output(26,False)
