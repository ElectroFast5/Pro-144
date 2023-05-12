# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
mountain=cv2.resize(mountain,(640,480))

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])
        mask1=cv2.inRange(frame_rgb,lower_bound,upper_bound)

        # thresholding image
        mask1=cv2.bitwise_not(mask1)
        # inverting the mask
        res1=cv2.bitwise_and(frame,frame,mask=mask1)
        # bitwise and operation to extract foreground / person
        #res2=cv2.bitwise_and(mountain,mountain,mask=mask1)
        # final image
        final_img=np.where(res1==0,mountain,res1)
        # show it
        cv2.imshow('frame' , final_img)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()