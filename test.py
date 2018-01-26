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

x = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
y = tl.tensor(np.zeros(61*73*61*176).reshape(61,73,61,176))
x = img1.get_data()
y = img2.get_data()

# ------------- INSTANCE OF tensorData ------------- #
tdTest = td([x, y], [0,1,2], 3)
a = tdTest.niftyList
# print(type(a[1]))
# print(a[0][1,1,1,:])
# print(tdTest.idx_spatial)
tensor_cube = tdTest.unfoldTemporal()
print(tensor_cube.shape)

