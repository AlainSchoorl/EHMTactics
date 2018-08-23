import pyautogui
import random

#print(pyautogui.position())

for x in range(0,20):
    print(random.randint(0,1))


'''


if ord(msvcrt.getch()) == 0
    print ord(msvcrt.getch())
    break
'''
'''
import win32api, win32con
import time
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def click(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x / SCREEN_WIDTH * 65535.0), int(y / SCREEN_HEIGHT * 65535.0))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)

click(793,37)
time.sleep(1)
click(793,37)
time.sleep(0.5)
click(790,414)
time.sleep(0.5)
click(1402,530)
time.sleep(0.5)
click(1197,507)

import ctypes
import time

def click(x,y):
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2,0,0,0,0)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)


click(793,37)
time.sleep(1)
click(790,414)
time.sleep(1)
click(1402,530)
time.sleep(1)
click(1197,507)
time.sleep(1)
click(1254,606)
time.sleep(1)
click(1364,652)
time.sleep(1)
click(790,414)
time.sleep(435)
'''