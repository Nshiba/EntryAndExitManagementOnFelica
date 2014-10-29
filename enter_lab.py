# -*- coding: utf-8 -*-

#入室するときに実行するファイル

import os.path
import datetime
import csv

ld = open("dump_data/temporary_dump.txt")
#ld = param[2]
lines = ld.readlines()
ld.close()

def gakuban_seikei():
    for line in lines:
        if line.find('006A:0000') >= 0:
            gakuban = line[16:-1]
            gakubanR = gakuban[:14]
            return gakubanR

def shimei_seikei():
    for line in lines:
        if line.find('006A:0001') >= 0:
            shimei = line[12:-1]
            shimeiR = shimei.replace("00","")
            return shimeiR

def asc_to_mozi(asc_mozi):
    mozi = ''
    while asc_mozi != '':
        mozi += chr(int(asc_mozi[:2],16))
        asc_mozi = asc_mozi[2:]
    return mozi

row = []

gakuT = asc_to_mozi(gakuban_seikei())
row.append(asc_to_mozi(shimei_seikei()))
#入室
row.append(1)
row.append(datetime.datetime.now())

filename = 'dump_data/' + gakuT + '.csv'

with open(filename, 'a') as f:
    writer = csv.writer(f, lineterminator='\n') 
    writer.writerow(row)
