"""
InkOptHelpers.py
Adrian Henle
Voxtel, Inc.

Helper functions for InkOpt
"""


import numpy as np
import logging
from InkOptConf import *


# Set up logging
log = logging.getLogger(__name__)
log.setLevel(LOGLEVEL)
loghandle = logging.StreamHandler()
loghandle.setLevel(LOGLEVEL)
loghandle.setFormatter(logging.Formatter(LOGFORMAT))
log.addHandler(loghandle)
log.info("Begin log")


def inputf(dict, key, prompt):
	"""
	Helper function to handle interactive parameter acquisition
	"""
	while(True):
		try:
			inpstr = input("{}: ".format(prompt))
			dict[key] = [np.float64(x) for x in [inpstr.split(" ")]][0] # This looks stupid...
			break
		except:
			print("Bad input to {}".format(key))
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
	
	for wavelength in [*Dn]: # This could be made more elegant with a lambda
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
		(data.iloc[dopant1]["n(587 nm)"] * d1pct / 100#data.iloc[dopant1.astype(int)]["n(587 nm)"] * d1pct / 100
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

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	