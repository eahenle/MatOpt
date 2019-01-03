"""
InkOptConf.py
Adrian Henle
Voxtel, Inc.

Configurations and settings values for InkOpt and InkOptHelpers
"""


import logging
import pyfiglet


# Constants
VERSION = 10.13 # Version number
COPYRIGHT = "©2019 Voxtel, Inc."
ABOUT = "VoxtelNano Ink Optimizer v{}\n\nAdrian Henle\n\n{}\n".format(VERSION, COPYRIGHT)
ENABLECONSOLE = False # Disabled for GUI development
SPLASH = pyfiglet.figlet_format("InkOpt v{}".format(VERSION))
INPUTFILE = "material_table.csv" # Default input file for material properties
MINMATPCT = 20 # Minimum volume percentage of the matrix in a composite
SMALLWINDOWX = 300
SMALLWINDOWY = 400
LARGEWINDOWX = 600
LARGEWINDOWY = 800
RUNBUTTONTEXT = "LAUNCH OPTIMIZER"
RUNBUTTONCOLOR = "green"
EXITBUTTONTEXT = "Exit"
EXITBUTTONCOLOR = "red"
ABOUTBUTTONTEXT = "About"
PARAMWINDOWTITLE = "Parameter Window"
DOPSTEP = 6 # Number of points to sample in dopant percentage ranges
"""
	### WARNING! ###
	Complexity for v7 algorithm is O(k^DOPSTEP).
	Don't increase sampling density unless you have all day to run permutations.
"""

# Set loggers for debugging in development versions, error reporting in stable versions
if((VERSION * 10) % 1 == 0):
	LOGLEVEL = logging.ERROR
else:
	LOGLEVEL = logging.DEBUG
	
# Output formatting string for logging handlers
LOGFORMAT = "%(asctime)s %(name)s|%(levelname)s %(message)s"
