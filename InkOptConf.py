"""
InkOptConf.py
Adrian Henle
Voxtel, Inc.

Configurations and settings values for InkOpt and InkOptHelpers
"""


# ## This code is a mess.


import time
import logging
import sys

# ## This should probably be moved to an installer program.
import subprocess
def Install(module):
	"""
	
	"""
	
	try:
		subprocess.call([sys.executable, "-m", "pip", "install", module])
	except:
		raise

try:
	import pyfiglet
except Exception:
	try:
		Install("pyfiglet")
		import pyfiglet
	except:
		raise
except:
	raise

try:
	import tkinter as tk
except Exception:
	try:
		Install("tkinter")
		import tkinter
	except Exception:
		try:
			Install("Tkinter")
			import tkinter
		except:
			raise
	except:
		raise
except:
	raise


# Definitions
ENABLED = True
DISABLED = False

# Use Mode Settings
INTERCONSOLE = DISABLED

# General Constants
PROGNAME = "VoxtelNano Ink Optimizer"
VERSION = 10.22 # Version number
COPYRIGHT = "©2019 Voxtel, Inc."
LEADDEV = "Adrian Henle"
ABOUT = "{} v{}\n\n{}\n\n{}\n".format(PROGNAME, VERSION, LEADDEV, COPYRIGHT)
# ## This renders well in Unix, poorly in Windows.  Replace with JPEG in a tk.Canvas?
SPLASH = pyfiglet.figlet_format("InkOpt v{}".format(VERSION))
INPUTFILE = "material_table.csv" # Default input file for material propertie

# GUI Settings
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
FRAMERELIEF = tk.GROOVE

# Algorithm Settings
MINMATPCT = 20 # Minimum volume percentage of the matrix in a composite
DOPSTEP = 5 # Number of points to sample in dopant percentage ranges
"""
	### WARNING! ###
	Complexity for v7 algorithm is O(k^DOPSTEP).
	5 is pretty good for testing purposes.  Don't increase sampling density unless you have all day to run permutations.
"""

# Set loggers for debugging in development versions, error reporting in stable versions
if((VERSION * 10) % 1 == 0):
	LOGLEVEL = logging.ERROR
else:
	LOGLEVEL = logging.DEBUG
	
# Output formatting string for logging handlers
LOGFORMAT = "%(asctime)s|%(name)s|%(levelname)s: %(message)s"

# ## Some of this stuff should be buried in the production version, and some should be left in a conf.txt file.  Split eventually.

# ## Mark the start time of the program run.  This is definitely not the place to do this.
STARTTIME = time.time()
