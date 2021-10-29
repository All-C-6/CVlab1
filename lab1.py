# -*- coding: utf-8 -*-
import numpy as np

image1 = open('figure1.txt')
image2 = open('figure2.txt')
image3 = open('figure3.txt')
image4 = open('figure4.txt')
image5 = open('figure5.txt')
image6 = open('figure6.txt')

size1 = float(image1.readline())
size2 = float(image2.readline())
size3 = float(image3.readline())
size4 = float(image4.readline())
size5 = float(image5.readline())
size6 = float(image6.readline())

a1 = np.loadtxt(image1, skiprows=1)
a2 = np.loadtxt(image2, skiprows=1)
a3 = np.loadtxt(image3, skiprows=1)
a4 = np.loadtxt(image4, skiprows=1)
a5 = np.loadtxt(image5, skiprows=1)
a6 = np.loadtxt(image6, skiprows=1)


image3.close()
image4.close()
image5.close()
image6.close()

b1 = np.array(a1.shape)
b2 = np.array(a2.shape)
b3 = np.array(a3.shape)
b4 = np.array(a4.shape)
b5 = np.array(a5.shape)
b6 = np.array(a6.shape)

print("Номинальное разрешение image1:", round(size1/b1[0], 4))
print("Номинальное разрешение image2:", round(size2/b2[0], 4))
print("Номинальное разрешение image3:", round(size3/b3[0], 4))
print("Номинальное разрешение image4:", round(size4/b4[0], 4))
print("Номинальное разрешение image5:", round(size5/b5[0], 4))
print("Номинальное разрешение image6:", round(size6/b6[0], 4))
