#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:16:10 2019

@author: carlos_urzua
"""

import cv2
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans,vq

image_raw = cv2.imread("afremov.jpeg", cv2.IMREAD_COLOR)

image_hsv = cv2.cvtColor(image_raw, cv2.COLOR_BGR2HSV)

def our_flatten(arr):
    return(arr.reshape(-1, arr.shape[-1]))
    
#image_hsv[:, :, 2] = 210
#image_hsv[:, :, 1] = 0
image_kmeans = KMeans(n_clusters=10, random_state=0).fit(our_flatten(image_hsv))
    


counter = 0
for i in range(len(image_hsv)):
    for j in range(len(image_hsv[i])):
        #print(image_hsv[i][j])
        cluster_nummer = image_kmeans.labels_[ counter ]
        image_hsv[i][j] = image_kmeans.cluster_centers_[cluster_nummer]
        counter += 1

        
image_bgr = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
        
cv2.imwrite('composition_afremov_sv.png', image_bgr)

cv2.imwrite('hsv_trump.png', image_hsv)