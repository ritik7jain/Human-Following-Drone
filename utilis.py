from djitellopy import Tello
import cv2





def initializeTello():
    peter = Tello()
    peter.connect()
    peter.for_back_velocity=0
    peter.left_right_velocity = 0
    peter.up_down_velocity = 0
    peter.yaw_velocity = 0
    peter.speed = 0
    print(peter.get_battery())
    peter.streamoff()
    peter.streamon()
    return peter

def telloGetFrame(peter,w=360,h=240):
    myframe=peter.get_frame_read()
    myframe=myframe.frame
    img=cv2.resize(myframe,(w,h))
    return img