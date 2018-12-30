import sys
import time
import pandas as pd
import numpy as np
import pyfiglet
import logging
import InkOptHelpers
from InkOptConf import *

LOGLEVEL = logging.INFO

log = logging.getLogger(__name__)
log.setLevel(LOGLEVEL)
loghandle = logging.StreamHandler()
loghandle.setLevel(LOGLEVEL)
loghandle.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
log.addHandler(loghandle)
log.info("Begin log")

class InkOpt():
	"""
	Reads and processes material info and ink formulation parameters to generate
	testable permutations.
	"""	
	
	def __init__(self):
		"""
		Allocates a data frame for formulation outputs, serializes output file
		"""
		self.output = []
		self.outputfile = "output_{}.csv".format(time.time())
		log.info("InkOpt object initialized with output target {}".format(self.outputfile))
	
	def getData(self, input):
		"""
		Creates input data frame from file
		"""
		self.data = pd.read_csv(input)
		log.info("Read input from {}:\n{}".format(input, self.data))
		
	def writeOutput(self):
		"""
		Writes the output file as CSV
		"""
		self.output.to_csv(self.outputfile)
		log.info("Wrote output to {}".format(self.outputfile))

	def setParams(self, fileInput = None):
		"""
		Get parameters.
		Specify a fileInput for non-interactive parameter acquisition.
		"""
		
		# Parameter dictionary. Order must be the same as prompts array.
		params = {
			"maxDiffPdfs"	:		None,
			"maxPDf"		:		None,
			"minVgrin"		:		None,
			"minDnAvg"		:		None,
			"matrix1"		:		None,
			"matrix2"		:		None,
			"dopant1"		:		None,
			"dopant2"		:		None,
			"dopant3"		:		None,
			"dopant4"		:		None,
			"d1min"			:		None,
			"d1max"			:		None,
			"d2min"			:		None,
			"d2max"			:		None,
			"d3min"			:		None,
			"d3max"			:		None,
			"d4min"			:		None,
			"d4max"			:		None
		}
		keys = [*params] # Unpack keys
		
		if(fileInput == None): # Interactive parameter acquisition
			log.debug("Starting interactive parameter acquisition.")
			prompts = [ # List of parameter prompts
				"Enter max difference between Pd,f_hi and Pd,f_lo",
				"Enter the max P(delta)d,f",
				"Enter the minimum Vgrin",
				"Enter the minimum average of (delta)n",
				"Enter a space-delimited list of rows for matrix 1",
				"Enter a space-delimited list of rows for matrix 2",
				"Enter a space-delimited list of rows for dopant 1",
				"Enter a space-delimited list of rows for dopant 2",
				"Enter a space-delimited list of rows for dopant 3",
				"Enter a space-delimited list of rows for dopant 4",
				"Enter the minimum percentage of dopant 1",
				"Enter the maximum percentage of dopant 1",
				"Enter the minimum percentage of dopant 2",
				"Enter the maximum percentage of dopant 2",
				"Enter the minimum percentage of dopant 3",
				"Enter the maximum percentage of dopant 3",
				"Enter the minimum percentage of dopant 4",
				"Enter the maximum percentage of dopant 4"
			]
			for index, key in enumerate(keys):
				log.info("Getting input for {}".format(key))
				InkOptHelpers.inputf(params, key, prompts[index]) # Print prompt, store input
		else: # Parameter inputs from file. Line order must match the params dictionary
			log.info("Starting file parameter acquisition.")
			inputs = open(fileInput).readlines() # Read file into list of lines
			log.debug("Read from {}:\n{}".format(fileInput, inputs))
			for index, key in enumerate(keys): # Iterate over keys
				try:
					log.debug("Storing {} in {}".format(inputs[index][:-1], key))
					params[key] = np.float64(inputs[index].split(" ")) # Cast input to float
				except Exception as e: # Handle bad data
					log.error("Error in file input for {}:{{{}}} ({})".format(key, inputs[index], e))
					quit()

		self.params = params # Store parameters
		log.debug("Parameters stored:\n{}".format(self.params))
		return self.params
		
	def getParams(self): # Superfluous, but whatever.
		"""
		Return the params object of InkOpt's input parameters as a dict.
		"""
		return self.params
		
	def validateParams(self):
		"""
		Checks input parameters
		"""
	
		log.info("Starting parameter validation.")
	
		def fail():
			log.error("Input validation failed.")
			quit()
	
		# All parameters must be >= 0
		log.info("Checking for negative value inputs.")
		params = self.params.values()
		log.info("Parameters: {}".format(params))
		nums = InkOptHelpers.iflat(params)
		log.info("Flattened inputs:\n{}".format(nums))
		for num in nums:
			log.debug(num)
			try:
				if num < 0:
					log.error("Negative value input!")
					fail()
			except ValueError:
				try:
					for nuum in num:
						if nuum < 0:
							log.error("Negative value input!")
							fail()
				except: # Why did this take so much effort??
					raise
			except Exception as e:
				log.error(e)
				fail()
			
		# "min" values must be < "max" values
		## IMPLEMENT
		
		# matrix materials must be at least MINMATPCT % of composite volume 
		## IMPLEMENT
		
	def permuteV7(self):
		"""
		Permute the following lists with each other:
			Polymer1
			Polymer2
			NPs for Polymer1 (single)
			NPs for Polymer1 (pairs)
			NPs for Polymer2 (single, pairs)
			
		This is a re-implementation of the InkOpt v7 algorithm.
		"""
		
		counter = 0
		
		def calcDns(matrix1, matrix2, dopant1, d1pct, dopant2, d2pct, dopant3, d3pct, dopant4, d4pct):
			Dn = {
				"486"	:	-1,
				"587"	:	-1,
				"656"	:	-1
			}
			
			# Find matrix percentages, reject permutation if too little matrix by volume
			mat1pct = 100 - d1pct - d2pct
			mat2pct = 100 - d3pct - d4pct
			if(mat1pct < MINMATPCT or mat2pct < MINMATPCT):
				return Dn
			
			for wavelength in [*Dn]:
				Dn[wavelength] = (
					self.data.iloc[dopant1.astype(int)]["n({} nm)".format(wavelength)] * d1pct/100
					+
					self.data.iloc[dopant2.astype(int)]["n({} nm)".format(wavelength)] * d2pct/100
					+
					self.data.iloc[matrix1.astype(int)]["n({} nm)".format(wavelength)] * mat1pct/100
					) - (
					self.data.iloc[dopant3.astype(int)]["n({} nm)".format(wavelength)] * d3pct/100
					+
					self.data.iloc[dopant4.astype(int)]["n({} nm)".format(wavelength)] * d4pct/100
					+
					self.data.iloc[matrix2.astype(int)]["n({} nm)".format(wavelength)] * mat2pct/100
				)
			return Dn
		
		for matrix1 in self.params["matrix1"]:
			for matrix2 in self.params["matrix2"]:
				for dopant1 in self.params["dopant1"]:
					for dopant2 in self.params["dopant2"]:
						for dopant3 in self.params["dopant3"]:
							for dopant4 in self.params["dopant4"]:
								for d1pct in np.linspace(self.params["d1min"][0], self.params["d1max"][0], num = DOPSTEP):
									for d2pct in np.linspace(self.params["d2min"][0], self.params["d2max"][0], num = DOPSTEP):
										for d3pct in np.linspace(self.params["d3min"][0], self.params["d3max"][0], num = DOPSTEP):
											for d4pct in np.linspace(self.params["d4min"][0], self.params["d4max"][0], num = DOPSTEP):
												counter = counter + 1
												if(counter % 1000 == 0):
													print("Working on permutation {}...".format(counter))
												# Calulate Dn for each wavelength and check average against constraints minDnAvg and MINMATPCT
												Dn = calcDns(matrix1, matrix2, dopant1, d1pct, dopant2, d2pct, dopant3, d3pct, dopant4, d4pct)
												if((Dn["486"] + Dn["587"] + Dn["656"])/3 < self.params["minDnAvg"][0]):
													continue
												self.output.append([
													self.data.iloc[matrix1.astype(int)][0],
													self.data.iloc[matrix2.astype(int)][0],
													self.data.iloc[dopant1.astype(int)][0],
													self.data.iloc[dopant2.astype(int)][0],
													self.data.iloc[dopant3.astype(int)][0],
													self.data.iloc[dopant4.astype(int)][0],
													d1pct,
													d2pct,
													d3pct,
													d4pct
												])
		
	def getOutput(self, writeToFile = None):
		if(writeToFile != None):
			df = pd.DataFrame(self.output)
			df.columns = ["matrix1", "matrix2", "dopant1", "dopant2", "dopant3", "dopant4", "d1pct", "d2pct", "d3pct", "d4pct"]
			try:
				df.to_csv(self.outputfile)
				print("Output written to {} ({} lines)".format(self.outputfile, len(df)))
			except Exception as e:
				print("Error writing to {} ({})".format(self.outputfile, e))
		
		return self.output