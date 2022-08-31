import Keyboard
from djitellopy import tello
import KeyboardModule as km
import cv2
import time

km.init()
Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

Martin.streamon()

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

    if km.getkey('z'):
        cv2.imwrite(f'Imagebank/Images/{time.time()}.jpg',img)
        time.sleep(0.5)
    return [lr,fb,up,yv]

while True:
    touch=getKeyboardInput()
    Martin.send_rc_control(touch[0],touch[1],touch[2],touch[3]) \
    image = Martin.get_frame_read().frame
    image.cv2.resize(image(360, 240))
    cv2.imshow("image", image)
    cv2.waitKey(1)
