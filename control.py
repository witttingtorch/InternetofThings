import Keyboard
from djitellopy import tello
import KeyboardModule as km

km.init()
Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

def getkeyboardInput():
    lr,fb,up,yv=0,0,0,0
    speed=50

if km.getkey("LEFT"):lr=-speed
elif km.getkey("RIGHT"):lr=-speed

if km.getkey("UP"):fb=speed
elif km.getkey("DOWN"):fb=-speed

if km.getkey("w"):up=speed
elif km.getkey("s"):up=-speed

if km.getkey("a"):yv=speed
elif km.getkey("d"):yv=-speed

if km.getkey("q"): yv = Martin.land()
if km.getkey("t"): yv = Martin.takeoff()

return[lr,fb,up,yv]
while True:
    touch=getKeyboardInput()
    Martin.send_rc_control(touch[0],touch[1],touch[2],touch[3])\
    sleep(0.05)
