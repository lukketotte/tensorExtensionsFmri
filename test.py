import numpy as np

from nilearn import plotting as plot
from nilearn.image import smooth_img
from nilearn import image
from nilearn import datasets
import matplotlib.pyplot as plt

import os as os
import tensorflow as tf
import tensorly as tl

from tensorData import tensor as td
# ----------- ADD DATA ----------- #
adhdData = datasets.fetch_adhd(n_subjects = 2)
# list of 4D nifti file locations for each subject
funcFilenames = adhdData.func

img1 = smooth_img(funcFilenames[0], fwhm = "fast")
img2 = smooth_img(funcFilenames[1], fwhm = "fast")

x = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
y = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
x = img1.get_data()
y = img2.get_data()

# ------------- INSTANCE OF tensorData ------------- #
tdTest = td([x, y], [0,1,2], 3)
a = tdTest.niftyList
# this is fine
print(type(a[0]))
# print(type(a[1]))
# print(a[0][1,1,1,:])
# print(tdTest.idx_spatial)
tensor_cube = tdTest.unfoldTemporal()
# print(tensor_cube.shape)

# ----------- CHECK THE DATA ---------- #
t = np.array(range(0,176))
# print(tensor_cube[:,205000,1])
# plt.plot(t, tensor_cube[:,100000,1])
# plt.show()
# find the first position of non-zeroes
idx = 1
for i in range(100500, 101000):
	if(np.count_nonzero(tensor_cube[:, i, 0]) > 0):
		idx = i
		print("Found value: col %d" % i)
		break

a = tensor_cube[:, 100500, 0]
# this is a problem... to much casting. Not sure what is happening
print(type(a))
#print(type(t))
#plt.plot(t,a)
#plt.show()

# going to test spatialMean function and check time
xt = np.array(range(0,176))

from datetime import datetime
startTime = datetime.now()

xt = tdTest.spatialMean(tensor_cube, 0)
print(datetime.now() - startTime)
plot(t, xt)
plot.show()