#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:37:20 2019

@author: carlos_urzua 
"""

from PIL import Image
import math

long="/Users/carlos_urzua/Desktop/big_data/vitral_voronoi/voronoi_data.csv"

with open(long) as f:
    created = False
    for line in f:
        record = line.strip().split(",")
        if created:
            x, y, = [int(x) for x in record[:2]]
            color = record[2]
            r, g, b = [int(x) for x in color.split("_")]
            print(x,y,color)
            nx.append(x)
            ny.append(y)
            nr.append(r)
            ng.append(g)
            nb.append(b)
        else:
            created = True
            width, height = [int(x) for x in record[:2]]
            image = Image.new("RGB", (width, height))
            putpixel = image.putpixel
            imgx, imgy = image.size
            nx = []
            ny = []
            nr = []
            ng = []
            nb = []
            
for y in range(imgy):
    for x in range(imgx):
        dmin = math.hypot(imgx-1, imgy-1)
        j = -1
        for i in range(len(nx)):
            d = math.hypot(nx[i]-x, ny[i]-y)
            if d < dmin:
                dmin = d
                j = i
        putpixel((x, y), (nr[j], ng[j], nb[j]))
        
        
image.save("VoronoiDiagram.png", "PNG")

