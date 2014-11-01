# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os
import manager
import mytwitter

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
            success_read(1)

        else:
            error_read()


    elif GPIO.input(20) == False:
        #退室 

        GPIO.output(26,True)

        path = u'./my_felica_dump.sh'
        os.system(path)

        dump_bool = manager.dump(0) 

        if dump_bool:
            success_read(0)

        else:
            error_read()

    else:
        GPIO.output(13,False)
        GPIO.output(19,False)
        GPIO.output(26,False)


def success_read(read_type):
    GPIO.output(26,False)
    GPIO.output(19,True)
    time.sleep(0.2)
    GPIO.output(19,False)
    time.sleep(0.2)
    GPIO.output(19,True)
    time.sleep(0.2)

    mane = manager.ninzu()
    ninzu = mane[0]
    gakuT = mane[1]

    if read_type == 1:
        mytwitter.myUpdate_status(gakuT + "が入室しました。現在" + ninzu + "名です。")
    else:
        mytwitter.myUpdate_status(gakuT + "が退出ました。現在" + ninzu + "名です。")


def error_read():
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
