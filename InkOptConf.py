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


CONFLOGLEVEL = logging.DEBUG


log = logging.getLogger(__name__)
log.setLevel(CONFLOGLEVEL)
loghandle = logging.StreamHandler()
loghandle.setLevel(CONFLOGLEVEL)
loghandle.setFormatter(logging.Formatter("%(asctime)s|%(name)s|%(levelname)s: %(message)s"))
log.addHandler(loghandle)


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
	
try:
	import numpy as np
except:
	try:
		Install("numpy")
		import numpy as np
	except:
		raise
	
try:
	import pandas
except:
	try:
		Install("pandas")
		import pandas
	except:
		raise


# Definitions
ENABLED = 1
DISABLED = 0
DEC = "number"
STR = "string"


# Get constants from config file, render as a dict, and then re-write the dict so it isn't broken AF
config = pandas.read_csv("InkOptConf.csv")
config.columns = ["CONSTANT", "Value"]
config = config.to_dict("records")
confdict = {}
for dict in config:
	confdict[dict["CONSTANT"]] = dict["Value"]

log.debug(confdict)

# ## Refactor to allow use of all default values
def getConst(confdict, const, type = STR, default = None):
	"""
	Pull the value of a config file constant by name.  If the constant isn't named in the config file, use the default.
	"""
	
	log.debug("Setting {} from config file.".format(const))
	
	try:
		val = confdict[const]
		log.debug("Set to {}".format(val))
	except Exception as e:
		log.debug(e)
		log.debug("Using default for {}".format(const))
		val = default
		
	if type == DEC:
		val = np.float64(val)
		
	if type == STR:
		val = "{}".format(val)
	
	return val
	
INTERCONSOLE = getConst(confdict, "INTERCONSOLE", DEC, DISABLED)
PROGNAME = getConst(confdict, "PROGNAME", STR, "VoxtelNano Ink Optimizer")
VERSION = getConst(confdict, "VERSION", DEC, "10.24")
COPYRIGHT = getConst(confdict, "COPYRIGHT", STR, "©2019 Voxtel, Inc.")
LEADDEV = "Adrian Henle" # This one doesn't get to be overwritten.
LOGO = getConst(confdict, "LOGO", STR, "logo.png")
INPUTFILE = getConst(confdict, "INPUTFILE", STR, "material_table.csv")
SMALLWINDOWX = getConst(confdict, "SMALLWINDOWX", DEC, "300")
SMALLWINDOWY = getConst(confdict, "SMALLWINDOWY", DEC, "400")
LARGEWINDOWX = getConst(confdict, "LARGEWINDOWX", DEC, "600")
LARGEWINDOWY = getConst(confdict, "LARGEWINDOWY", DEC, "800")
RUNBUTTONTEXT = getConst(confdict, "RUNBUTTONTEXT", STR, "LAUNCH OPTIMIZER")
RUNBUTTONCOLOR = getConst(confdict, "RUNBUTTONCOLOR", STR, "green")
EXITBUTTONTEXT = getConst(confdict, "EXITBUTTONTEXT", STR, "Exit")
EXITBUTTONCOLOR = getConst(confdict, "EXITBUTTONCOLOR", STR, "red")
ABOUTBUTTONTEXT = getConst(confdict, "ABOUTBUTTONTEXT", STR, "About")
PARAMWINDOWTITLE = getConst(confdict, "PARAMWINDOWTITLE", STR, "Parameter Window")
FRAMERELIEF = getConst(confdict, "FRAMERELIEF", STR, tk.GROOVE)
MINMATPCT = getConst(confdict, "MINMATPCT", DEC, "20")
DOPSTEP = getConst(confdict, "DOPSTEP", DEC, "5")
LOGFORMAT = getConst(confdict, "LOGFORMAT", STR, "%(asctime)s|%(name)s|%(levelname)s: %(message)s")


# ## Get constants from config file
#INTERCONSOLE = DISABLED

# General Constants
#PROGNAME = "VoxtelNano Ink Optimizer"
#VERSION = 10.24 # Version number
#COPYRIGHT = "©2019 Voxtel, Inc."
#LEADDEV = "Adrian Henle"
ABOUT = "{} v{}\n\n{}\n\n{}\n".format(PROGNAME, VERSION, LEADDEV, COPYRIGHT)
# ## This renders well in Unix, poorly in Windows.  Replace with JPEG in a tk.Canvas?
SPLASH = pyfiglet.figlet_format("{} v{}".format(PROGNAME, VERSION))
#LOGO = "logo.png"
#INPUTFILE = "material_table.csv" # Default input file for material propertie

# GUI Settings
"""SMALLWINDOWX = 300
SMALLWINDOWY = 400
LARGEWINDOWX = 600
LARGEWINDOWY = 800
RUNBUTTONTEXT = "LAUNCH OPTIMIZER"
RUNBUTTONCOLOR = "green"
EXITBUTTONTEXT = "Exit"
EXITBUTTONCOLOR = "red"
ABOUTBUTTONTEXT = "About"
PARAMWINDOWTITLE = "Parameter Window"
FRAMERELIEF = tk.GROOVE"""

# Algorithm Settings
#MINMATPCT = 20 # Minimum volume percentage of the matrix in a composite
#DOPSTEP = 5 # Number of points to sample in dopant percentage ranges
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
#LOGFORMAT = "%(asctime)s|%(name)s|%(levelname)s: %(message)s"

# ## Some of this stuff should be buried in the production version, and some should be left in a conf.txt file.  Split eventually.

# ## Mark the start time of the program run.  This is definitely not the place to do this.
STARTTIME = time.time()
