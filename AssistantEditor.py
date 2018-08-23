import ctypes
import time
import numpy as np
from numpy import *
from PIL import Image
from PIL import ImageGrab
import pytesseract
import cv2
import os
import msvcrt
import csv
import sys

# mode = int(sys.argv[1])



def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

def doubleClick(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    time.sleep(0.09)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

def getCode(character):
    if character == "0":
        return 0x30
    elif character == "1":
        return 0x31
    elif character == "2":
        return 0x32
    elif character == "3":
        return 0x33
    elif character == "4":
        return 0x34
    elif character == "5":
        return 0x35
    elif character == "6":
        return 0x36
    elif character == "7":
        return 0x37
    elif character == "8":
        return 0x38
    elif character == "9":
        return 0x39
    else:
        return 0x30

def type(string):
    for char in string:
        keycode = getCode(char)
        ctypes.windll.user32.keybd_event(keycode, 0, 0, 0)
        time.sleep(0.05)
        ctypes.windll.user32.keybd_event(keycode, 0, 0x0002, 0)
        time.sleep(0.05)

def delete():
    ctypes.windll.user32.keybd_event(0x2E, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(0x2E, 0, 0x0002, 0)
    time.sleep(0.05)

def enter():
    ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(0x0D, 0, 0x0002, 0)
    time.sleep(0.05)

def read():
    print 'reading'
    readlist = []
    with open(('roles.csv'), 'rb') as File:
        reader = csv.reader(File, delimiter=';')
        for row in reader:
            role = []
            for col in row:
                role.append(int(col))
            readlist.append(role)
    return readlist

def setTechs(i):
    atts = []
    for x in range(0,14):
        atts.append(allRoles[i][x])
    return atts

def setMents(i):
    atts = []
    for x in range(14,27):
        atts.append(allRoles[i][x])
    return atts

def setPhys(i):
    atts = []
    for x in range(27,37):
        atts.append(allRoles[i][x])
    return atts

def setHW(i):
    atts = []
    for x in range(37,39):
        atts.append(allRoles[i][x])
    return atts

def setRoles(i):
    atts = []
    for x in range(39,41):
        atts.append(allRoles[i][x])
    return atts

allRoles = read()

#0 : DefD
#1 : DefD (Fin)
#2 : DefD (Phy)
#3 : OffD
#4 : OffD (Fin)
#5 : OffD (Phy)
#6 : PMD
#7 : PMD (Fin
#8 : PMD (Phy)
#9 : PntD
#10: PntD (Fin)
#11: PntD (Phy)
#12: SAHD
#13: TWD
#14: TWF
#15: DefF
#16: DefF (Fin)
#17: DefF (Phy)
#18: SkF
#19: Grinder
#20: PMF
#21: PMF (Fin)
#22: PMF (Phy)
#23: PowF
#24: GSF
#25: GSF (Fin)
#26: GSF (Phy)

techs = []
ments = []
phys = []
ada = 12
amb = 12
det = 12
loy = 12
pre = 12
pro = 12
spo = 12
tem = 12
pers = [ada, amb, det, loy, pre, pro, spo, tem]
hw = []
roles = []
time.sleep(2)
click(548, 108)

#35 / 16
#930, 308
#1136, 328

roleNum = 13
techs = setTechs(roleNum)
ments = setMents(roleNum)
phys = setPhys(roleNum)
hw = setHW(roleNum)
roles = setRoles(roleNum)

for a in range(1, 4):
    doubleClick(98, 168 + (a*17))
    time.sleep(0.4)
    c = 1
    a = 0
    for y in techs:
        click(733 + (c*206), 319 + (a*20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        #type(value)
    a += 9
    for y in hw:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    c += 1
    a = 0
    for y in ments:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    a += 9
    for y in roles:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a = 0
    c += 1
    for y in phys:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    click(1397, 183)
    time.sleep(0.4)

roleNum = 6
techs = setTechs(roleNum)
ments = setMents(roleNum)
phys = setPhys(roleNum)
hw = setHW(roleNum)
roles = setRoles(roleNum)

for a in range(4, 7):
    doubleClick(98, 168 + (a*17))
    time.sleep(0.4)
    c = 1
    a = 0
    for y in techs:
        click(733 + (c*206), 319 + (a*20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        #type(value)
    a += 9
    for y in hw:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    c += 1
    a = 0
    for y in ments:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    a += 9
    for y in roles:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a = 0
    c += 1
    for y in phys:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    click(1397, 183)
    time.sleep(0.4)

roleNum = 14
techs = setTechs(roleNum)
ments = setMents(roleNum)
phys = setPhys(roleNum)
hw = setHW(roleNum)
roles = setRoles(roleNum)

for a in range(7, 11):
    doubleClick(98, 168 + (a*17))
    time.sleep(0.4)
    c = 1
    a = 0
    for y in techs:
        click(733 + (c*206), 319 + (a*20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        #type(value)
    a += 9
    for y in hw:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    c += 1
    a = 0
    for y in ments:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    a += 9
    for y in roles:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a = 0
    c += 1
    for y in phys:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    click(1397, 183)
    time.sleep(0.4)

roleNum = 20
techs = setTechs(roleNum)
ments = setMents(roleNum)
phys = setPhys(roleNum)
hw = setHW(roleNum)
roles = setRoles(roleNum)

for a in range(11, 15):
    doubleClick(98, 168 + (a*17))
    time.sleep(0.4)
    c = 1
    a = 0
    techs[4] = 80
    for y in techs:
        click(733 + (c*206), 319 + (a*20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        #type(value)
    a += 9
    for y in hw:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    c += 1
    a = 0
    for y in ments:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    a += 9
    for y in roles:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a = 0
    c += 1
    for y in phys:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    click(1397, 183)
    time.sleep(0.4)

roleNum = 24
techs = setTechs(roleNum)
ments = setMents(roleNum)
phys = setPhys(roleNum)
hw = setHW(roleNum)
roles = setRoles(roleNum)

for a in range(15, 19):
    doubleClick(98, 168 + (a*17))
    time.sleep(0.4)
    c = 1
    a = 0
    for y in techs:
        click(733 + (c*206), 319 + (a*20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        #type(value)
    a += 9
    for y in hw:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    c += 1
    a = 0
    for y in ments:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a += 1
    a += 9
    for y in roles:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        type(str(y))
        a += 1
        # type(value)
    a = 0
    c += 1
    for y in phys:
        click(733 + (c * 206), 319 + (a * 20))
        delete()
        delete()
        delete()
        a += 1
        # type(value)
    a += 1
    click(1397, 183)
    time.sleep(0.4)




'''

#get_region((132,89,580,119), 1, Image.BICUBIC)
name = get_string((src_path + str(1) + "test.png"), 0)
print name'''