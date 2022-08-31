import Keyboard
import cv2
import numpy as np
from djitellopy import tello
import KeyboardModule as km
from time import sleep
import math

#PARAMETERS
fowardspeed=120/10 #foward speed in cm/s
angularspeed=360/10#angular speed Degree/s
interval=0.25

distanceinterval=fowardspeed*interval
angularinterval=angularspeed*interval
#########
km.init()
Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

points=[(0,0),(0,0)]
def getkeyboardInput():
    lr,fb,up,yv=0,0,0,0
    speed=50
    d=0
    global x,y,yaw,a
if km.getkey("LEFT"):
    lr=-speed
    d= distanceinterval
    a= -180
elif km.getkey("RIGHT"):
    lr=-speed
    d = -distanceinterval
    a = 180


if km.getkey("UP"):
    fb=speed
    d = distanceinterval
    a = 270
elif km.getkey("DOWN"):
    fb=-speed
    d = -distanceinterval
    a = -90

if km.getkey("w"):
    up=speed
elif km.getkey("s"):
    up=-speed

if km.getkey("a"):
    yv=speed
    yaw -=ainterval
elif km.getkey("d"):
    yv=-speed
    yaw+=ainterval

if km.getkey("q"): yv = Martin.land()
if km.getkey("t"): yv = Martin.takeoff(

a+=yaw

x+= int(d*math.cos(math.radians(a))
y+= int(d*math.cos(math.radians(a))
return[lr,fb,up,yv,x,y]

def drawpoints(image,points):
    for pointsin points:
        cv2.circle(image(points[0],points[1]),20,(0,0,255),cv2.FILLED)
    cv2.putText(image,f'({points[-1][0]-500)/100},{(points[-1[1]-500)/100})m',(points[-1][0]+10,points[-1][0]+30),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1 )
while True:
    touch=getKeyboardInput()
    Martin.send_rc_control(touch[0],touch[1],touch[2],touch[3])\
    image=np.zeros((1000,1000,3),np.uint8)
    if(points[-1][0]!=touch[4] or points[-1][1] !=touch[5]):
        points.append((touch[4],touch[5]))
    drawpoints(image,points)
    cv2.imshow("output",image)
    cv2.waitkey(1)
