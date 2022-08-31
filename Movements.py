from djitellopy import tello
from time import sleep

Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

Martin.send_rc_control(0,50,0,0)
sleep(2)
Martin.send_rc_control(0,0,0,0)
Martin.land()