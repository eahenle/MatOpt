#!/usr/bin/env python
"""
InkOpt_v10.py
Adrian Henle
Voxtel, Inc.

Launch point for InkOpt v10
"""


from InkOptConf import *
from InkOptHelpers import *
from InkOpt import *
from InkOptGUI import *
import sys
import logging
# ## import signal
import time
import tkinter as tk


def GUILaunch(log):
	"""
	Launch the GUI
	"""
	try:
		consoleFlag = False # If GUI mode launches, don't enter console mode
		root = tk.Tk() # Root of the Tk process
		root.title("{} v{}".format(PROGNAME, VERSION))
		GUI = InkOptGUI(root, inkopt)
		root.mainloop() # Launch the window
	except tk._tkinter.TclError as e:
		log.error("{}".format(e))
		if INTERCONSOLE == ENABLED:
			consoleFlag = True
		else:
			Quit(log, code = 1, msg = "{}. Is there an X11 display available?".format(e))
	except Exception as e:
		raise e
	return root, GUI, consoleFlag
	

def interConsole(inkopt, sysargs, log):
	"""
	Run the interactive console routine
	"""
	# Console splash and program info
	print("\n{}\n\n{}\n{}\n{}".format(SPLASH, PROGNAME, LEADDEV, COPYRIGHT))
	
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
		numArgs = len(sysargs)
		log.info("Number of arguments: {}".format(numArgs))
	except:
		log.info("No arguments.")
		numArgs = 0
	
	# Get parameters from file if runtime arg specified; otherwise, get parameters interactively
	if(numArgs > 1):
		log.info("Getting parameter input from {}".format(sysargs[1]))
		inkopt.setParams(fileInput = sysargs[1]) # from file
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
	

# Main program block
if __name__ == "__main__":

	# Mark program start time
	# STARTTIME = time.time() # ## This is done by InkOptConf.py... but it shouldn't be.

	# Start logging
	log = startLog(__name__)
	
	# ## Start exception handling

	# Spin up the Ink Optimizer
	log.info("Instantiating InkOpt object")
	inkopt = InkOpt()
	
	# Launch the GUI
	root, GUI, consoleFlag = GUILaunch(log)
			
	# If GUI launches OK, exit program on GUI close.
	if not consoleFlag:
		log.info("Program exit")
		Quit(log)
		
	# Don't run in console mode if disabled in InkOptConf.py
	if INTERCONSOLE == DISABLED:
		log.info("Interactive console mode disabled.")
		Quit(log)
		
	# Run in console mode if GUI mode has errors
	interConsole(inkopt, sys.argv, log)
		
	# End of program
	log.info("End of program.")
	Quit(log)
	