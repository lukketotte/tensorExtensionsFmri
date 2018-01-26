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
x = img1.get_data()

# ------------- INSTANCE OF tensorData ------------- #
tdTest = td([img1, img2], [0,1,2], 3)
x = tdTest.niftyList
print(type(x[1]))