from djitellopy import tello
import  cv2

Martin=tello.Tello()
Martin.connect()
print(Martin.get_battery())

Martin.streamon()

while True:
    image=Martin.get_frame_read().frame
    image.cv2.resize(image(360,240))
    cv2.imshow("image",image)
    cv2.waitKey(1)