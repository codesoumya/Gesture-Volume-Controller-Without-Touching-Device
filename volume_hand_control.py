'''
Production of CodeSoumya

E-mail - soumyadipbubul@gmail.com
whatsApp - 7797807565

These are dependency for this project. install this packages before use this app 


pip install opencv-python
pip install numpy
pip install mediapipe
pip install pycaw

please follow comments to under stand the code 

'''
import cv2
import time
import numpy as np
import handTracxkingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam , hCam = 600, 500

cap = cv2.VideoCapture(0) # use argument value 0 for inbuilt webCam for external web cam change the value
cap.set(3, wCam)
cap.set(4, hCam)

cTime = 0
pTime = 0

detector = htm.handDetector()


##################################################################################################################
########################################## Volume Control Section ################################################

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# xxx =volume.GetMasterVolumeLevel()
vo_range= volume.GetVolumeRange()
low_range = vo_range[0]
high_range = vo_range[1]

#################################################################################################################
#################################################################################################################




# ############ Distance between two coordinates ################
def distance_dt(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))


print("Work going on...")
while True:
    success, img = cap.read()
    img = detector.findHands(img,draw=False)               # For showing the hand line detection enable draw agrgument as True
    lm = detector.findPosition(img,draw=False)             # For showing hand key points and key id`s enable draw argument as True


# #############################        FPS CALCULATION PART #################################3
    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime


    # //////////Showing the fps
    # cv2.putText(img,"FPS : "+str(int(fps)),(20,30),cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0),2)

    if len(lm)!=0:
        # print("Thumb : ",lm[4],"Index tip : " ,lm[8],"\n")

        x1, y1 = lm[4][1], lm[4][2]  # coordinates of thumb tip
        x2, y2 = lm[8][1], lm[8][2]  # coordinates of index tip

        sx1 , sy1 = lm[0][1], lm[0][2]  # coordinates of base
        sx2 , sy2 = lm[9][1], lm[9][2]  # coordinates of middle finger pip

        standard_dist = distance_dt(sx1,sy1,sx2,sy2)  # the distance between key 0 and 9 (base and middle finger pip) aproximately non changeble so its our standard scale
        distance_tip = distance_dt(x1,y1,x2,y2)      # distance between thumb tip and index tip
        my_mejor = (distance_tip/standard_dist)*100  # standard scaleing major

        # 140 - 35
        vol = np.interp(my_mejor,[35,140],[low_range,high_range])
        volume.SetMasterVolumeLevel(vol, None)


        # print(vol)
        # print("index dist",distance_tip)
        # print("standard dist", standard_dist)

        #############################  OTHERS DATA SHOWING ON SCREEN ############################3

        # cv2.putText(img,"Distance btw tips : "+str(my_mejor),(20,60),cv2.FONT_HERSHEY_COMPLEX,1, (255,0,0),2)
        # cv2.putText(img,"st dist : "+str(standard_dist),(20,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,0,255),2)

        # cv2.circle(img,(x1,y1),5,(255,255,0),cv2.FILLED)
        # cv2.circle(img,(x2,y2),5,(255,255,0),cv2.FILLED)
        # cv2.line(img, (x1,y1),(x2,y2),(230,120,0),2)

        # cv2.circle(img,(sx1,sy1),5,(25,255,0),cv2.FILLED)
        # cv2.circle(img,(sx2,sy2),5,(25,255,0),cv2.FILLED)
        # cv2.line(img, (sx1,sy1),(sx2,sy2),(0,220,0),2)
        

    # cv2.imshow("imaGE",img)   # showing the image 
    cv2.waitKey(1)