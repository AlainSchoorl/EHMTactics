import random
from Classes import Population
from Classes import Individual
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

vacationList = [[308,16],[313,389],[1166,596],[956,573],[1014,673],[1124,716],[1140,614],[1140,614]]
regionList = ([[1647,333,1703,352],[637,423,693,442],[1243,423,1299,442],[1849,423,1905,442],[637,513,693,532],
               [1041,513,1097,532],[1647,513,1703,532],[1849,513,1905,532],[637,603,693,622],[839,603,895,622,],
               [1243,603,1299,622],[1445,603,1501,622],[637,693,693,712],[1243,693,1299,712]])
regionList2 = ([1582,331,1636,350],[227,447,281,466],[1040,447,1094,466],[1853,447,1907,466],[227,563,281,582],
               [769,563,823,582],[1582,563,1636,582],[1853,563,1907,582],[227,679,281,698],[498,679,552,698],
               [1040,679,1094,698],[1311,679,1365,698],[227,795,281,814],[1040,795,1094,814])
reloadList = ([1613,12],[1558,95],[1143,609],[759,401],[1178,842])
src_path = "X:\\Users\\Alain\\Documents\\GitHub\\EHMTactics\\"
generation = int(sys.argv[1])
resultStart = int(sys.argv[2])


def randomPopulation():
    newPopulation = []
    for x in range(0,100):
        newGenes = []
        for y in range(0,18):
            for z in range(0,10):
                newGenes.append(random.randint(1,6))
            for z in range(0,3):
                newGenes.append(random.randint(0,2))
        newGenes.append(random.randint(1,6))
        newGenes.append(random.randint(1,5))
        newGenes.append(random.randint(1,4))
        newGenes.append(random.randint(1,7))
        newGenes.append(random.randint(1,5))
        newGenes.append(random.randint(1,4))
        newGenes.append(random.randint(1,5))
        newGenes.append(random.randint(1,4))
        newGenes.append(0)
        newGenes.append(0)
        newGenes.append(-1)
        newPopulation.append(Individual(newGenes))
    returnPop = Population(newPopulation)
    return returnPop

def runSimulation(sta, rs):
    counter = sta
    while counter < (working.getLength()-1):
        for y in range(counter,working.getLength()):
            print ('getting ' + str(y))
            if working.getIndividual(y)[244] < 0:
                print ('not done yet')
                break
            else:
                print ('done')
                counter += 1
        click(881, 353)
        time.sleep(0.5)
        if not (counter == 100):
            if not (rs == 1):
                print 'not starting with results'
                print ('starting with: ' + str(counter))
                setTactics(working.getIndividual(counter))
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 27:
                        sys.exit()
                vacation()
            r = getResults()
            rs = 0
            working.getIndividual(counter)[242] = r[0]
            working.getIndividual(counter)[243] = r[1]
            working.getIndividual(counter)[244] = r[2]
            save(working, generation)
            reloadGame()

def setTactics(ind):
    print("go to tactics and fill stuff in")
    ctypes.windll.user32.keybd_event(0x76, 0, 0, 0)  # F7 Down, go to tactics
    ctypes.windll.user32.keybd_event(0x76, 0, 0x0002, 0) #F7 up
    time.sleep(0.25)
    click(362,109) #personal tactics
    time.sleep(0.11)
    for x in range(0,18):
        get_region([1474,56,1538,76], 15, Image.BICUBIC)
        string = get_string((src_path + str(15) + "test.png"), 0)
        if (string == "Confirm"):
            click(61,(259+(23*x)))
            time.sleep(0.11)
            for y in range(0,10):
                z = 1
                while z < ind[x*13+y]:
                    click(1825,295+y*23)
                    time.sleep(0.11)
                    z += 1
            if ind[x*13+10] > 0:
                click(1573, 568)
                time.sleep(0.11)
                click(1325, 597)
                time.sleep(0.11)
            if ind[x*13+11] > 0:
                click(1651, 614)
                time.sleep(0.11)
            if ind[x*13+12] > 0:
                click(1651, 634)
                time.sleep(0.11)
            if msvcrt.kbhit():
                if ord(msvcrt.getch()) == 27:
                    sys.exit()
        else:
            sys.exit()
    click(225,110)
    time.sleep(0.11)
    print ("General tactics:")
    for x in range(0,8):
        click(1490,584+x*22)
        time.sleep(0.11)
        click(1324,568+ind[234+x]*22+x*22)
        time.sleep(0.11)
    click(643,465)
    time.sleep(0.11)
    click(1504, 66) #confirm
    time.sleep(0.11)
    #to be filled in

def vacation():
    for x in vacationList:
        click(x[0],x[1]) #click vacation buttons
        time.sleep(0.18)
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 27:
                sys.exit()
    for x in range(0,82):
        time.sleep(5) #wait x time
        print (str(x+1) + " of 82")
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 27:
                save(working, generation)
                sys.exit()
    get_region([79, 798, 111, 814], 15, Image.BICUBIC)
    string = get_string((src_path + str(15) + "test.png"), 3)
    print string
    x = 0
    while x < 60:
        if (string.find("Balance")) > -1:
            time.sleep(0.75)
            get_region([26, 797, 111, 814], 15, Image.BICUBIC)
            string = get_string((src_path + str(15) + "test.png"), 3)
            print string
            if (string.find("Balance")) > -1:
                time.sleep(0.75)
                get_region([26, 797, 111, 814], 15, Image.BICUBIC)
                string = get_string((src_path + str(15) + "test.png"), 3)
                print string
                if (string.find("Balance")) > -1:
                    time.sleep(0.75)
                    get_region([26, 797, 111, 814], 15, Image.BICUBIC)
                    string = get_string((src_path + str(15) + "test.png"), 3)
                    print string
                    if (string.find("Balance")) > -1:
                        time.sleep(0.75)
                        get_region([26, 797, 111, 814], 15, Image.BICUBIC)
                        string = get_string((src_path + str(15) + "test.png"), 3)
                        print string
                        if (string.find("Balance")) > -1:
                            break
        print ("Not yet done simming")
        time.sleep(1)
        get_region([26, 797, 111, 814], 15, Image.BICUBIC)
        string = get_string((src_path + str(15) + "test.png"), 3)
        print string
        x += 1

def reloadGame():
    print("click reload game buttons")
    time.sleep(0.11)
    for x in reloadList:
        click(x[0],x[1])
        time.sleep(0.11)
    get_region([1823,56,1882,76], 15, Image.BICUBIC)
    string = get_string((src_path + str(15) + "test.png"), 2)
    if (string == "Actions"):
        click2(reloadList[0][0], reloadList[0][1])
        for x in range(1, len(reloadList)):
            click(reloadList[x][0], reloadList[x][1])
            time.sleep(0.11)
    time.sleep(4)
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            sys.exit()
    #click reload game buttons
    #wait

def save(pop, i):
    print("saving generation " + str(i) + " to csv")
    with open(('gen' + str(i) + '.csv'), 'wb') as File:
        writer = csv.writer(File, delimiter=';')
        writer.writerows(pop.getFull())

def read(i):
    print 'reading'
    with open(('gen'+str(i)+'.csv'), 'rb') as File:
        reader = csv.reader(File, delimiter=';')
        readlist = []
        for row in reader:
            ind = Individual([])
            colNum = 0
            for col in row:
                if colNum == 244 or colNum == 243 or colNum == 242:
                    ind.append(float(col))
                else:
                    ind.append(int(col))
                colNum += 1
            readlist.append(ind)
    pop = Population(readlist)
    return pop

def get_region(box, i, extra):
    #Grabs the region of the box coordinates
    im = ImageGrab.grab(box)
    #Change size of image to 200% of the original size
    a, b, c, d = box
    doubleX = (c - a) * 2
    doubleY = (d - b) * 2
    im.resize((doubleX, doubleY), extra).save(os.getcwd() + "\\" + str(i) + "test.png", 'PNG')

def get_string(img_path, i):
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
    if (i == 1):
        string = '--psm 7 -c tessedit_char_whitelist=WL0123456789sot-'
    elif (i == 2):
        string = '--psm 7 -c tessedit_char_whitelist=Actions'
    elif (i == 3):
        string = '--psm 7 -c tessedit_char_whitelist=Balance'
    else:
        string = '--psm 7 -c tessedit_char_whitelist=Confirm'
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config=string)

    return result

def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

def click2(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.15)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

def getResults():
    time.sleep(0.5)
    goalsFor = 0
    goalsAgainst = 0
    failures = 0
    while failures < 3:
        click(368, 108)
        i = 1
        print('schedule click')
        try:
            for x in regionList2:
                # Grab the region of the screenshot (box area)
                #click(x[0],x[1])
                #time.sleep(0.25)
                region = (x[0],x[1],x[2],x[3])

                get_region(region, i, Image.BICUBIC)
                string = get_string((src_path + str(i) + "test.png"), 1)
                results = interpret(string)
                time.sleep(0.05)
                if (results[0]==-1):
                    get_region(region, i, Image.BILINEAR)
                    string = get_string((src_path + str(i) + "test.png"), 1)
                    results = interpret(string)
                    time.sleep(0.05)
                    if (results[0]==-1):
                        get_region(region, i, Image.ANTIALIAS)
                        string = get_string((src_path + str(i) + "test.png"), 1)
                        results = interpret(string)
                        time.sleep(0.05)
                        if (results[0]==-1):
                            results = [0,0]
                goalsFor = goalsFor + results[0]
                goalsAgainst = goalsAgainst + results[1]
                i += 1
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 27:
                        sys.exit()
            goalsFor = float(goalsFor)
            goalsAgainst = float(goalsAgainst)
            fitness = [goalsFor,goalsAgainst,(goalsFor/(goalsFor+goalsAgainst))]
            break
        except ValueError:
            print ("Error reading results")
            save(working, generation)
            fitness = [float(0),float(0),float(-1)]
            failures += 1
    print ('Fitness:')
    print fitness
    return fitness

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

x = 0
time.sleep(3)
while x < 10:
    sta = 0
    print sta
    print generation
    if generation > 1:
        working = read(generation)
    else:
        working = randomPopulation()
    runSimulation(sta, resultStart)
    resultStart = 0
    print ('resultStart is now ' + str(resultStart))
    print ("Old population has " + str(len(working.getFull())) + " before parent selection")
    newPop = working.selectParents()
    save(working, generation)
    print ("New population has " + str(len(newPop.getFull())) + " after parent selection")
    generation += 1
    newPop = newPop.breed(generation)
    print ("New population has " + str(len(newPop.getFull())) + " after breeding")
    x += 1
    working = newPop
    save(working, generation)
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            sys.exit()
