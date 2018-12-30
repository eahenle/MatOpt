"""
InkOptConf.py
Adrian Henle
Voxtel, Inc.

Configurations and settings values for InkOpt and InkOptHelpers
"""

import logging

# Constants
VERSION = 10.06 # Version number
INPUTFILE = "material_table.csv" # Default input file for material properties
MINMATPCT = 20 # Minimum volume percentage of the matrix in a composite
DOPSTEP = 4 # Number of points to sample in dopant percentage ranges
"""
	### WARNING! ###
	Complexity for v7 algorithm is O(k^DOPSTEP).
	Don't increase sampling density unless you have all day to run permutations.
"""

# Set loggers for debugging in development versions, error reporting in stable versions
if(VERSION % 1 == 0):
	LOGLEVEL = logging.ERROR
else:
	LOGLEVEL = logging.DEBUG
	
LOGFORMAT = "%(asctime)s %(name)s|%(levelname)s %(message)s"
