import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)
GPIO.output(21,True)

def trueout():
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,True)

def falseout():
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,False)
	
def inputButton():
	GPIO.setup(18,GPIO.IN)
	GPIO.setup(15,GPIO.IN)
	while True:
		print '18 to'
		print GPIO.input(18)
		print '15 to'
		print GPIO.input(15)
		time.sleep(0.2)
