

import cv2
import numpy as np
import math

fx = 350.87414617
fy = 351.96190768
cx = 308.62439269
cy = 252.00054404
    
k1 = -0.32577347
k2 = 0.10924895
p1 = 0.00087971
p2 = -0.00119745
k3 = -0.01607096
    
mtx = np.array([[fx,0,cx],[0,fy,cy],[0,0,1]], dtype = np.float32)
dist = np.array([[k1,k2,p1,p2,k3]], dtype = np.float32)
    

image_width = 3357
image_height = 823
origin_x = -3.206279 
origin_y = -9.831287

#rviz tf可得 
robot_X = 0
robot_Y = 0
robot_Z = 0.0150683
robot_W = 0.999886
#rviz tf可得 
robot_pos_x = 49.1106
robot_pos_y = 12.065



cap0 =  cv2.VideoCapture('/dev/video0')
#img = cv2.imread('/home/nvidia/procedure/img/img/1.jpg')


global h2

h2 = 0

#origin_x, origin_y为.yml文件中可得
#robot_pos_x,robot_pos_y为rviz中tf的position数值可得
def trans2positon(origin_x, origin_y, robot_pos_x, robot_pos_y, image_height):

    focal_robot_location_x_pixel = int((abs(origin_x) + robot_pos_x)/0.05)
    focal_robot_location_y_pixel = int(image_height - (abs(origin_y) + robot_pos_y)/0.05)
    #focal_robot_location_x_pixel = int((abs(int(origin_x)) + robot_pos_x)/0.05)
    #focal_robot_location_y_pixel = int(image_height - int(abs(int(origin_y) + robot_pos_y)/0.05))

    return focal_robot_location_x_pixel, focal_robot_location_y_pixel


#w, x, y, z 为rviz中tf数值可得
def to_euler_angles(w, x, y, z):
    """w、x、y、z to euler angles"""
    angles = {'pitch': 0.0, 'roll': 0.0, 'yaw': 0.0}
    #r = math.atan2(2*(w*x+y*z),1-2*(x*x+y*y))
    #p = math.asin(2*(w*y-z*z))
    y = math.atan2(2*(w*z+x*y),1-2*(z*z+y*y))
    #
    #angles['roll'] = r*180/math.pi
    #angles['pitch'] = p*180/math.pi
    angles['yaw'] = y
    #
    return angles['yaw'] 

#distance为目标距离值,可以通过测距公式可得:ceju
#theta 为 to_euler_angles可得
#focal_robot_location_x_pixel, focal_robot_location_y_pixel 为 trans2positon 可得
def obj_trans_location(distance, obj_theta, robot_theta, focal_robot_location_x_pixel, focal_robot_location_y_pixel):
    theta =  robot_theta - obj_theta
    print('robot_theta',robot_theta / math.pi * 180,' 度')
    print('final theta', theta / math.pi * 180,' 度')
    #print('robot_theta ,obj_theta', robot_theta , obj_theta)
    if theta <= 2*math.pi and theta > math.pi:
        theta  = theta - 2*math.pi
    elif theta >= -2*math.pi and theta < -1*math.pi:
        theta  = 2*math.pi - theta 
    print('最后 theta', theta / math.pi * 180,' 度')

    if theta >0 and theta <= math.pi/2:
        theta = abs(theta)
        obj_x_pixel = math.cos(theta) * distance/0.05 + focal_robot_location_x_pixel
        obj_y_pixel = -1 * math.sin(theta) * distance/0.05  + focal_robot_location_y_pixel
    elif theta > math.pi/2 and theta <= math.pi:
        theta = abs(theta)
        obj_x_pixel = -1 * math.cos(math.pi - theta) * distance/0.05   + focal_robot_location_x_pixel
        obj_y_pixel = -1 * math.sin(math.pi - theta) * distance/0.05  + focal_robot_location_y_pixel
    elif theta > -1 * math.pi and theta <= -1 * math.pi/2:
        theta = abs(theta)
        obj_x_pixel = -1 * math.cos(math.pi - theta) * distance/0.05   + focal_robot_location_x_pixel
        obj_y_pixel =  math.sin(math.pi - theta) * distance/0.05  + focal_robot_location_y_pixel
    elif theta >= -1/2 * math.pi and theta <= 0:
        theta = abs(theta)
        obj_x_pixel = math.cos(theta) * distance/0.05  + focal_robot_location_x_pixel
        obj_y_pixel = math.sin(theta) * distance/0.05  + focal_robot_location_y_pixel

    return int(obj_x_pixel), int(obj_y_pixel)


#求出目标像素值相对机器人的转向角
def obj_theta_trans(distance, u):
    theta = (u - cx)/fx
    obj_theta = np.arctan(theta)
    print('obj_theta:',obj_theta / math.pi * 180,' 度')
    return obj_theta


#F1为焦距, H1为摄像头高度, Y1为地面点到光轴点距离
def ceju(F1, H1, Y1):
    x = H1*F1/Y1
    print('distance:',x)
    #y = 0.4014959 + 1.39404*x -0.188427*x**2  + 0.02550385*x**3
    #y = 2.149 - 0.2923*x + 0.201846*x**2 
    y = -1.37816289 + 1.73089188*x #回归方程
    return y
    

#robot_x_pixel为机器人x轴的图像像素值
#robot_y_pixel为机器人y轴的图像像素值
#obj_x_pixel 为图像目标x轴的图像像素值
#obj_y_pixel 为图像目标y轴的图像像素值
def plotimg(robot_x_pixel, robot_y_pixel, obj_x_pixel, obj_y_pixel):
    frame = cv2.imread('./mmwr_tw.pgm',1)
    cv2.circle(frame, (robot_x_pixel, robot_y_pixel), 10, (0,0,255), -1)
    cv2.circle(frame, (obj_x_pixel, obj_y_pixel), 10, (255,0,255), -1)
    cv2.imwrite('./result.jpg', frame)
    print('imwrite finished')


def main():
    x = 394#指定x轴某目标的像素值
    y = 269#指定y轴某目标的像素值
    frame3 = cv2.imread('/media/zhu/UBUNTU 16_0/zc/mmwr/img/1.jpg')
    point_arr = np.array([[x, y]], dtype = np.float32)
    projector_point = cv2.undistortPoints(point_arr, mtx, dist, None, mtx)#去畸变
    h2 = projector_point[0][0][1]
    print('pixel height:', abs(h2 - cy))
    H1 = 0.73 
    Y1 = abs(h2 - cy)
    F1 = 2.91*1000/8.3
    juli = ceju(F1, H1, Y1)
    print('regression distance:', juli)
        
    robot_theta = to_euler_angles(w = robot_W, x = robot_X, y = robot_Y, z = robot_Z)
    print('robot_theta', robot_theta)
    focal_robot_location_x_pixel, focal_robot_location_y_pixel = trans2positon(origin_x = origin_x, origin_y = origin_y, robot_pos_x = robot_pos_x, robot_pos_y = robot_pos_y, image_height = image_height)
    print('focal_robot_location_x_pixel,focal_robot_location_y_pixel', focal_robot_location_x_pixel, focal_robot_location_y_pixel)

    obj_theta = obj_theta_trans(distance = juli, u = projector_point[0][0][0])

    obj_x_pixel, obj_y_pixel = obj_trans_location(distance = juli, obj_theta = obj_theta, robot_theta = robot_theta, focal_robot_location_x_pixel = focal_robot_location_x_pixel, focal_robot_location_y_pixel = focal_robot_location_y_pixel)
    print('obj_x_pixel, obj_y_pixel', obj_x_pixel, obj_y_pixel)
    plotimg(robot_x_pixel = focal_robot_location_x_pixel, robot_y_pixel = focal_robot_location_y_pixel, obj_x_pixel = obj_x_pixel, obj_y_pixel = obj_y_pixel)
            
     
        
 
if __name__ == "__main__":
    main()
        
        
        
        
