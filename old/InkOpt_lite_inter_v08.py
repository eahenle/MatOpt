#!/usr/bin/env python
"""
InkOpt_lite_inter_v8.py

CONFIDENTIAL PROPERTY OF VOXTEL, INC.

A program to generate ink formulations.

Each formulation is based on inputs of two lists of matrices and two lists-of-lists
of dopants.  Potential formulations are probed for calculated parameters relevant to
GRIN optics, and material combinations with acceptable values are returned to the
user in CSV format for viewing in spreadsheet software.

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

Future versions may include:
	GUI
	Command line data file specification
	Generation of massive SQL databases (minimal end-user compute time for finding
		good formulations with complex requirements)
"""

import time
import pandas as pd
import numpy as np

INPUTFILE = "material_table.csv"
BANNERFILE = "banner.txt"

def inputf(dict, key, prompt):
	while(True):
		try:
			dict[key] = np.float64(input("{}: ".format(prompt)))
			break
		except ValueError:
			print("Bad input.")

class InkOpt():
	"""
	Reads and processes material info and ink formulation parameters to generate
	testable permutations.
	"""	
	
	def __init__(self):
		self.output = pd.DataFrame()
	
	def getData(self, input):
		self.data = pd.read_csv(input)
		
	def writeOutput(self):
		pd.write_csv(self.output)
		
	def setMaxPdfDelta(self, input):
		self.maxPdfDelta = np.float64(input)

	def setParams(self, fileInput = None):
		"""
		Get parameters.
		Specify a fileInput for non-interactive parameter acquisition.
		"""
		
		# Parameter dictionary
		params = {
			"maxDiffPdfs"	:		None,
			"maxPDf"		:		None,
			"minVgrin"		:		None,
			"minDnAvg"		:		None,
			"iMin"			:		None,
			"iMax"			:		None,
			"jMin"			:		None,
			"jMax"			:		None,
			"kMin"			:		None,
			"kMax"			:		None,
			"lMin"			:		None,
			"lMax"			:		None,
			"mMin"			:		None,
			"mMax"			:		None,
			"nMin"			:		None,
			"nMax"			:		None,
			"oMin"			:		None,
			"oMax"			:		None,
			"pMin"			:		None,
			"pMax"			:		None,
			"qMin"			:		None,
			"qMax"			:		None,
			"rMin"			:		None,
			"rMax"			:		None
		}
		
		if(fileInput == None):
			keys = [*params]
			prompts = [
				"Enter max difference between Pd,f_hi and Pd,f_lo",
				"Enter the max P(delta)d,f",
				"Enter the minimum Vgrin",
				"Enter the minimum avg of (delta)n",
				"Enter the first row for the np2 data",
				"Enter the last row for the np2 data",
				"Enter the first row for the np1 data",
				"Enter the last row for the np1 data",
				"Enter the first row for the n4 data",
				"Enter the last row for the n4 data",
				"Enter the first row for the n3 data",
				"Enter the last row for the n3 data",
				"Enter the first row for the n2 data",
				"Enter the last row for the n2 data",
				"Enter the first row for the n1 data",
				"Enter the last row for the n1 data",
				"Enter the minimum value of percent 4",
				"Enter the maximum value of percent 4",
				"Enter the minimum value of percent 3",
				"Enter the maximum value of percent 3",
				"Enter the minimum value of percent 2",
				"Enter the maximum value of percent 2",
				"Enter the minimum value of percent 1",
				"Enter the maximum value of percent 1"
			]
			for index, key in enumerate(keys):
				inputf(params, key, prompts[index])
		else:
			print("Non-interactive parameter acquisition not yet implemented.")
			quit()
			
		self.params = params
			
		return params
		
	def getParams(self):
		return self.params
		
	def permute():
		"""
		Permute the following lists with each other:
			Polymer1
			Polymer2
			NPs for Polymer1 (single)
			NPs for Polymer1 (pairs)
			NPs for Polymer2 (single, pairs)
		"""

if __name__ == "__main__":

	# Display ASCII banner from file
	print("\n", *[line for line in open(BANNERFILE).readlines()])

	inkopt = InkOpt()
	inkopt.getData(INPUTFILE)	# Get the material data table
	inkopt.setParams()	# Get parameters (interactively)
	# ^^ This can be updated to allow command-line argument for input file
	
	inkopt.permute() # Generate permutations
	
	# See what we did
	print("\nMaterial Data Table:\n", inkopt.data, "\n") # Display the imported material data
	print("Parameters:") # Display the specified parameters
	for key in inkopt.getParams():
		print("\t{}\t\t{}".format(key, inkopt.getParams()[key])) # Formatting (tab width) issue
	
"""
for i in range(iMin,iMax):
   # Get np2 data
    np2_486 = float(nanoM [i][1])
    np2_587 = float(nanoM [i][2])
    np2_656 = float(nanoM [i][3])
    # for j = jMin to jMax
    for j in range(jMin,jMax):
        # Get np1 data
        np1_486 = float(nanoM [j][1])
        np1_587 = float(nanoM [j][2])
        np1_656 = float(nanoM [j][3])
        # for k = kMin to kMax
        for k in range(kMin,kMax):
            # get n4 data (N4_486, N4_587, N4_656)
            n4_486 = float(nanoM [k][1])
            n4_587 = float(nanoM [k][2])
            n4_656 = float(nanoM [k][3])
            # for l = lMin to lMax
            for l in range(lMin,lMax):
                # get n3 data
                n3_486 = float(nanoM [l][1])
                n3_587 = float(nanoM [l][2])
                n3_656 = float(nanoM [l][3])            
                # for m = mMin to mMax
                for m in range(mMin,mMax):
                    # get n2 data
                    n2_486 = float(nanoM [m][1])
                    n2_587 = float(nanoM [m][2])
                    n2_656 = float(nanoM [m][3])               
                    # for n = nMin to nMax
                    for n in range(nMin,nMax):
                        # get n1 data
                        n1_486 = float(nanoM [n][1])
                        n1_587 = float(nanoM [n][2])
                        n1_656 = float(nanoM [n][3])                  
                        # for o = oMin to oMax
                        for o in range(oMin,oMax):
                            # PCT4 = o*0.003
                            Pct4 = o*0.003
                            dT = time.time() - T
                            T = time.time()
                            print(i,j,k,l,m,n,o,(Pdf_hi - Pdf_lo),Vgrin,Dnavg,dT)
                            # for p = pMin to pMax
                            for p in range(pMin,pMax):
                                # PCT3 = p*0.003
                                Pct3 = p*0.003
                                # for q = qMin to qMax
                                for q in range(qMin,qMax):
                                    # PCT2 = q*0.003
                                    Pct2 = q*0.003
                                    # for r = rMin to rMax
                                    for r in range(rMin,rMax):
                                        # PCT1 = r*003
                                        Pct1 = r*0.003
                                        # if (o + p <= 50 and q + r <= 50):
                                        #declare equations
                                        # DN_486 = xxxx
                                        Dn486 = (n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1-Pct3-Pct4))                                 
                                        # DN_587 = xxxx
                                        Dn587 = (n1_587*Pct1+n2_587*Pct2+np1_587*(1-Pct1-Pct2))-(n3_587*Pct3+n4_587*Pct4+np2_587*(1-Pct3-Pct4))                                 
                                        # DN_656 = xxxx
                                        Dn656 = (n1_656*Pct1+n2_656*Pct2+np1_656*(1-Pct1-Pct2))-(n3_656*Pct3+n4_656*Pct4+np2_656*(1-Pct3-Pct4))                                 
                                        # Pdf_hi = xxxx
                                        Pdf_hi = ((n1_587*Pct1+n2_587*Pct2+np1_587*(1-Pct1-Pct2))-(n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2)))
                                        Pdf_hi = Pdf_hi/((n1_656*Pct1+n2_656*Pct2+np1_656*(1-Pct1-Pct2))-(n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2)))
                                        # Pdf_lo = xxxx
                                        Pdf_lo = ((n3_587*Pct3+n4_587*Pct4+np2_587*(1-Pct3-Pct4))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1-Pct3-Pct4)))
                                        Pdf_lo = Pdf_lo/((n3_656*Pct3+n4_656*Pct4+np2_656*(1-Pct3-Pct4))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1- Pct3- Pct4)))                                  
                                        # PDF = xxxx
                                        if Dn656 == Dn486:
                                            PDf = 1e10
                                        else:
                                            PDf = (Dn587-Dn486)/(Dn656 - Dn486)
                                        # Vgrin = xxxx
                                        if Dn486 == Dn656:
                                            Vgrin = 1e10
                                        else: 
                                            Vgrin = Dn587/(Dn486 - Dn656)
                                        # Dnavg = xxxx
                                        Dnavg = (Dn486 + Dn587 + Dn656)/3                                  
                                  # IF ABS(Pdf_hi-Pdf_lo)<maxDiffPdfs
                                     # IF ABS(PDf)<maxPDf
                                        # IF ABS(Vgrin)>minVgrin
                                           # IF ABS(Dnavg)>minDnAvg
                                             # IF q + r <= 50
                                               # IF o + p <= 50
                                        if (abs(Pdf_hi - Pdf_lo) <= maxDiffPdfs
                                                and abs(PDf) <= maxPDf
                                                and abs(Vgrin) >= minVgrin 
                                                and abs(Dnavg) >= minDnAvg):
# Write "i,j,k,l,m,n,o,p,q,r,PCT1, PCT2,PCT3,PCT4,N1_486,N1_587,N1_656,N2_486,
#N2_587,N2_656,N3_486,N3_587,N3_656,N4_486,N4_587,N4_656,NP1_486,NP1_587,NP1_656
#,NP2_486,NP2_587,NP2_656,DN_486,DN_587,DN_656,Pdf_hi,Pdf_lo,ABS(Pdf_hi-Pdf_lo),
#ABS(PDF),ABS(Vgrin),ABS(Dnavg)"
                                            line = repr (i) 
                                            line = line + "," + repr(j)
                                            line = line + "," + repr(k)
                                            line = line + "," + repr(l)
                                            line = line + "," + repr(m)
                                            line = line + "," + repr(n)
                                            line = line + "," + repr(o)
                                            line = line + "," + repr(p)
                                            line = line + "," + repr(q)
                                            line = line + "," + repr(r)
                                            line = line + "," + repr(Pct1)
                                            line = line + "," + repr(Pct2)
                                            line = line + "," + repr(Pct3)
                                            line = line + "," + repr(Pct4)
                                            line = line + "," + repr(n1_486)
                                            line = line + "," + repr(n1_587)
                                            line = line + "," + repr(n1_656)
                                            line = line + "," + repr(n2_486)
                                            line = line + "," + repr(n2_587)
                                            line = line + "," + repr(n2_656)
                                            line = line + "," + repr(n3_486)
                                            line = line + "," + repr(n3_587)
                                            line = line + "," + repr(n3_656)
                                            line = line + ","+ repr (n4_486)
                                            line = line + "," + repr(n4_587)
                                            line = line + "," + repr(n4_656)
                                            line = line + ","+ repr(np1_486)
                                            line = line + ","+repr(np1_587)
                                            line = line + ","+repr(np1_656)
                                            line = line + ","+repr(np2_486)
                                            line = line + ","+repr(np2_587)
                                            line = line + ","+repr(np2_656)
                                            line = line + ","+repr(Dn486)
                                            line = line + "," + repr(Dn587)
                                            line = line + "," + repr(Dn656)
                                            line = line + ","+repr(Pdf_hi)
                                            line = line + ","+repr(Pdf_lo)
                                            line = line+","+repr(abs(Pdf_hi-Pdf_lo))
                                            line = line + ","+repr(abs(PDf))
                                            line = line+","+repr(abs(Vgrin))
                                            line = line+","+repr(abs(Dnavg))
  
                                            print(line)
                                 
                                            doc.write(line+"\r\n")
# end
doc.close()
"""