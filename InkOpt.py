"""
InkOpt.py
Adrian Henle
Voxtel, Inc.

InkOpt class definition.
"""


import time
import pandas as pd
import numpy as np
import logging
from InkOptHelpers import *
from InkOptConf import *


class InkOpt():
	"""
	Reads and processes material info and ink formulation parameters to generate
	testable permutations.
	"""	
	
	def __init__(self):
		"""
		Allocates and initializes.
		"""
		# Set up logging
		self.log = startLog(__name__)
		self.log.info("Begin log")
		
		# Declare output list
		# ## List is efficient as implemented.  A DataFrame would be nicer in the end, but is SLOW to .append()... Transform later?
		self.output = []
		
		# Declare DataFrame for material data
		self.data = pd.DataFrame()
		
		# Serialize output file name
		self.outputfile = "output_{}.csv".format(time.time())
		
		self.log.info("InkOpt object initialized with output target {}".format(self.outputfile))
		# ## Gonna need to implement a way to avoid overwriting output
	
	
	def readData(self, input, headers = True):
		"""
		Creates input data frame from file
		"""
		# By default, read first line as column headers.  Otherwise, read without headers.
		if headers == True:
			self.data = pd.read_csv(input, header = 0)
		else:
			self.data = pd.read_csv(input, header = None)
		self.log.info("Read input from {}:\n{}".format(input, self.data))
		
		return self.data
		
		
	def writeOutput(self, output = None, outputfile = None, log = None):
		"""
		Writes the output file as CSV
		"""
		# ## Write a lambda for this.  I'm sure it can be done!
		output = output if not output == None else self.output
		outputfile = outputfile if not outputfile == None else self.outputfile
		log = log if not log == None else self.log
		try:
			output.to_csv(outputfile)
			log.info("Wrote output to {}".format(outputfile))
		except:
			log.error("Error writing to {}".format(outputfile))
			
			
	# ## Put a lot more try/except blocks everywhere.
	# ## This compiles but it doesn't execute.  Can it be fixed?  This is pure curiosity.
	"""try:
		def func(self):
			return 1/0
	except:
		def func(self):
			return 2"""
	# ## Remove "self." and "*.*.*.*.*.*" from all over.
		

	def setParams(self, fileInput = None):
		"""
		Get parameters.
		Specify a fileInput for non-interactive parameter acquisition.
		"""
		
		# Parameter dictionary. Order must be the same as prompts array.
		# ## Find a way to build this from a config file
		params = {
			"maxDiffPdfs"	:		None,
			"maxPDf"		:		None,
			"minVgrin"		:		None,
			"minDnAvg"		:		None,
			"matrix1"		:		None,
			"matrix2"		:		None,
			"dopant1"		:		None,
			"dopant2"		:		None,
			"dopant3"		:		None,
			"dopant4"		:		None,
			"d1min"			:		None,
			"d1max"			:		None,
			"d2min"			:		None,
			"d2max"			:		None,
			"d3min"			:		None,
			"d3max"			:		None,
			"d4min"			:		None,
			"d4max"			:		None
		}
		keys = [*params] # Unpack keys
		
		if(fileInput == None):
		# Interactive parameter acquisition
			self.log.debug("Starting interactive parameter acquisition.")
			prompts = [ # List of parameter prompts # ## Find a way to build this from a config file
				"Enter max difference between Pd,f_hi and Pd,f_lo",
				"Enter the max P(delta)d,f",
				"Enter the minimum Vgrin",
				"Enter the minimum average of (delta)n",
				"Enter a space-delimited list of rows for matrix 1",
				"Enter a space-delimited list of rows for matrix 2",
				"Enter a space-delimited list of rows for dopant 1",
				"Enter a space-delimited list of rows for dopant 2",
				"Enter a space-delimited list of rows for dopant 3",
				"Enter a space-delimited list of rows for dopant 4",
				"Enter the minimum percentage of dopant 1",
				"Enter the maximum percentage of dopant 1",
				"Enter the minimum percentage of dopant 2",
				"Enter the maximum percentage of dopant 2",
				"Enter the minimum percentage of dopant 3",
				"Enter the maximum percentage of dopant 3",
				"Enter the minimum percentage of dopant 4",
				"Enter the maximum percentage of dopant 4"
			]
			for index, key in enumerate(keys):
				self.log.info("Getting input for {}".format(key))
				inputf(params, key, prompts[index]) # Print prompt, store user input
		else:
		# Parameter inputs from file. Line order must match the params dictionary
			self.log.info("Starting file parameter acquisition.")
			inputs = open(fileInput).readlines() # Read file into list of lines
			self.log.debug("Read from {}:\n{}".format(fileInput, inputs))
			for index, key in enumerate(keys): # Iterate over keys
				try:
					self.log.debug("Storing {} in {}".format(inputs[index][:-1], key))
					params[key] = np.float64(inputs[index].split(" ")) # Cast input to float
				except Exception as e: # Handle bad data
					self.log.error("Error in file input for {}:{{{}}} ({})".format(key, inputs[index], e))
					Quit(self.log)

		self.params = params # Store parameters
		self.log.debug("Parameters stored:\n{}".format(self.params))
		return self.params
		
		
	def getParams(self): # Superfluous, but whatever.
		"""
		Return the params object of InkOpt's input parameters as a dict.
		"""
		return self.params
		
		
	def validateParams(self):
		"""
		Checks input parameters
		"""
		self.log.info("Starting parameter validation.")
	
		def fail():
			log.error("Input validation failed.")
			Quit(self.log)
	
		# All parameters must be >= 0
		self.log.info("Checking for negative value inputs.")
		params = self.params.values()
		self.log.info("Parameters: {}".format(params))
		nums = iflat(params)
		self.log.info("Flattened inputs:\n{}".format(nums))
		for num in nums:
			self.log.debug(num)
			try:
				if num < 0:
					self.log.error("Negative value input!")
					fail()
			except ValueError:
				try:
					for nuum in num:
						if nuum < 0:
							self.log.error("Negative value input!")
							fail()
				except: # Why did this take so much effort??
					raise
			except Exception as e:
				self.log.error(e)
				fail()
			
		# "min" values must be < "max" values
		self.log.info("Checking that min < max for d1-d4")
		for x in [1, 2, 3, 4]:
			if self.params["d{}min".format(x)] > self.params["d{}max".format(x)]:
				self.log.error("d{}min > d{}max".format(x, x))
				fail()
				
		## There must be other conditions to check...
		
		
	# ## This needs unit testing
	def permuteV7(self):
		"""
		Permute the following lists with each other:
			Polymer1
			Polymer2
			NPs for Polymer1 (single)
			NPs for Polymer1 (pairs)
			NPs for Polymer2 (single, pairs)
			
		This is a re-implementation of the InkOpt v7 algorithm.
		This could be improved by determining the most selective factors and ordering the constraint checks to avoid
		frequently unnecessary computational steps.  Alternately, order to avoid most expensive step until last.
		"""
		
		counter = 0			
		for matrix1 in self.params["matrix1"]:
			for matrix2 in self.params["matrix2"]:
				for dopant1 in self.params["dopant1"]:
					for dopant2 in self.params["dopant2"]:
						if dopant1 == dopant2:
							log.debug("Skipping redundant combinations")
							continue
						for dopant3 in self.params["dopant3"]:
							for dopant4 in self.params["dopant4"]:
								if dopant3 == dopant4:
									log.debug("Skipping redundant combinations")
									continue
								for d1pct in np.linspace(self.params["d1min"][0], self.params["d1max"][0], num = DOPSTEP):
									if 100 - d1pct < MINMATPCT:
										self.log.debug("Skipping bad permutations...")
										break
									for d2pct in np.linspace(self.params["d2min"][0], self.params["d2max"][0], num = DOPSTEP):
										if 100 - d1pct - d2pct < MINMATPCT:
											self.log.debug("Skipping bad permutations...")
											break
										for d3pct in np.linspace(self.params["d3min"][0], self.params["d3max"][0], num = DOPSTEP):
											if 100 - d3pct < MINMATPCT:
												self.log.debug("Skipping bad permutations...")
												break
											for d4pct in np.linspace(self.params["d4min"][0], self.params["d4max"][0], num = DOPSTEP):
												if 100 - d3pct - d4pct < MINMATPCT:
													self.log.debug("Skipping bad permutations...")
													break
											
												counter = counter + 1
												self.log.debug("Permutation {}".format(counter))
												if(counter % 1000 == 0):
													self.log.info("Working on permutation {}...".format(counter))
												
												# Calulate Dn for each wavelength and check average against minDnAvg
												Dn = calcDns(matrix1, matrix2, dopant1, d1pct, dopant2, d2pct,
													dopant3, d3pct, dopant4, d4pct, self.data)
												if((Dn["486"] + Dn["587"] + Dn["656"])/3 < self.params["minDnAvg"][0]):
													self.log.debug("Formulation Dn average too low")
													continue
												self.log.debug("Dn average OK")
												
												# Calculate Pdfs and check against maxDiffPdfs
												if(abs(
													calcPdf(matrix1, dopant1, d1pct, dopant2, d2pct, self.data)
													- calcPdf(matrix2, dopant3, d3pct, dopant4, d4pct, self.data)
													) > self.params["maxDiffPdfs"]):
													self.log.debug("Pdf difference too great")
													continue
												self.log.debug("Pdf difference OK")
												
												# Calculate PDf and check against maxPDf
												PDf = 1e10 if Dn["656"] == Dn["486"] else (Dn["587"] - Dn["486"]) / (Dn["656"] - Dn["486"])
												self.log.debug("PDf is {}".format(PDf))
												if PDf > self.params["maxPDf"]:
													self.log.debug("PDf too high")
													continue
												self.log.debug("PDf OK")
												
												# Calculate Vgrin and check against minVgrin
												Vgrin = 1e10 if Dn["486"] == Dn["656"] else Dn["587"] / (Dn["486"] - Dn["656"])
												if Vgrin < self.params["minVgrin"]:
													self.log.debug("Vgrin too low")
													continue
												self.log.debug("Vgrin OK")
												
												# Append successful permutation to output
												self.log.debug("Appending formulation")
												self.output.append([
													self.data.iloc[matrix1.astype(int)][0],
													self.data.iloc[matrix2.astype(int)][0],
													self.data.iloc[dopant1.astype(int)][0],
													self.data.iloc[dopant2.astype(int)][0],
													self.data.iloc[dopant3.astype(int)][0],
													self.data.iloc[dopant4.astype(int)][0],
													d1pct,
													d2pct,
													d3pct,
													d4pct
												])
		
		
	def getOutput(self, writeToFile = None):
		"""
		Return the output of the permutation and testing algorithms.  Write to a file if a file name is specified.
		"""
		if(writeToFile != None):
			df = pd.DataFrame(self.output)
			df.columns = ["matrix1", "matrix2", "dopant1", "dopant2", "dopant3", "dopant4", "d1pct", "d2pct", "d3pct", "d4pct"]
			try:
				df.to_csv(self.outputfile)
				print("Output written to {} ({} lines)".format(self.outputfile, len(df)))
			except Exception as e:
				print("Error writing to {} ({})".format(self.outputfile, e))
		
		return self.output
		
		
	def getData(self):
		"""
		Return the material data table
		"""
		return self.data
		