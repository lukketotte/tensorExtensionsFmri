"""
Select rows based on some criterions from the ADHD data set.
Will return string of location for IDs
"""

import pandas as pd
import os


class adhd:
	"""
	Parameters
	----------
	csvLocation: String
		location of csv with supplementary information on subjects

	niftyLocation: String
		location of data with niftys organized such that each subject
		has a folder named after ID 

	site: int
		which Site to get IDs for

	subjects: int
		number of subjects to return the folder location for
	"""

	def __init__(self, csvLoc = None, niftyLocation = None,
		         site = None, noSubjects = None):
		self._csvLocation = csvLocation
		self._niftyLocation = niftyLocation
		self._site = site
		self._noSubjects = noSubjects

	# --- GETTERS & SETTERS --- #

	@property
	def csvLocation(self):
		return self._csvLocation
	@csvLocation.setter
	def csvLocation(self, strLoc):
		# input validation
		if isinstance(strLoc, String):
			self._csvLocation = strLoc
		else:
			raise TypeError("Must be String")

	@property
	def niftyLocation(self):
		return self._niftyLocation
	@niftyLocation.setter
	def csvLocation(self, strLoc):
		if isinstance(strLoc, String):
			self._niftyLocation = strLoc
		else:
			raise TypeError("Must be String")