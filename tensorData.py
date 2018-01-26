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
import tensorly as tl        # has operations

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

	def __init__(self, niftyList = [],
		         idx_spatial = None, idx_temporal = None):
		# not sure what this thing does, optional parameter assignment
		# in initialization?
		self._niftyList = niftyList
		self._idx_spatial = idx_spatial
		self._idx_temporal = idx_temporal

	#------ getters & setters -------#

	# getter and setter for niftylist
	@property
	def niftyList(self):
		# whenever this is being called a RecursionError is thrown
		return self._niftyList
	@niftyList.setter
	def niftyList(self, smoothImg):
		# check that input is nifty image fransformed to numpday.ndarray
		if isinstance(smoothImg[0], numpy.ndarray):
			# check that is 4d
			shape_img = smoothImg[0].get_data().shape
			if len(shape_img) == 4:
				# instanciate a TF tensor of the same shape as the smooth img
				# tensor = tf.get_variable("tensor_fMRI", smoothImg.get_data().shape)
				# number of elements in the tensor
				dim = shape_img[0] * shape_img[1] * shape_img[2] * shape_img[3]
				X = tl.tensor(np.zeros(dim).reshape(shape_img[0], shape_img[1], shape_img[2], shape_img[3]))
				for i in range(0,(len(smoothImg) - 1)):
					# this doesn't get returned as a np object
					X = smoothImg[i].get_data()
					self.niftyList.append(X)
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
			# check that length is 3, fmri is 4d
			if len(values) == 3:
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
	# a spatial and a temporal dimension. Stacking together these unfolded
	# tensors results in a 3d tensor with the 3-d mode being subjects in the
	# study

	# following Kolda et. al 2009
	"""
		This function takes no parameters
		it will be called to take the excisting 
		information in the class and create
		the 3d tensor out of the list of tensors
	"""
	def unfoldTemporal(self):
		# return object will be a 3d tensor
		# of dim: R^(Temp x (prod_spat) x Sub)
		# should have some rough input validation
		# TODO: create function that checks that all niftys 
		#       in the niftyList are of equal dimensions
		if self.niftyList != None:
			shape_tensor = self.niftyList[0].shape
			# set up the dimensions of the return object
			spat_dim = shape_tensor[0] * shape_tensor[1] * shape_tensor[2]
			temp_dim = shape_tensor[3]
			# no of subjects
			subj_dim = len(self.niftyList)
			# create a (temp, spat, subj) tensor to hold the result
			X = tl.tensor(np.zeros(temp_dim * spat_dim * subj_dim).reshape(temp_dim, spat_dim, subj_dim))
			# loop through the list of niftys, fold to temp_dim x spat_dim matricies
			# and add to the tensor. Folding is done on the temporal mode, leading
			# to the temporal fibers being the rows, with each column containing 
			# the spatial information
			
			#temp_nifty = tl.tensor(np.zeros(temp_dim * spat_dim).reshape(temp_dim, spat_dim))
			
			# loop through the subjects
			for i in range(0,(subj_dim-1)):
				# temp_nifty = tl.unfold(self.niftyList[i], self.idx_temporal)
				# seems like you have to make it to a tl.tensor rather than ndarray
				X[:,:,i] = tl.unfold(tl.tensor(self.niftyList[i]), self.idx_temporal)
		else:
			raise TypeError("No niftys has been entered")

		return X



