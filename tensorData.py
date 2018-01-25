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

class tensor:
	""" Restrucutre list of nilearn imgs to 3-way tensor

	Important note: assume that the dimensions over the 
	nifty files from the subjects are constant. For the
	refolding (unfolding?) to be valid.
	
	Parameters
	----------
	niftyList: list[smooth_img]
		list (or tuple?) of a smooth_img for each subject

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

	# getter and setter for niftylist
	@property
	def niftyList(self):
		return self._niftylist
	@niftyList.setter
	def niftyList(self, smoothImg):
		# check that input is nifty image
		if isinstance(smoothImg, nibabel.nifti1.Nifti1Image):
			self._niftylist.append(smoothImg)
		else:
			raise TypeError("Must be a nifty type object")