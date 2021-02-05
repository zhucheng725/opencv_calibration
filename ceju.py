

import cv2
import numpy as np

point_arr = np.array([[[283, 281]]], dtype=np.float32)

fx = 350.87414617
fy = 351.96190768
cx = 308.62439269
cy = 252.00054404

k1 = -0.32577347
k2 = 0.10924895
p1 = 0.00087971
p2 = -0.00119745
k3 = -0.01607096

mtx = np.array([[fx, 0, cx],[0, fy, cy],[0, 0, 1]], dtype=np.float32)
dist = np.array([[k1, k2, p1, p2, k3]], dtype=np.float32)

projector_points_fixed = cv2.undistortPoints(point_arr, mtx, dist,None, mtx)
new_u = projector_points_fixed[0][0][0] 
new_v = projector_points_fixed[0][0][1] 

print('new_u',new_u)
print('new_v',new_v)

print('new_x_cor',(new_u-cx)/ fx)
print('new_y_cor',(new_v-cy)/fy)

xp = 0.73 * fy/ (new_v - cy)
yp = xp * (cx - new_u) /fx
print(xp, yp)

img = cv2.imread('/media/zhu/0003E52A000920B8/procedure/calibration/test/1.jpg')
dst = cv2.undistort(img, mtx, dist, None)
cv2.imwrite('/media/zhu/0003E52A000920B8/procedure/calibration/dst.jpg', dst)

















