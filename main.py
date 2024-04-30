import cv2
from djitellopy import tello
import cvzone
import time 
 

drone = tello.Tello()
drone.connect() 

imgthold = 0.6
nmsthold = 0.2
classNames = []
classFile = "coco.names"
with open(classFile, 'rt') as file:
    classNames = file.read().split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(configPath,weightPath)

net.setInputSize(320,320)
net.setInputScale(1.0/ 120)
net.setInputMean((120, 120, 120))
net.setInputSwapRB(True)



print(f"Battery: {drone.get_battery()}%")
time.sleep(2)

drone.streamoff()

drone.streamon()





while True:
    img = drone.get_frame_read().frame

    classIds, confs, bbox = net.detect(img,confThreshold=imgthold, nmsThreshold=nmsthold)
    try:
        for classId, conf, box in zip(classIds.flatten(),confs.flatten(), bbox):
            print(classId,conf, box)
            cvzone.cornerRect(img, box, rt=0)

            cv2.putText(img, f"{classNames[classId-1].upper()} {round(conf*100,2)}%", (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1,(251, 255, 0),2)
    except:
        pass

    drone.send_rc_control(0,0,0,0)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("Drone Image Detection", img_rgb)
    key = cv2.waitKey(1)
