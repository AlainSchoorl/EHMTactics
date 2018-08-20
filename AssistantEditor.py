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

stat1 = []
stat2 = [1]
stat3 = [13,15,16,17,18]
statList = [stat1,stat2,stat3]
value = "50"

time.sleep(2)
click(548, 108)

#35 / 16
#930, 308
#1136, 328
for a in range(1, 16):
    doubleClick(98, 168 + (a*17))
    time.sleep(0.4)
    c = 1
    for x in statList:
        for y in x:
            click(733 + (c*206), 299 + (y*20))
            delete()
            delete()
            delete()
            ran = random.choice([1,2,4,17,19,20])
            ran = str(ran)
            type(ran)
            #type(value)
        c += 1
    '''c = 1
    for y in stat0:
        click(743, 299 + (y * 20))
        delete()
        delete()
        delete()
        type(value)'''
    click(1397, 183)
    time.sleep(0.4)




'''

#get_region((132,89,580,119), 1, Image.BICUBIC)
name = get_string((src_path + str(1) + "test.png"), 0)
print name'''