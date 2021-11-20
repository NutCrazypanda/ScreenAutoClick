import pyautogui
from pynput.keyboard import Key, Listener
import time


def on_press(key):
    #print('{0} pressed'.format(key))
    pass


def on_release(key):
    #print('{0} release'.format(key))
    global tstart,tstop
    if str(key) == "'s'":
        print("Start record screen click...")
        tstart = time.time()
    if str(key) == "'c'":

        tstop = time.time()
        delay = tstop - tstart
        print(pyautogui.position(),"delay = ",str(int(delay)))
        tstart = time.time()
        tstop  = 0
        x = str(pyautogui.position()).split("x=")
        x = x[1].split(",")
        y = x[1].split("y=")
        x = x[0]
        y = y[1].split(")")
        y = y[0]
        #print(x,y,1,str(int(delay)))
        outputfile = str(x)+" "+str(y)+" 1 "+str(int(delay))+"\n"
        f.write(outputfile)

    if key == Key.esc:
        # Stop listener
        f.close()
        return False

f = open("Coordinates.txt","w")
with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
