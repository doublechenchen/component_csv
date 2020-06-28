import cv2
import numpy as np
import os

img_path = '/media/cc/cc/t-less2/t_1/scene_sim/data/img/individual/'

img = np.zeros([480, 640, 3])

num_images = 10000

for m in range(0, num_images):
    x_min = 640 - 1
    y_min = 480 - 1
    x_max = 0
    y_max = 0
    im = cv2.imread(img_path + '{}_0.png'.format(m))

    for i in range(0,480):
        for j in range(0,640):
            if ((im[i][j][0] != 0) or (im[i][j][0] != 0) or (im[i][j][0] != 0)):
                x_min = min(j,x_min)
                x_max = max(j,x_max)
                y_min = min(i,y_min)
                y_max = max(i,y_max)
            else:
                x_min = x_min
                x_max = x_max
                y_min = y_min
                y_max = y_max
    box_txt = open('component_1.txt','a')
    box_txt.write('/home/cc/keras-retinanet/keras_retinanet/CSV/data/%s.jpg'%(m) +','+str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max)+','+'component_1')
    box_txt.write('\n')
    box_txt.close()




