"""
This class will deal with restructuring a list of
tensors asummed to be 4d. The data will finally be 
stored as a tensorflow variable with three dimensions.
Spatial, temporal and subjects. Hard coded for 
my master thesis.
"""

import numpy as np
from nilearn import image
import tensorflow as tf

class tensor:
	""" Restrucutre list of nilearn imgs to 3-way tensor

	Important note: assume that the dimensions over the 
	nifty files from the subjects are constant. For the
	refolding (unfolding?) to be valid.
	
	Parameters
	----------
	idx_spatial: list[int]
		specifies the indecies in the tuple from calling
		get_data().shape on a nilearn image of the spatial
		dimensions

	idx_temporal: int
		specifies the indecies in the tuple from calling
		get_data().shape on a nilearn image of the temporal
		dimensions


	"""