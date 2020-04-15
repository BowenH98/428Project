import cv2
import numpy as np
import os
img_array = []
path = '/Applications/CMPUT428/project/rgbd_tracking/tracking_milkcan/tracking_milkcan/' 
for count in range(0,733):
    filename = path + str(count) + '_rgb.png'
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('tracking_milkcan.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()