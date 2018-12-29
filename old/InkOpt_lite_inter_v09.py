#!/usr/bin/env python
"""
InkOpt_lite_inter_v09.py

CONFIDENTIAL PROPERTY OF VOXTEL, INC.

A program to generate ink formulations.

Each formulation is based on inputs of two lists of matrices and two lists-of-lists
of dopants.  Potential formulations are probed for calculated parameters relevant to
GRIN optics, and material combinations with acceptable values are returned to the
user in CSV format for viewing in spreadsheet software.

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
	
Percentages are permuted with a density of 1000 samples in each range.  I.e., each step
iterates the tested percentage by (Max - Min)/1000

Future versions may include:
	GUI
	Command line data file specification
	Generation of massive SQL databases (minimal end-user compute time for finding
		good formulations with complex requirements)
"""

import sys # For command line argument parsing
import time # For output file serialization
import pandas as pd # For data handling
import numpy as np # For type casting


INPUTFILE = "material_table.csv" # Default input file for material properties
BANNERFILE = "banner.txt" # ASCII art splash for program start


def inputf(dict, key, prompt):
	"""
	Helper function to handle interactive parameter acquisition
	"""
	while(True):
		try:
			dict[key] = np.float64(input("{}: ".format(prompt)))
			break
		except ValueError:
			print("Bad input.")

			
class InkOpt():
	"""
	Reads and processes material info and ink formulation parameters to generate
	testable permutations.
	"""	
	
	def __init__(self):
		"""
		Allocates a data frame for formulation outputs, serializes output file
		"""
		self.output = pd.DataFrame()
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
		
		# Parameter dictionary
		params = {
			"maxDiffPdfs"	:		None,
			"maxPDf"		:		None,
			"minVgrin"		:		None,
			"minDnAvg"		:		None,
			"iMin"			:		None,
			"iMax"			:		None,
			"jMin"			:		None,
			"jMax"			:		None,
			"kMin"			:		None,
			"kMax"			:		None,
			"lMin"			:		None,
			"lMax"			:		None,
			"mMin"			:		None,
			"mMax"			:		None,
			"nMin"			:		None,
			"nMax"			:		None,
			"oMin"			:		None,
			"oMax"			:		None,
			"pMin"			:		None,
			"pMax"			:		None,
			"qMin"			:		None,
			"qMax"			:		None,
			"rMin"			:		None,
			"rMax"			:		None
		}
		keys = [*params] # Unpack keys
		
		if(fileInput == None): # Interactive parameter acquisition
			prompts = [ # List of parameter prompts
				"Enter max difference between Pd,f_hi and Pd,f_lo",
				"Enter the max P(delta)d,f",
				"Enter the minimum Vgrin",
				"Enter the minimum avg of (delta)n",
				"Enter the first row for the np2 data",
				"Enter the last row for the np2 data",
				"Enter the first row for the np1 data",
				"Enter the last row for the np1 data",
				"Enter the first row for the n4 data",
				"Enter the last row for the n4 data",
				"Enter the first row for the n3 data",
				"Enter the last row for the n3 data",
				"Enter the first row for the n2 data",
				"Enter the last row for the n2 data",
				"Enter the first row for the n1 data",
				"Enter the last row for the n1 data",
				"Enter the minimum value of percent 4",
				"Enter the maximum value of percent 4",
				"Enter the minimum value of percent 3",
				"Enter the maximum value of percent 3",
				"Enter the minimum value of percent 2",
				"Enter the maximum value of percent 2",
				"Enter the minimum value of percent 1",
				"Enter the maximum value of percent 1"
			]
			for index, key in enumerate(keys):
				inputf(params, key, prompts[index]) # Print prompt, store input
		else: # Parameter inputs from file
			inputs = open(fileInput).readlines() # Read file into list of lines
			for index, key in enumerate(keys): # Iterate over keys
				try:
					params[key] = np.float64(inputs[index]) # Cast input to float
				except Exception as e: # Handle bad data
					print("Error in file input for {} ({})".format(key, e))
					quit()
			
		self.params = params # Store parameters
		return params
		
	def getParams(self):
		return self.params
		
	def permute(self):
		"""
		Permute the following lists with each other:
			Polymer1
			Polymer2
			NPs for Polymer1 (single)
			NPs for Polymer1 (pairs)
			NPs for Polymer2 (single, pairs)
		"""
		
		# Construct a list of Dopant1/Dopant2 loading permutations
		dopants12 = []
		
		# Construct a list of Dopant3/Dopant4 loading permutations
		# Construct a list of Matrix1/Dopant1-2 composite permutations
		# Construct a list of Matrix2/Dopant3-4 composite permutations
		# Construct a list of composite pairs

if __name__ == "__main__":

	# Display ASCII banner from file
	print("\n", *[line for line in open(BANNERFILE).readlines()])

	inkopt = InkOpt()
	inkopt.getData(INPUTFILE)	# Get the material data table
	
	try:
		numArgs = len(sys.argv)
	except:
		numArgs = 1
	
	if(numArgs > 1):
		inkopt.setParams(fileInput = "input.txt") # Get parameters from file
	else:
		inkopt.setParams() # Get parameters interactively
	
	inkopt.permute() # Generate permutations
	
	# See what we did
	print("\nMaterial Data Table:\n", inkopt.data, "\n") # Display the imported material data
	print("Parameters:") # Display the specified parameters
	for key in inkopt.getParams():
		print("\t{}\t\t{}".format(key, inkopt.getParams()[key])) # Formatting (tab width) issue
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	