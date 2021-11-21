import time
import pyautogui
from pynput.mouse import Listener
from pynput.keyboard import Listener as kListener
from pynput.keyboard import Key


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
        m_listener.stop()
        return False

def on_click(x, y, button, pressed):
    try:
        global tstart, tstop
        tstop = time.time()
        delay = tstop - tstart
        if delay <= 0:
            delay = 1
        if pressed:
            print("click",x,y, "delay = ", str(int(delay)))
        tstart = time.time()
        tstop = 0
        outputfile = str(x) + " " + str(y) + " 1 " + str(int(delay)) + " c \n"
        f.write(outputfile)
    except:
        print("Press 's' to start click record...")
def on_scroll(x, y, dx, dy):
    try:
        global tstart, tstop
        tstop = time.time()
        delay = tstop - tstart
        if delay <= 0:
            delay = 1
        print("scroll",x,y, "delay = ", str(int(delay)))
        tstart = time.time()
        tstop = 0

        outputfile = str(x) + " " + str(y) + " 1 " + str(int(delay)) + " s\n"
        f.write(outputfile)
    except:
        print("Press 's' to start click record...")

f = open("Coordinates.txt","w")
print("Press 's' to start click record...")
with kListener(on_release=on_release) as k_listener, \
        Listener(
        on_click=on_click,
        on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()
