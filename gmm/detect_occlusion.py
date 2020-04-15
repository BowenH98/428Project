import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math
from sklearn import mixture
import matplotlib.pyplot
import matplotlib.mlab
import scipy.stats
from sklearn.mixture import GaussianMixture
print('Done')

def detect_occlusion(image, start_point, end_point):
    occlusion = False
    tracking_box = image[start_point[0]:end_point[0],start_point[1]:end_point[1]]
    data = tracking_box.ravel().reshape([-1, 1]) 
    gmm = GaussianMixture(n_components=3)
    gmm.fit(data)
    m = gmm.means_
    w = gmm.weights_
    c = gmm.covariances_
    max_m = 0
    max_index = 0
    for index in range(0,3):
        temp_m = m[index][0]
        if temp_m > max_m:
            max_m = temp_m
            max_index = index
        # temp_c = c[index][0][0]
        # for 
        # h = h + scipy.stats.norm(m[index][0], c[index][0][0]).pdf(z)*w[index]
    if np.ndarray.max(c) == c[index][0][0]:
        occlusion = True
    
    x = []
    y = []
    for z in range(1,266):
        h = 0
        for index in range(0,3):
            h = h + scipy.stats.norm(m[index][0], c[index][0][0]).pdf(z)*w[index]
        x.append(z)
        y.append(h)
    
    # plt.plot(x,y)
    return occlusion, x, y
