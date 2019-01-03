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
import logging
import signal # ## Needed?  If not... maybe write some good signal handlers? The default behavior is crappy.
import time
import tkinter as tk
from InkOpt import *
from InkOptConf import *
from InkOptGUI import *


# Set logging level (ERROR for stable versions, DEBUG for working versions)
log = logging.getLogger(__name__)
log.setLevel(LOGLEVEL)
loghandle = logging.StreamHandler()
loghandle.setLevel(LOGLEVEL)
loghandle.setFormatter(logging.Formatter(LOGFORMAT))
log.addHandler(loghandle)
log.info("Begin main program block")

def _endMain():
	log.info("The program is exiting. Up-time: {} seconds\n".format(int(time.time() - STARTTIME)))
	quit()


# Main program block
if __name__ == "__main__":

	# ## Functionalize
	
	STARTTIME = time.time()

	# Spin up the Ink Optimizer
	log.info("Instantiating InkOpt object")
	inkopt = InkOpt()
	
	# Launch the GUI
	try:
		consoleFlag = False # If GUI mode launches, don't enter console mode
		root = tk.Tk() # Main window
		root.title("VoxtelNano Ink Optimizer v{}".format(VERSION))
		GUI = InkOptGUI(root, inkopt)
		root.mainloop() # Launch the window
	except tk._tkinter.TclError as e:
		if ENABLECONSOLE:
			log.error("{}\nGoing to console application mode.".format(e))
			consoleFlag = True
		else:
			raise e
	except Exception as e:
		raise e
	
	# Run in console mode if GUI mode has errors
	if not consoleFlag:
		log.info("Program exit")
		_endMain()
		
	# Don't run in console mode if disabled in InkOptConf.py
	if INTERCONSOLE == DISABLED:
		log.info("Interactive console mode disabled.")
		_endMain()
		
	# Console splash and program info
	print(SPLASH)
	print("\n{}\n{}\n{}".format(PROGNAME, LEADDEV, COPYRIGHT))
	
	# Get material data from standard file input
	try:
		log.info("Reading data from {}".format(INPUTFILE))
		inkopt.readData(INPUTFILE)
	except Exception as e:
		log.error("Error getting material data ({})".format(e))
	
	log.info("\nMaterial Data Table:\n", inkopt.getData(), "\n") # Display the imported material data
	
	# Check for command line argument (parameter input file)
	try: ## # Change to make this less hacky
		log.info("Checking for command line argument (parameter input file)")
		numArgs = len(sys.argv)
		log.info("Number of arguments: {}".format(numArgs))
	except:
		log.info("No arguments.")
		numArgs = 0
	
	# Get parameters from file if runtime arg specified; otherwise, get parameters interactively
	if(numArgs > 1):
		log.info("Getting parameter input from {}".format(sys.argv[1]))
		inkopt.setParams(fileInput = sys.argv[1]) # from file
	else:
		log.info("Getting parameters interactively")
		inkopt.setParams() # interactively
	
	log.info("Call InkOpt input validation method")
	inkopt.validateParams() # Validate parameters
	
	# Generate permutations (using the new implementation of the old algorithm)
	log.info("Calling InkOpt v7 permutation algorithm")
	inkopt.permuteV7()
	
	log.info("Parameters:") # Display the specified parameters
	for key in inkopt.getParams():
		log.info("\t{}:  {}".format(key, inkopt.getParams()[key])) # ## Formatting (tab width) issue
	
	# Save permutations to file
	inkopt.getOutput("output.txt") # ## I don't like this implementation.  Also output file should be programmatically generated.
	
	log.info("End of program.")
	_endMain()
	