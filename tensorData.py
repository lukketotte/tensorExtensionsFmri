"""
This class will deal with restructuring a list of
tensors asumed to be 4d. The data will finally be 
stored as a tensorflow variable with three dimensions.
Spatial, temporal and subjects. Hard coded for 
my master thesis.
"""

import numpy as np            # highly uncertain if necessary
from nilearn import image     # nifty 
import tensorflow as tf       # store as tensors
import nibabel                # input validation
import tensorly as tly        # has operations

class tensor:
	""" Restrucutre list of nilearn imgs to 3-way tensor

	Important note: assume that the dimensions over the 
	nifty files from the subjects are constant. For the
	refolding (unfolding?) to be valid.
	
	Parameters
	----------
	niftyList: list[smooth_img]
		list (or tuple?) of tensor variables

	idx_spatial: list[int]
		specifies the indecies in the tuple from calling
		get_data().shape on a nilearn image of the spatial
		dimensions

	idx_temporal: int
		specifies the indecies in the tuple from calling
		get_data().shape on a nilearn image of the temporal
		dimensions
	"""

	def __init__(self, niftyList = None,
		         idx_spatial = None, idx_temporal = None):
		# not sure what this thing does, optional parameter assignment
		# in initialization?
		self.niftyList = niftyList
		self.idx_spatial = idx_spatial
		self.idx_temporal = idx_temporal

	#------ getters & setters -------#

	# getter and setter for niftylist
	@property
	def niftyList(self):
		return self._niftylist
	@niftyList.setter
	def niftyList(self, smoothImg):
		# check that input is nifty image
		if isinstance(smoothImg, nibabel.nifti1.Nifti1Image):
			# check that is 4d
			shape_img = smoothImg.get_data().shape
			if len(shape_img) == 4:
				# instanciate a TF tensor of the same shape as the smooth img
				# tensor = tf.get_variable("tensor_fMRI", smoothImg.get_data().shape)
				# number of elements in the tensor
				dim = shape_img[0] * shape_img[1] * shape_img[2] * shape_img[3]
				X = tl.tensor(np.zeros(dim).reshape([shape_img]))
				self._niftylist.append(X)
			else:
				raise ValueError("Shape of nifty must be 4d")
		else:
			raise TypeError("Must be a nifty type object")

	# getter and setter for idx_spatial
	@property
	def idx_spatial(self):
		return self._idx_spatial
	@idx_spatial.setter
	def idx_spatial(self, values):
		# check that we have a list
		if isinstance(values, list):
			# check that length is 2
			if len(values) == 2:
				# should check next position
				if(isinstance(values[0], int)):
					self._idx_spatial = values
				else: 
					raise TypeError("list must contain integer")
			else:
				raise ValueError("list must be of length 2")
		else:
			raise TypeError("Must be of list type")

	@property
	def idx_temporal(self):
		return self._idx_temporal
	@idx_temporal.setter
	def idx_temporal(self, value):
		if isinstance(value, int) and value > 0:
			self._idx_temporal = value
		else:
			raise TypeError("Must be positive integer")

	#-----------------------------------#

	# Matrix operations to unfold in the tensor to reduce the dimensions
	# some applications folds in the 4d fMRI tensor to a 2d matrix with 
	# a spatial and a temporal dimension. The 3d is then subjects

	# following Kolda et. al 2009

	# folding the tensor to 2d should result in a 783728 x 176 matrix
	# tensorly works but takes numpy array (ndarray?) as argument

