#!/usr/bin/env python
"""
InkOpt version 10

Written by Adrian Henle, based on InkOpt_lite_inter_v7.py

CONFIDENTIAL PROPERTY OF VOXTEL, INC.

Input specifications:
	Matrix1:		a list of matrix materials from the data table
	Matrix2:		a list of matrix materials from the data table
	Dopant1:		a list of potential dopants for Matrix1
	Dopant2:		a list of potential co-dopants for Matrix1
	Dopant3:		a list of potential dopants for Matrix2
	Dopant4:		a list of potential co-dopants for Matrix2
	MaxDeltaPdf:	the maximum allowable difference in Pd,f
	MaxPDeltadf:	the maximum allowable P(delta)d,f
	MinAvgDeltan:	the minimum average of (delta)n
	MinPercent1:	the minimum volume % loading of Dopant1
	MaxPercent1:	the maximum volume % loading of Dopant1
	MinPercent2:	the minimum volume % loading of Dopant2
	MaxPercent2:	the maximum volume % loading of Dopant2
	MinPercent3:	the minimum volume % loading of Dopant3
	MaxPercent3:	the maximum volume % loading of Dopant3
	MinPercent4:	the minimum volume % loading of Dopant4
	MaxPercent4:	the maximum volume % loading of Dopant4
	
Inputs may be specified interactively, or by specifying a parameter input file at runtime.
Input files must specify parameters in the order shown above. List-type data are entered
as space-delimited lists on a single line.  Non-numeric inputs are rejected.
	
Dopant percentages are permuted with a density of DOPSTEP samples in each range.  I.e., each step
iterates the tested percentage by (Max - Min)/DOPSTEP
"""


import sys
import time
import pandas as pd
import numpy as np
import pyfiglet
import logging


VERSION = 10.02 # Version number ## Consider scraping from filename?
INPUTFILE = "material_table.csv" # Default input file for material properties
MINMATPCT = 20 # Minimum volume percentage of the matrix in a composite
DOPSTEP = 4 # Number of points to sample in dopant percentage ranges
"""
	### WARNING! ###
	Complexity for v7 algorithm is O(k^DOPSTEP).
	Don't increase sampling density unless you have all day to run permutations.
"""

# Set logging level (ERROR for stable versions, INFO for working versions)
LOGLEVEL = logging.NOTSET
if(VERSION % 1 == 0):
	LOGLEVEL = logging.ERROR
else:
	LOGLEVEL = logging.INFO
LOG = logging.getLogger(__name__)
LOG.setLevel(LOGLEVEL)
LOG.info("Begin log")


def inputf(dict, key, prompt):
	"""
	Helper function to handle interactive parameter acquisition
	"""
	while(True):
		try:
			inpstr = input("{}: ".format(prompt))
			dict[key] = [np.float64(x) for x in [inpstr.split(" ")]]
			break
		except:
			print("Bad input to {}".format(key))

			
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
	
	def getData(self, input):
		"""
		Creates input data frame from file
		"""
		self.data = pd.read_csv(input)
		
	def writeOutput(self):
		"""
		Writes the output file as CSV
		"""
		self.output.to_csv(self.outputfile)

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
				inputf(params, key, prompts[index]) # Print prompt, store input
		else: # Parameter inputs from file. Line order must match the params dictionary
			inputs = open(fileInput).readlines() # Read file into list of lines
			for index, key in enumerate(keys): # Iterate over keys
				try:
					params[key] = np.float64(inputs[index].split(" ")) # Cast input to float
				except Exception as e: # Handle bad data
					print("Error in file input for {}:{{{}}} ({})".format(key, inputs[index], e))
					quit()
			
		self.params = params # Store parameters
		return self.params
		
	def getParams(self):
		return self.params
		
	def validateParams(self):
	
		def fail():
			print("Input validation failed.")
			quit()
	
		# All parameters must be >= 0
		try:
			bools = [self.params[x][0] >= 0 for i, x in enumerate(self.params)]
		except:
			pass
		try:
			bools = [item for sublist in bools for item in sublist]
		except:
			pass
		if(sum([1 if x==False else 0 for x in bools]) != 0):
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

if __name__ == "__main__":

	# Display ASCII art
	print(pyfiglet.figlet_format("InkOpt v{}".format(VERSION)))
	print("©2018 Voxtel, Inc.")
	#print(pyfiglet.figlet_format("© VoxtelNano"))

	# Instantiate InkOpt object and read material data
	inkopt = InkOpt()
	try:
		inkopt.getData(INPUTFILE)
	except Exception as e:
		print("Error getting material data ({})".format(e))
	
	print("")
	
	print("Material Data Table:\n", inkopt.data, "\n") # Display the imported material data
	
	# Check for command line argument (parameter input file)
	try:
		numArgs = len(sys.argv)
	except:
		numArgs = 0
	
	if(numArgs > 1):
		inkopt.setParams(fileInput = sys.argv[1]) # Get parameters from file
	else:
		inkopt.setParams() # Get parameters interactively
	
	inkopt.validateParams() # Validate parameters
	
	# Generate permutations (using the new implementation of the old algorithm)
	inkopt.permuteV7()
	
	print("Parameters:") # Display the specified parameters
	for key in inkopt.getParams():
		print("\t{}:  {}".format(key, inkopt.getParams()[key])) # Formatting (tab width) issue
	
	print("")
	
	#print("Permutations:\n", inkopt.getOutput("output.txt")) # Print the permutation outputs
	inkopt.getOutput("output.txt")
	
	print("")
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	