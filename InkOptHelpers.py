"""
InkOptHelpers.py
Adrian Henle
Voxtel, Inc.

Helper functions for InkOpt
"""


import logging
from InkOptConf import *


# Set up logging
log = logging.getLogger(__name__)
log.setLevel(LOGLEVEL)
loghandle = logging.StreamHandler()
loghandle.setLevel(LOGLEVEL)
loghandle.setFormatter(logging.Formatter('%(asctime)s %(name)s|%(levelname)s %(message)s'))
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
	log.debug("RET iflat({})".format(iterable))
	