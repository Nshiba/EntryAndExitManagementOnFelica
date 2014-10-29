# -*- coding: utf-8 -*-
import os

enterPath = u'./enter.sh'
exitPath = u'./exit.sh'

def TrueOrFalse(testbool):
    if testbool == True:
        os.system(enterPath)
    else:
        os.system(exitPath)
