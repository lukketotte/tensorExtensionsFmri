import numpy as np

from nilearn import plotting as plot
from nilearn.image import smooth_img
from nilearn import image
from nilearn import datasets

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
# print(img2.get_data().shape)
x = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
y = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
x = tl.tensor(img1.get_data())
y = img2.get_data()
# print(isinstance(tl.to_numpy(x),np.ndarray))
# expecting NDarray type, and that it was it is getting???
# the error message is off I guess, wants a tl.tensor
tl.unfold(x,1)
# lets try and create the 3d tensor of 2 subjects
# tl.unfold(x, 3)
# y = tl.unfold(y, 3)
# store in
#X = tl.tensor(np.zeros(176*61*73*61).reshape(176, 61*73*61, 2))
#X[:,:,0] = x
#X[:,:,1] = y


#print(type(x))

# ------------- INSTANCE OF tensorData ------------- #
# tdTest = td([x, y], [0,1,2], 3)
# a = tdTest.niftyList
# print(type(a[1]))
# print(a[0][1,1,1,:])
# print(tdTest.idx_spatial)
# tensor_cube = tdTest.unfoldTemporal()
# print(tensor_cube.shape)

