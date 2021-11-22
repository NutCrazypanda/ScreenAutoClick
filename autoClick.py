import sys
import pyautogui
from pynput.keyboard import Key, Listener
import threading
from time import sleep


thread_list =[]

def clicker(numberOfIterations, coords):
    while True:
        for _ in range(numberOfIterations):
            for i in coords:
                x = i[0]
                y = i[1]
                n = i[2]
                t = i[3]
                a = i[4]

                for __ in range(int(n)):
                    pyautogui.moveTo(int(x), int(y), duration=int(t))
                    if a == 'c':
                        pyautogui.mouseDown()
                        #pyautogui.moveTo(int(x),int(y)+100)
                        pyautogui.mouseUp()
                        print("clicked (" + str(x) + "," + str(y) + ")")
                    if a == 's':
                        pyautogui.scroll(-150)
                        print("scroll down (" + str(x) + "," + str(y) + ")")

        sleep(looptimer)

def listen():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
    #print('{0} pressed'.format(key))
    pass


def on_release(key):
    #print('{0} release'.format(key))

    if str(key) == "'s'":
        print("Starting autoclick...")
        thread = threading.Thread(target=clicker,args=( numberOfIterations ,coords, ) )
        thread_list.append(thread)
        thread.start()

    if key == Key.esc:
        # Stop listener
        print("Stop")
        return False


numberOfIterations = 1
coords = []

if len(sys.argv) > 1:
    if(sys.argv[1] == "-f"):
        coordinatefile = sys.argv[2]
else:
    coordinatefile = "Coordinates.txt"
try:
    f = open(coordinatefile,"r")

    try:
        for i in f.readlines():
            coords.append(i.split())
    except:
        print("Error!\nCoordinates.txt file is empty!")
        exit(0)

except:
    print("Error!\nCoordinates.txt file not found!")
    exit(0)

print("=== ScreenAutoClick v.0.3 ===")
looptimer = input("Do auto click every(sec) [enter 0 for no timer] : ")
looptimer = int(looptimer)
print("Press 's' to start...")
thread1 = threading.Thread(target=listen)
thread_list.append(thread1)
thread1.start()
