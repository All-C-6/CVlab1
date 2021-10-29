# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:45:57 2021

@author: ilyan
"""

import numpy as np

image1 = open('img1.txt')
image2 = open('img2.txt')

a1 = np.loadtxt(image1, skiprows=1)
a2 = np.loadtxt(image2, skiprows=1)

image1.close()
image2.close()

nz1 = np.nonzero(a1)
nz1y = nz1[0]
nz1x = nz1[1]
nz2 = np.nonzero(a2)
nz2y = nz2[0]
nz2x = nz2[1]
'''
Проверка объектов на соответствие
if nz1x.size != nz2x.size:
    print("Объекты не равны")
else:
    for k in nz1x:
        t = nz1x[0]-nz2x[0]
        if nz1x[k]-nz2x[k] != t:
            print("Объекты не равны")
            break
  '''      
shiftX = nz1x[0]-nz2x[0]
shiftY = nz1y[0]-nz2y[0]
print("Объект сдвинут по осям X и Y на", shiftX,'и', shiftY )


    



