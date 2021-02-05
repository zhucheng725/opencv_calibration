from pathlib import Path

import numpy as np
import cv2

if __name__ == '__main__':

    img_dir = Path('/media/zhu/0003E52A000920B8/procedure/calibration/img')
    fnames = [str(f) for f in img_dir.glob('*.jpg')]
    fnames.sort()

    pattern_width = 7
    pattern_height = 7
    pattern_size = (pattern_width, pattern_height)
    horizontal_grid_dist = 10
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 100, 0.0001)

    corners = list()


    for row in range(pattern_height):
        for col in range(pattern_width):
            x = col*horizontal_grid_dist
            y = row * horizontal_grid_dist
            corners.append(np.array([x,y,0]).reshape(1,3).astype(np.float32))


    corners = np.vstack(corners).reshape(-1,3)
    #print('corners', corners)
    img_centers = list()
    obj_pts = list()
    iterate = 0
    for f in fnames:
        obj_pts.append(corners)
        img = cv2.imread(f)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        ret, centers = cv2.findCirclesGrid(gray, pattern_size, None, cv2.CALIB_CB_SYMMETRIC_GRID)
        #print('centers', centers)

        cv2.drawChessboardCorners(img, pattern_size, centers, centers is not None)
        cv2.imwrite('/media/zhu/0003E52A000920B8/procedure/calibration/newresult/' + str(iterate) + '.jpg', img)  
        iterate += 1
        #print('ret', ret)
        #print('f',f)
        if ret:
            img_centers.append(centers)
            


    retval, cam_mtx, dist_coeff, rvecs, tvecs = cv2.calibrateCamera(obj_pts, img_centers,(640, 480),None,None)  

    cam_data = {'cam_mtx':cam_mtx, 'dist_coeff':dist_coeff}
    print(cam_data)
    print("\nReporjection Error: {}".format(retval))






'''
import cv2

img = cv2.imread('/media/zhu/0003E52A000920B8/procedure/calibration/img/2.jpg')

_ = cv2.circle(img, (218, 156), 5, (0, 128, 255), -1)
_ = cv2.circle(img, (239, 154), 5, (0, 128, 255), -1)
_ = cv2.circle(img, (259, 153), 5, (0, 128, 255), -1)
_ = cv2.circle(img, (281, 152), 5, (0, 128, 255), -1)
_ = cv2.circle(img, (302, 151), 5, (0, 128, 255), -1)
_ = cv2.circle(img, (323, 151), 5, (0, 128, 255), -1)
_ = cv2.circle(img, (344, 151), 5, (0, 128, 255), -1)


cv2.imwrite('/media/zhu/0003E52A000920B8/procedure/calibration/img.jpg', img)


'''


