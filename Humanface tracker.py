import time

import cv2
import numpy as np

km.init()
Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

 Martin.streamon()
 Martin.takeoff()
 Martin.send_rc_control(0,0,25,0)
 time.sleep(2.2)
w,h=360,240
fowardbackwardrange[6200,6800]
pid=[0.4,0.4,0 ]
perror=0

def findface(image):
    facecascade=cv2.CascadeClassifier("Imagebank/Images/haarcascade_frontalface_default.xml")
    imagegray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    Faces=facecascade.detectMultiScale(imagegray,1.2,8)

Martinfacelist=[]
MartinfacelistArea=[]

for(x,y,w,h) in Faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2) #rectangle around the face
    cx=x+w//2
    cy=y+h//2
    area=w*h
    cv2.circle(image,(cx,cy),5,(0,255,0),cv2.FILLED)
    Martinfacelist.append([cx,cy])
    MartinfacelistArea.append(area)
if len(MartinfacelistArea)!=0:
    i=MartinfacelistArea.index(max(MartinfacelistArea))
    return image,[Martinfacelist[i],MartinfacelistArea[i]]
else:
    return image,[[0,0],0]
def facetrack(Martin,info,w,pid,perror):
     area=info[1]
     x,y=info[0]
     fowardbackward=0
     error=x-w//2
    speed=pid[0]*error+pid[1]*(error-perror)
    speed=int(np.clip(speed,-100,100))

    area=info[1]
    if area>fowardbackwardrange[0] and area < fowardbackwardrange[1]:
        fowardbackward=0
    if area>fowardbackwardrange[1]:
        fowardbackward=-20
    elif area < fowardbackwardrange[0] and area !=0:
        fowardbackward=20
    print(speed,fowardbackward)
    if x==0:
        speed=0
    Martin.send_rc_control(0,fowardbackward,o,speed)
    return error

capture = cv2.VideoCapture(0)

while True:
    _,image=capture.read()
    image=Martin.get_frame_read().frame
    image=cv2.resize(image,(w,h))
    print("centre", info[0],"Area",info[1])
    pError=facetrack(Martin, info, w, pid, perror)
    cv2.imshow("output",image)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        Martin.land()
        break