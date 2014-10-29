# -*- coding: utf-8 -*-
import os

enterPath = u'./enter.sh'
exitPath = u'./exit.sh'

def TrueOrFalse(testbool):
    if testbool == True:
	try:
        	os.system(enterPath)
	except NoneError:
		return False
    else:
        os.system(exitPath)

TrueOrFalse(True)
