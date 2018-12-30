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
import importlib
import InkOpt
import InkOptHelpers
from InkOptConf import *

# Set logging level (ERROR for stable versions, DEBUG for working versions)
if(VERSION % 1 == 0):
	LOGLEVEL = logging.ERROR
else:
	LOGLEVEL = logging.DEBUG
log = logging.getLogger(__name__)
log.setLevel(LOGLEVEL)
loghandle = logging.StreamHandler()
loghandle.setLevel(LOGLEVEL)
loghandle.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
log.addHandler(loghandle)
log.info("Begin log")



	
	


if __name__ == "__main__":

	# Display ASCII art
	print(pyfiglet.figlet_format("InkOpt v{}".format(VERSION)))
	print("©2018 Voxtel, Inc.")
	#print(pyfiglet.figlet_format("© VoxtelNano"))

	# Instantiate InkOpt object and read material data
	inkopt = InkOpt.InkOpt()
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
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	