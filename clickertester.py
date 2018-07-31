import ctypes
import time

individual = [1,1,3,3,2,1,3,5,2,3,1,0,1,5,3,4,2,3,5,2,2,3,4,1,0,0,5,3,2,2,5,3,5,2,1,4,0,0,1,1,3,3,1,4,2,1,4,4,3,0,1,1,4,4,5,1,2,1,1,1,4,2,0,1,1,1,4,5,1,4,4,1,1,3,5,0,0,0,2,4,4,5,1,3,4,2,5,2,0,1,0,2,2,5,1,2,1,1,1,5,4,1,1,1,3,5,5,2,1,2,3,4,2,5,1,1,1,4,2,2,5,5,1,3,4,5,4,1,1,1,1,1,4,2,5,1,4,4,1,1,1,1,0,3,4,1,1,1,5,1,3,3,5,1,0,0,1,4,4,4,3,3,1,5,3,1,0,1,0,5,3,1,1,1,1,1,3,2,3,1,0,1,3,3,4,1,2,2,3,4,3,1,1,0,1,4,4,1,5,2,3,3,3,3,5,0,0,1,2,5,5,1,4,1,2,2,5,2,0,1,1,5,4,4,1,1,4,1,4,5,1,1,0,1,3,3,1,5,4,2,2,1,0.0,0.0,-3.0]


def setTactics(ind):
    click(881, 353)
    print("go to tactics and fill stuff in")
    ctypes.windll.user32.keybd_event(0x76, 0, 0, 0)  # F7 Down, go to tactics
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(0x76, 0, 0x0002, 0) #F7 up
    time.sleep(0.15)
    click(362,109) #personal tactics
    time.sleep(0.25)
    for x in range(0,3):
        click(61,(259+(23*x)))
        time.sleep(0.25)
        print ("Player " + str(x+1))
        for y in range(0,10):
            z = 1
            print(ind[x*13+y])
            while z < ind[x*13+y]:
                click(1825,295+y*23)
                time.sleep(0.25)
                z += 1
        print ind[x*13+10]
        print ind[x * 13 + 11]
        print ind[x * 13 + 12]
        if ind[x*13+10] > 0:
            click(1573, 568)
            time.sleep(0.25)
            click(1325, 597)
            time.sleep(0.25)
        if ind[x*13+11] > 0:
            click(1651, 614)
            time.sleep(0.25)
        if ind[x*13+12] > 0:
            click(1651, 634)
            time.sleep(0.25)
    click(225,110)
    time.sleep(0.15)
    print ("General tactics:")
    for x in range(0,8):
        click(1490,584+x*22)
        time.sleep(0.15)
        print ind[234+x]
        click(1324,568+ind[234+x]*22+x*22)
        time.sleep(0.15)
    click(643,465)
    time.sleep(0.15)
    click(1504, 66) #confirm
    time.sleep(0.15)
    #to be filled in

def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

setTactics(individual)