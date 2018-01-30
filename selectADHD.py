"""
Select rows based on some criterions from the ADHD data set.
Will return string of location for IDs
"""

import pandas as pd 	# for reading the csv with suppl data 
import os 				# for creating paths
import re 				# for removing [] in the numpy array


class adhd:
	"""
	Parameters
	----------
	csvLocation: String
		location of csv with supplementary information on subjects.
		Path has to be all the way to the file itself.

	niftyLocation: String
		location of data with niftys organized such that each subject
		has a folder named after ID 

	site: int
		which Site to get IDs for

	numbSubjects: int
		number of subjects to return the folder location for
	"""

	def __init__(self, csvLoc = None, niftyLocation = None,
		         site = None, numbSubjects = None):
		self._csvLocation = csvLocation
		self._niftyLocation = niftyLocation
		self._site = site
		self._numbSubjects = numbSubjects

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

	@property
	def site(self):
		return self._site
	@site.setter
	def site(self, siteInt)
		if isinstance(siteInt, int):
			self._site = siteInt
		else:
			raise TypeError("Must be int")

	@property
	def numbSubjects(self)
		return self._numbSubjects
	@numbSubjects.setter
	def numbSubjects(self, numbSubInt)
		if isinstance(numbSubInt, int):
			self._numbSubjects = numbSubInt
		else:
			raise TypeError("Must be int")

	# ---------------------------------- #

	"""
		Should return a list of Strings with the 
		locations of valid repositories in the data
		folder. These should be based on the site
		requested
	"""

	def listOfLocations(self):
		# check that the paths are correctly specified...
		if(fileExists(niftyLocation)):
			if(fileExists(csvLocation)):
				# begin by reading the csv
				supplementaryData = pd.read_csv(self._csvLocation)
				# subset to the site (where the data has been gathered)
				# only keep ID column for now
				vec = supplementaryData.loc[(supplementaryData["Site"] == self._site)]
				vec = vec.loc[:, ["ID"]]
				# make it to np.array
				vec = np.array(vec)
				# loop through the vector and check whether the user id 
				# exists in the data repository
				subjectList = []
				for i in range(len(vec)):
					# need to make the numpy value to int and just using str()
					# carries through the square brackets. If subject ID exists in
					# the data repository it is appended to the subjectList
					tempLoc = os.path.join(niftyLocation, 
						                   re.sub("[\[\]]", "", np.array_str(vec[i])))
					if(fileExists(tempLoc)):
						subjectList.append(tempLoc)
				return subjectList
				# ...if not, raise an error
			else:
				raise FileNotFoundError("Path for csv not found")
		else: 
			raise FileNotFoundError("Path for niftyLocation not found")

	"""
		Helper function to find whether a file excists
	"""
	def fileExists(path):
		try:
			st = os.stat(path)
		except os.error:
			return False
		return True

