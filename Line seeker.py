
import numpy as np
from djitellopy import tello
import cv2
Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

Martin.streamon()
Martin.takeoff()
hugesaturationvalues=[0,0,117,179,22,219]
sensors=3
threshold=0.2
width,height=480,360
capture=cv2.VideoCapture(1)
sensitivity=3
weights=[-25,-15,0,15,25]
curve=0
fowardspeed=10

def thresholding(image):
    hugesaturationvalue=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    lower=np.array([ hugesaturationvalue[0], hugesaturationvalue[1], hugesaturationvalue[2]])
    upper = np.array([hugesaturationvalue[3], hugesaturationvalue[4], hugesaturationvalue[5]])
    mask=cv2.inRange(hugesaturationvalue,lower,upper)
    return mask
def getcontours(image_threshold,image):
    contours ,hierachy=cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if len(contours)!=0:
        biggest=max(contours,key=cv2.contourArea())
        x,y,w,h=cv2.boundingRect(biggest)
        centrex=x+w//2
        centrey=y+h//2
        cv2.drawContours(image,contours,-1,(255,0,255),7)
        cv2.circle(image,(centrex,centrey),10,(0,255,0),cv2.FILLED)
    return centrex
def getSensorOutput(image_threshold,sensors):
    images=np.hsplit(image_threshold,sensors)#make sure image size is divisible by 3
    totalpixels=image.shape[1]//sensors*image.shape[0]
    for im in enumerate(images):
        pixelcount=cv2.countNonZero(im)
        if pixelcount>threshold*totalpixels:
            sendout.append[1]
        else:
            sendout.append[0]
        cv2.imshow(str(x), im)
    print(sendout)
    return  sendout

def sendcommands(sendout,centrex):
    '''translations'''
    global curve
    lr=centrex-width//2//sensitivity
    lr=int(np.clip(lr,-10,-10))

    if lr<2 and lr>-2:lr=0

    # rotation
    if sendout==[1, 0, 0]:curve=weights[0]
    elif sendout == [1, 1, 0]: curve = weights[1]
    elif sendout == [0, 1, 0]: curve = weights[2]
    elif sendout == [0, 1, 1]: curve = weights[3]
    elif sendout == [0, 0, 1]: curve = weights[4]

    elif sendout == [0, 0, 0]: curve = weights[2]
    elif sendout == [1, 1, 1]: curve=weights[2]
    elif sendout == [1, 1, 1]: curve=weights[2]

    Martin.send_rc_control(lr,fowardspeed,0,curve)


while True:
    -,image=capture.read()
    image=cv2.resize(image,(width,height))
    image=cv2.flip(image,0)

    image_threshold=thresholding(image)#For translation
    sendout=getSensorOutput(image_threshold,sensors)#rotation
    centrex=getContours(image_threshold,image)
    sendcommands(sendout,centrex)
    cv2.imshow("output",image)
    cv2.waitKey(1)