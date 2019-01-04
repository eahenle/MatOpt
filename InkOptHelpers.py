"""
InkOptHelpers.py
Adrian Henle
Voxtel, Inc.

Helper functions for InkOpt
"""

# ## Check dependencies for redundancies
# ## see about the right way to use packages...
from InkOptConf import *

import logging
import time
import sys

try:
	import numpy as np
except:
	try:
		Install("numpy")
		import numpy
	except:
		raise
		
		
def TkFrame(master):
	"""
	Generates a tk.Frame under the given master frame and pack it
	"""
	
	frame = tk.Frame(master, relief = FRAMERELIEF)
	frame.pack()
	
	return frame
	
	
def WidthProp(master, width = SMALLWINDOWX, side = tk.TOP):
	"""
	Generates a tk.Frame for propping a window open to a minimum width
	"""
	
	prop = tk.Frame(master, width = width, relief = FRAMERELIEF)
	prop.pack(side = side)
	
	return prop


# ## Improve by handling INFO and ERROR logging in a StreamHandler, and DEBUG logging in a FileHandler
def startLog(name, level = LOGLEVEL, format = LOGFORMAT):
	"""
	Helper function to spin up a logger stream.
	Invoke with log = startLog(__name__)
	"""
	log = logging.getLogger(name)
	log.setLevel(level)
	loghandle = logging.StreamHandler()
	loghandle.setLevel(level)
	loghandle.setFormatter(logging.Formatter(format))
	log.addHandler(loghandle)
	return log


# ## Try to use this with SIGINT and SIGKILL
def Quit(log, code = 0, msg = None):
	"""
	Helper function that swiftly exits the program.
	"""
	# ## Hack this line to intelligently handle a msg = None situation
	log.info("The program is exiting with message {}; Up-time: {} second(s)\n".format(msg, int(time.time() - STARTTIME)))
	sys.exit(code)
			

def inputf(dict, key, prompt):
	"""
	Helper function to handle interactive parameter acquisition
	"""
	inpstr = ""
	while(inpstr == ""):
		try:
			inpstr = input("{}: ".format(prompt))
			dict[key] = [np.float64(x) for x in [inpstr.split(" ")]][0] # This looks stupid...
			break
		except KeyboardInterrupt:
			log.error("Ctrl+C quit")
			Quit(log)
		except:
			print("Bad input to {}".format(key))
			inpstr = ""
	log.debug("Stored {} to {}".format(inpstr, key))

	
def iflat(iterable):
	"""
	Helper function to flatten an interable object.
	"""
	log.debug("iflat({})".format(iterable))
	for element in iter(iterable):
		log.debug("element: {}".format(element))
		if isinstance(element, (list, tuple)):
			log.debug("element is list or tuple")
			for subelement in iflat(element):
				log.debug("yielding {} to subelement generator".format(subelement))
				yield subelement
		else:
			log.debug("yielding {} to element generator".format(element))
			yield element
			
			
def calcDns(matrix1, matrix2, dopant1, d1pct, dopant2, d2pct, dopant3, d3pct, dopant4, d4pct, data):
	"""
	Calculate difference of refractive index at different wavelengths.
	At least I think that's what it does.  The math is based on the v7 code.
	Returns dictionary of wavelength-Dn pairs.
	"""

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
	
	for wavelength in [*Dn]: # ## This could be made more elegant with a lambda
		Dn[wavelength] = np.float64(
			data.iloc[dopant1.astype(int)]["n({} nm)".format(wavelength)] * d1pct / 100
			+ data.iloc[dopant2.astype(int)]["n({} nm)".format(wavelength)] * d2pct / 100
			+ data.iloc[matrix1.astype(int)]["n({} nm)".format(wavelength)] * mat1pct / 100
			- data.iloc[dopant3.astype(int)]["n({} nm)".format(wavelength)] * d3pct / 100
			- data.iloc[dopant4.astype(int)]["n({} nm)".format(wavelength)] * d4pct / 100
			- data.iloc[matrix2.astype(int)]["n({} nm)".format(wavelength)] * mat2pct / 100
		)
	log.debug("Calculated Dns")
	return Dn			
	
	
def calcPdf(matrix, dopant1, d1pct, dopant2, d2pct, data):
	"""
	Calculate the Pdf for a doubly doped optical material, using a material data table
	At least I think that's what it does.  The math is based on the v7 code.
	Returns an np.float64
	"""
	matrix, dopant1, dopant2 = int(matrix), int(dopant1), int(dopant2)
	log.debug("Calculating Pdf for {} with {} ({}%) and {} ({}%)".format(
		data.iloc[matrix]["Material"], data.iloc[dopant1]["Material"], d1pct, data.iloc[dopant2]["Material"], d2pct))
	return np.float64(
		(data.iloc[dopant1]["n(587 nm)"] * d1pct / 100
		+ data.iloc[dopant2]["n(587 nm)"] * d2pct / 100
		+ data.iloc[matrix]["n(587 nm)"] * (1 - (d1pct + d2pct) / 100)
		- data.iloc[dopant1]["n(486 nm)"] * d1pct / 100
		- data.iloc[dopant2]["n(486 nm)"] * d2pct / 100
		- data.iloc[matrix]["n(486 nm)"] * (1 - (d1pct + d2pct) / 100)
		) / (
		data.iloc[dopant1]["n(656 nm)"] * d1pct / 100
		+ data.iloc[dopant2]["n(656 nm)"] * d2pct / 100
		+ data.iloc[dopant1]["n(656 nm)"] * (1 - (d1pct + d2pct) / 100)
		- data.iloc[dopant1]["n(486 nm)"] * d1pct / 100
		- data.iloc[dopant2]["n(486 nm)"] * d2pct / 100
		- data.iloc[matrix]["n(486 nm)"] * (1 - (d1pct + d2pct) / 100)
		)
	)

