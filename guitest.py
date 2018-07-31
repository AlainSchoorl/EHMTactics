import pyautogui
import numpy as np
from numpy import *
from PIL import Image
from PIL import *
import pytesseract
import cv2
import os
import time
import ctypes

#vacation

'''
pyautogui.click(793,37)
pyautogui.click()
time.sleep(1)
pyautogui.click(793,37)
time.sleep(1)
pyautogui.click(793,37)
time.sleep(0.5)
pyautogui.click(790,414)
time.sleep(0.5)
pyautogui.click(1402,530)
time.sleep(0.5)
pyautogui.click(1197,507)
time.sleep(0.5)
pyautogui.click(1254,606)
time.sleep(0.5)
pyautogui.click(1364,652)
time.sleep(0.5)
pyautogui.click(790,414)
time.sleep(435)


'''
#results

def get_region(box, i, extra):
    #Grabs the region of the box coordinates
    im = ImageGrab.grab(box)
    #Change size of image to 200% of the original size
    a, b, c, d = box
    doubleX = (c - a) * 2
    doubleY = (d - b) * 2
    im.resize((doubleX, doubleY), extra).save(os.getcwd() + "\\" + str(i) + "test.png", 'PNG')

def get_string(img_path):
    img = cv2.imread(img_path)
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)
    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)
    # Recognize text with tesseract for python
    string = '--psm 7 -c tessedit_char_whitelist=WL0123456789sot-'
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config=string)

    return result

def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)

def getResults():
    print("go to schedule screen")
    click(368,108)
    print('schedule click')
    time.sleep(0.5)
    i = 1
    goalsFor = 0
    goalsAgainst = 0
    for x in regionList2:
        # Grab the region of the screenshot (box area)
        #click(x[0],x[1])
        #time.sleep(0.25)
        region = (x[0],x[1],x[2],x[3])

        get_region(region, i, Image.BICUBIC)
        string = get_string(src_path + str(i) + "test.png")
        results = interpret(string)
        time.sleep(0.05)
        if (results[0]==-1):
            get_region(region, i, Image.BILINEAR)
            string = get_string(src_path + str(i) + "test.png")
            results = interpret(string)
            time.sleep(0.05)
            if (results[0]==-1):
                get_region(region, i, Image.ANTIALIAS)
                string = get_string(src_path + str(i) + "test.png")
                results = interpret(string)
                time.sleep(0.05)
                if (results[0]==-1):
                    results = [0,0]
        goalsFor = goalsFor + results[0]
        goalsAgainst = goalsAgainst + results[1]
        i += 1
    goalsFor = float(goalsFor)
    goalsAgainst = float(goalsAgainst)
    fitness = [goalsFor,goalsAgainst,(goalsFor/(goalsFor+goalsAgainst))]
    print ('Fitness:')
    print fitness
    return fitness
    #go to schedule screen
    #read screen, add goals for/against
    #calculate fitness
    #return fitnessList

def interpret(string):
    print('String read: ' + string.encode('utf-8'))
    dash = string.find('-')
    if(dash < 0):
        return [-1,-1]
    if(len(string)-(dash+1) == 2):
        goalsAgainst = int(string[-2:])
    else:
        goalsAgainst = int(string[-1:])
    if(string[dash-2].isdigit() and (not string[dash-2] == 0)):
        goalsFor = int(string[dash-2:dash])
    else:
        goalsFor = int(string[dash-1])
    ot = 0
    if (string.find('ot') > -1 or string.find('0t') > -1  or string.find('so') > -1 or string.find('s0') > -1 or string.find('50') > -1 or string.find('5o') > -1):
        ot = True
    if (ot):
        if (goalsFor > goalsAgainst):
            goalsFor -= 1
        else:
            goalsAgainst -= 1
    print('goalsFor: ' + str(goalsFor) + ' goalsAgainst: ' + str(goalsAgainst))
    return [goalsFor, goalsAgainst]

pyautogui.click(861,376)
src_path = "X:\\Users\\Alain\\Documents\\GitHub\\EHMTactics\\"
regionList = ([1500,287],[150,403],[960,403],[1770,403],[150,519],[690,519],[1500,519],[1770,519],[150,635],[420,635],
              [960,635],[1230,635],[150,751],[960,751])
regionList2 = ([1582,331,1636,350],[227,447,281,466],[1040,447,1094,466],[1853,447,1907,466],[227,563,281,582],
               [769,563,823,582],[1582,563,1636,582],[1853,563,1907,582],[227,679,281,698],[498,679,552,698],
               [1040,679,1094,698],[1311,679,1365,698],[227,795,281,814],[1040,795,1094,814])
reloadList = ([1613,12],[1558,95],[1143,609],[759,401],[1178,842])

time.sleep(1)
for x in reloadList:
    click(x[0], x[1])
    time.sleep(1)
