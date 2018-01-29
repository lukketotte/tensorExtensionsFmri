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
adhdData = datasets.fetch_adhd(n_subjects = 30)
# list of 4D nifti file locations for each subject
funcFilenames = adhdData.func

print(funcFilenames[0])

img1 = smooth_img(funcFilenames[0], fwhm = "fast")
img2 = smooth_img(funcFilenames[1], fwhm = "fast")
img3 = smooth_img(funcFilenames[2], fwhm = "fast")
img4 = smooth_img(funcFilenames[7], fwhm = "fast")

# x = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
# y = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
x = img1.get_data()
y = img2.get_data()
z = img3.get_data()
w = img4.get_data()
#print(y.shape) # (61,73,61,176)
#print(x.shape) # (61,73,61,176)
#print(z.shape) # (61,73,61,176)
print(w.shape) # (61,73,61,175)
# many observations have different shapes
# not sure what to do about that. That seems 
# to imply that the procedure for subject is
# not the same as for the others. Check the extra
# CSV with site information. Perhaps that the sites
# are adhering to slightly different protocols and 
# have differing equipment

# ------------- INSTANCE OF tensorData ------------- #
# w & y has no data?
# ERROR: every even position has no data
tdTest = td([z, x, y], [0,1,2], 3)
a = tdTest.niftyList
# this is fine
print(type(a[0]))
# print(type(a[1]))
# print(a[0][1,1,1,:])
# print(tdTest.idx_spatial)
tensor_cube = tdTest.unfoldTemporal()
#271633, the dimensions are correct
print(tensor_cube.shape)


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
		#print("Found value: col %d" % i)
		break

#a = tensor_cube[:, 100500, 0]
# this is a problem... to much casting. Not sure what is happening
#print(type(a))
#print(type(t))
#plt.plot(t,a)
#plt.show()


# going to test spatialMean function and check time
xt = np.array(range(0,175))

from datetime import datetime
startTime = datetime.now()

# first subject
xt = tdTest.spatialMean(tensor_cube, 0)
print(datetime.now() - startTime)

yt = tdTest.spatialMean(tensor_cube, 1)
# this thing gives an indexing error
# IndexError: index 2 is out of bounds for axis 2 with size 2
wt = tdTest.spatialMean(tensor_cube, 2)
# same here, no data?
# wt = tdTest.spatialMean(tensor_cube, 3)
# print(yt)
plt.plot(t, xt, "r", t, wt,"b", t, yt, "g")
plt.show()