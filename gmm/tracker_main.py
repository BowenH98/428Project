import os
import cv2
from detect_occlusion import detect_occlusion



def draw_images(image_name, depth_image_name=None, start_point=None, end_point=None):
    image = cv2.imread(image_name)
    color = (255, 0, 0)
    if start_point != None:
        start_point = (start_point[0], start_point[1])
        end_point = (end_point[0], end_point[1])
        thickness = 2
        depth_image = cv2.imread(depth_image_name)
        occlusion, x, y = detect_occlusion(depth_image, start_point, end_point)
        if occlusion:
           color = (255,255,255) 
        image = cv2.rectangle(image, start_point, end_point, color, thickness) 
        cv2.imshow('bear_front',image)
        cv2.waitKey(100)
    else:
        print(1)
        # cv2.imshow('bear_front',image)

def get_tracker_position(path):
    position_list = []
    file_name = path + 'bear_front.txt'
    f = open(file_name, "r")
    position_list = f.read().splitlines()
    return position_list


if __name__ == "__main__":
    path = '/Applications/CMPUT428/project/PPT/ValidationSet/bear_front/rgb/' 
    depth_path = '/Applications/CMPUT428/project/PPT/ValidationSet/bear_front/depth/'  
    position_list = get_tracker_position('/Applications/CMPUT428/project/PPT/ValidationSet/bear_front/')
    for index in range(34,200):
        image_name = path + str(index+1) + '.png' 
        depth_image_name = path + str(index) + '.png' 
        position_info = position_list[index].split(',')
        print(position_info)
        try:
            start_point = [int(position_info[0]), int(position_info[1])]
            end_point = [int(position_info[0]) + int(position_info[2]),int(position_info[1]) + int(position_info[3])]
            draw_images(image_name, depth_image_name, start_point, end_point)
        except:
            draw_images(image_name)